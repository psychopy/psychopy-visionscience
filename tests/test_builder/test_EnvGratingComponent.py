from psychopy_visionscience.components.envelopegrating import EnvGratingComponent
from psychopy_visionscience.secondorder import EnvelopeGrating
from psychopy.tests.test_experiment.test_components.test_base_components import BaseComponentTests, _TestLibraryClassMixin

class TestEnvGratingComponent(BaseComponentTests, _TestLibraryClassMixin):
    """
    Tests the Envelope Stim Component writes its code correctly
    """
    comp = EnvGratingComponent
    libraryClass = EnvelopeGrating
