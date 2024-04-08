from pathlib import Path
import shutil
import time

# specify path to docs source folder
docsFolder = Path(__file__).parent
# specify path to root folder (containing the pyproject.toml)
rootFolder = docsFolder.parent
# specify path for the module folder (will be the first folder found which contains an __init__.py)
modFolder = list(rootFolder.glob("*/__init__.py"))[0].parent
# specify path to api folder
apiFolder = docsFolder / "api"
# clear api folder
shutil.rmtree(apiFolder, ignore_errors=True)
# make fresh
time.sleep(0.1)
apiFolder.mkdir(parents=True, exist_ok=True)

# find all python files
for file in modFolder.glob("**/*.py"):
    # construct relative path to docs folder
    docsFile = apiFolder / file.relative_to(modFolder)
    # change extension to markdown
    docsFile = docsFile.parent / (docsFile.stem + ".md")
    # replace __init__ with index
    if docsFile.stem == "__init__":
        docsFile = docsFile.parent / ("index.md")
    # make sure folder exists
    docsFile.parent.mkdir(parents=True, exist_ok=True)
    # get parents for import
    parents = [f.stem for f in file.relative_to(rootFolder).parents if f.stem]
    parents.reverse()
    # if not an index file, give own name to import string too
    if file.stem != "__init__":
        parents.append(file.stem)
    # build import string
    importString = ".".join(parents)
    # construct content
    content = (
        "::: " + importString
    )
    # write content
    docsFile.write_text(content, encoding="utf-8")