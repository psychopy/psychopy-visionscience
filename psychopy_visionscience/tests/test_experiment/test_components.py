from psychopy.tests.test_experiment.test_components import TestComponents
from psychopy import plugins


class TestVisionscienceComponents(TestComponents):
    """
    Run the usual TestComponents test from the PsychoPy library, with this plugin installed and
    activated
    """

    @classmethod
    def setup_class(cls):
        # activate plugins
        plugins.activatePlugins()
        # continue as normal
        return TestComponents.setup_class(cls)
