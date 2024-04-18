from psychopy_visionscience.components.noise import NoiseStimComponent
from psychopy_visionscience.noise import NoiseStim
from psychopy.tests.test_experiment.test_components.test_base_components import BaseComponentTests, _TestLibraryClassMixin

class TestNoiseStimComponent(BaseComponentTests, _TestLibraryClassMixin):
    """
    Tests the Noise Stim Component writes its code correctly
    """
    comp = NoiseStimComponent
    libraryClass = NoiseStim
