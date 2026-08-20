from psychopy.tests.utils import profiledImport


def test_component_import():
    """
    Test that Components can be imported in good time and without touching costly packages.
    """
    for ref in [
        "psychopy_visionscience.components.envelopegrating",
        "psychopy_visionscience.components.noise",
        "psychopy_visionscience.components.radial",
    ]:
        profiledImport(
            ref=ref,
            notouch=[
                "psychopy.visual",
                "psychopy_visionscience.noise",
                "psychopy_visionscience.radial",
                "psychopy_visionscience.secondorder",
            ]
        )
