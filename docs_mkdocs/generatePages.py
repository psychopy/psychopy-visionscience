"""
This script will scan the repository for entry points and Python files and create a markdown file for each.

While you absolutely can write your docs manually if you prefer, we recommend running this file once as a starting point!
"""
from importlib import metadata, import_module
import sys
import textwrap
from pathlib import Path
from psychopy.experiment import Experiment


# if running with `--hard` set, delete existing files
hard = "--hard" in sys.argv

# specify path to docs source folder
docsFolder = Path(__file__).parent
# specify path to root folder (containing the pyproject.toml)
rootFolder = docsFolder.parent
# make sure there's an index file
if not (docsFolder / "index.md").is_file():
    (docsFolder / "index.md").write_text("")
# create a dummy experiment so we can initialize comps/routines to inspect their params
exp = Experiment()


def writeBuilderDocs(cls: type, group: str):
    """
    Write documentation for a Builder element, i.e. a Component or a Standalone Routine.

    Parameters
    ----------
    element : type
        Class of the Builder element to write documentation for
    group : str
        What kind of Builder element is this? Use "component" for a Component or "routine" for a Standalone Routine
    """
    # construct folder path and make sure it exists
    file = docsFolder / "builder" / group / (cls.__name__ + ".md")
    # make sure folder exists
    if not file.parent.is_dir():
        file.parent.mkdir(parents=True, exist_ok=True)
    # make sure builder folder has an index file
    if not (file.parent.parent / "index.md").is_file():
        content = (
            "Use the sidebar to navigate through the Builder elements added to the PsychoPy app by this plugin."
        )
        (file.parent / "index.md").write_text(content)
    # make sure folder has an index file
    if not (file.parent / "index.md").is_file():
        content = (
            f"Use the sidebar to navigate through the {group.title()}s added to the PsychoPy app by this plugin."
        )
        (file.parent / "index.md").write_text(content)
    # skip if file exists, unless we're running in hard mode
    if file.is_file() and not hard:
        return
    # make a component/routine with default attrs
    emt = cls(exp, "")
    # write the intro to the docs
    content = (
        f"# {cls.__name__}\n"
        f"{textwrap.dedent(emt.__doc__)}\n"
        f"\n"
        f"> **Categories:** {', '.join(emt.categories)}\n"
        f"> **Works in:** {', '.join(emt.targets)}\n"
        f"\n"
    )
    # start off with parameters heading
    content += (
        f"## Parameters\n"
        f"\n"
    )
    # sort params by category
    byCateg = {}
    for param in emt.params.values():
        if param.categ not in byCateg:
            byCateg[param.categ] = []
        byCateg[param.categ].append(param)
    # iterate through categs
    for categ, params in byCateg.items():
        # write a heading for each categ
        content += (
            f"### {categ}\n"
            f"\n"
        )
        # add each param...
        for param in params:
            # write basics (heading and description)
            content += (
                f"#### `{param.label}`\n"
                f"> {param.hint}\n"
            )
            # if there are options, display them
            if bool(param.allowedVals) or bool(param.allowedLabels):
                # write heading
                content += (
                    f"> \n"
                    f"> Options:\n"
                )
                # if no allowed labels, use allowed vals
                options = param.allowedLabels or param.allowedVals
                # add list item for each option
                for opt in options:
                    content += (
                        f"> - {opt}\n"
                    )
            # add newline at the end
            content += "\n"
        # save
        file.write_text(content, encoding="utf-8")


def writeCoderDocs(obj: type):
    """
    Write documentation for a Code element, e.g. a visual stim or a hardware device

    Parameters
    ----------
    obj : type or function
        Object to document
    """
    # make file path
    file = docsFolder / "coder" / (obj.__name__ + ".md")
    # make sure folder exists
    if not file.parent.is_dir():
        file.parent.mkdir(parents=True, exist_ok=True)
    # make sure folder has an index file
    if not (file.parent / "index.md").is_file():
        content = (
            "Use the sidebar to navigate through the code elements added to the PsychoPy library by this plugin."
        )
        (file.parent / "index.md").write_text(content)
    # skip if file exists, unless we're running in hard mode
    if file.is_file() and not hard:
        return
    # start with no content
    content = ""
    # add import instructions
    content += (
        f"To import {obj.__name__}, you can either use:\n"
        f"```python\n"
        f"from {obj.__module__} import {obj.__name__}\n"
        f"```\n"
        f"or, any time after `psychopy.plugins.activatePlugins` has been called:\n"
        f"```python\n"
        f"from {ep.group} import {ep.name}\n"
        f"```\n"
        f"\n"
    )
    # add documentation
    content += (
        f"::: {ep.value.replace(':', '.')}"
    )

    file.write_text(content, encoding="utf-8")


# get path for the module folder (will be the first folder found which contains an __init__.py)
modFolder = list(rootFolder.glob("*/__init__.py"))[0].parent
# find all entry point groups
for group in metadata.entry_points():
    # make sure it's pointing to psychopy
    if not group.startswith("psychopy"):
        continue
    # find all entry points for this group
    for ep in metadata.entry_points(group=group):
        # make sure it's come from a module from this plugin
        if not ep.module.split(".")[0] == modFolder.stem:
            continue
        # load object
        obj = ep.load()
        # write docs
        if group.startswith("psychopy.experiment.components") or group.startswith("psychopy.experiment.routines"):
            # if it's for Builder, write special Builder docs
            writeBuilderDocs(obj, group=group.split(".")[-1])
        else:
            # anything else, write for Coder
            writeCoderDocs(obj)
