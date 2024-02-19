from psychopy.tests.test_experiment.test_params import TestStyle
from psychopy import plugins


class TestVisionscienceComponents(TestStyle):
    """
    Run the usual TestStyle test from the PsychoPy library, with this plugin installed and
    activated
    """

    @classmethod
    def setup_class(cls):
        # activate plugins
        plugins.activatePlugins()
        # continue as normal
        return TestStyle.setup_class(cls)
