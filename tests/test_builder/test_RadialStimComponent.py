from psychopy_visionscience.components.radial import RadialStimComponent
from psychopy_visionscience.radial import RadialStim
from psychopy.tests.test_experiment.test_components.test_base_components import BaseComponentTests, _TestLibraryClassMixin

class TestRadialStimComponent(BaseComponentTests, _TestLibraryClassMixin):
    """
    Tests the Radial Stim Component writes its code correctly
    """
    comp = RadialStimComponent
    libraryClass = RadialStim
