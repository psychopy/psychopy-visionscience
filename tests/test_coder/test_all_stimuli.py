import sys, os, copy
from pathlib import Path

from psychopy import visual, monitors, prefs, constants
from psychopy.visual import filters
from psychopy.tools.coordinatetools import pol2cart
from psychopy.tests import utils
from psychopy.tests import skip_under_vm, requires_plugin
from psychopy.tools import systemtools
from psychopy_visionscience import secondorder, noise, radial
import numpy
import pytest
import shutil
from tempfile import mkdtemp

"""Each test class creates a context subclasses _baseVisualTest to run a series
of tests on a single graphics context (e.g. pyglet with shaders)

To add a new stimulus test use _base so that it gets tested in all contexts

"""


class _TestPluginVisualStim:
    @classmethod
    def setup_class(self):#run once for each test class (window)
        self.win=None
        self.contextName
        raise NotImplementedError

    @classmethod
    def teardown_class(self):#run once for each test class (window)
        self.win.close()#shutil.rmtree(self.temp_dir)

    def setup_method(self):#this is run for each test individually
        #make sure we start with a clean window
        self.win.flip()

    def test_envelopeGratingAndRaisedCos(self):
        win = self.win
        size = numpy.array([2.0, 2.0]) * self.scaleFactor
        if win.units in ['norm', 'height']:
            sf = 5
        else:
            sf = 5.0 / size  # this will do the flipping and get exactly one cycle
        if win._haveShaders == True:  # can't draw envelope gratings without shaders so skip this test
            image = secondorder.EnvelopeGrating(win, carrier='sin', envelope='sin',
                                           size=size, sf=sf, mask='raisedCos',
                                           ori=-45, envsf=sf / 2, envori=45,
                                           envphase=90, moddepth=0.5,
                                           contrast=0.5)
            image.draw()
            utils.compareScreenshot('envelopeandrcos_%s.png' % (self.contextName), win)
            win.flip()
            "{}".format(image)

    def test_envelopeGratingPowerAndRaisedCos(self):
        win = self.win
        size = numpy.array([2.0, 2.0]) * self.scaleFactor
        if win.units in ['norm', 'height']:
            sf = 5
        else:
            sf = 5.0 / size  # this will do the flipping and get exactly one cycle
        if win._haveShaders == True:  # can't draw envelope gratings without shaders so skip this test
            image = secondorder.EnvelopeGrating(win, carrier='sin', envelope='sin',
                                           size=size, sf=sf, mask='raisedCos',
                                           ori=-45, envsf=sf / 2, envori=45,
                                           envphase=90, moddepth=0.5, power=0.5,
                                           contrast=0.5)
            image.draw()
            utils.compareScreenshot('envelopepowerandrcos_%s.png' % (self.contextName), win)
            win.flip()
            "{}".format(image)

    def test_NoiseStim_defaults(self):
        noiseTypes = ['binary', 'uniform', 'normal', 'white', 'filtered']

        for noiseType in noiseTypes:
            stim = noise.NoiseStim(
                win=self.win,
                noiseType=noiseType,
                size=(32, 32),
                units='pix'
            )
            stim.updateNoise()
            stim.draw()

    def test_NoiseStim_defaults_image(self):
        noiseType = 'image'

        # noiseImage kwarg missing.
        with pytest.raises(ValueError):
            noise.NoiseStim(win=self.win,
                             noiseType=noiseType,
                             size=(32, 32),
                             units='pix')

    def test_noiseAndRaisedCos(self):
        numpy.random.seed(1)
        win = self.win
        size = numpy.array([2.0, 2.0]) * self.scaleFactor
        tres = 128
        elementsize = 4
        sf = None
        fileName = os.path.join(utils.TESTS_DATA_PATH, 'testimagegray.jpg')
        if win.units in ['pix']:
            ntype = 'Binary'
            size = numpy.array([128, 128])
        elif win.units in ['degFlatPos']:
            ntype = 'Gabor'
            sf = 0.125
        elif win.units in ['degFlat']:
            ntype = 'Isotropic'
            sf = 0.125
        elif win.units in ['deg']:
            ntype = 'Filtered'
            sf = 0.125
        elif win.units in ['cm']:
            ntype = 'Image'
            sf = 0.25
        else:
            if self.contextName == 'stencil':
                ntype = 'White'
            elif self.contextName == 'height':
                ntype = 'Uniform'
            else:
                ntype = 'Normal'
            elementsize = 1.0 / 8.0
        image = noise.NoiseStim(win=win, name='noise', units=win.units,
                                 noiseImage=fileName, mask='raisedCos',
                                 ori=0, pos=(0, 0), size=size, sf=sf, phase=0,
                                 color=[1, 1, 1], colorSpace='rgb', opacity=1, blendmode='avg',
                                 contrast=0.5,
                                 texRes=tres,
                                 noiseType=ntype, noiseElementSize=elementsize,
                                 noiseBaseSf=32.0 / size[0],
                                 noiseBW=0.5, noiseBWO=7, noiseFractalPower=-1,
                                 noiseFilterLower=4.0 / size[0], noiseFilterUpper=16.0 / size[0],
                                 noiseFilterOrder=1, noiseClip=4.0, interpolate=False, depth=-1.0)
        image.draw()
        utils.compareScreenshot('noiseAndRcos_%s.png' % (self.contextName), win)
        win.flip()
        str(image)

    def test_noiseFiltersAndRaisedCos(self):
        numpy.random.seed(1)
        win = self.win
        size = numpy.array([2.0, 2.0]) * self.scaleFactor
        tres = 128
        elementsize = 4
        sf = None
        ntype = 'Binary'
        comp = 'Amplitude'
        fileName = os.path.join(utils.TESTS_DATA_PATH, 'testimagegray.jpg')
        if win.units in ['pix']:
            ftype = 'Butterworth'
            size = numpy.array([128, 128])
        elif win.units in ['degFlatPos']:
            ftype = 'Gabor'
            sf = 0.125
            elementsize = 1
        elif win.units in ['degFlat']:
            ftype = 'Isotropic'
            sf = 0.125
            elementsize = 1
        elif win.units in ['deg']:
            ntype = 'Image'
            ftype = 'Butterworth'
            sf = 0.125
        elif win.units in ['cm']:
            ntype = 'Image'
            ftype = 'Butterworth'
            comp = 'Phase'
            sf = 0.25
        else:
            if self.contextName == 'stencil':
                ntype = 'White'
                ftype = 'Butterworth'
            elif self.contextName == 'height':
                ntype = 'Uniform'
                ftype = 'Butterworth'
            else:
                ntype = 'Normal'
                ftype = 'Butterworth'
            elementsize = 1.0 / 8.0
        image = noise.NoiseStim(win=win, name='noise', units=win.units,
                                 noiseImage=fileName, mask='raisedCos',
                                 ori=0, pos=(0, 0), size=size, sf=sf, phase=0,
                                 color=[1, 1, 1], colorSpace='rgb', opacity=1, blendmode='avg',
                                 contrast=0.5,
                                 texRes=tres,
                                 noiseType=ntype, noiseElementSize=elementsize,
                                 noiseBaseSf=32.0 / size[0],
                                 noiseBW=0.5, noiseBWO=7, noiseFractalPower=-1,
                                 noiseFilterLower=4.0 / size[0],
                                 noiseFilterUpper=16.0 / size[0], noiseFilterOrder=1, noiseOri=45.0,
                                 noiseClip=4.0, imageComponent=comp, filter=ftype,
                                 interpolate=False, depth=-1.0)

        image.draw()
        utils.compareScreenshot('noiseFiltersAndRcos_%s.png' % (self.contextName), win)
        win.flip()
        str(image)

    def test_envelopeBeatAndRaisedCos(self):
        win = self.win
        size = numpy.array([2.0, 2.0]) * self.scaleFactor
        if win.units in ['norm', 'height']:
            sf = 5
        else:
            sf = 5.0 / size  # this will do the flipping and get exactly one cycle
        if win._haveShaders == True:  # can't draw envelope gratings without shaders so skip this test
            image = secondorder.EnvelopeGrating(win, carrier='sin', envelope='sin',
                                           size=size, sf=sf, mask='raisedCos',
                                           ori=-45, envsf=sf / 2, envori=45,
                                           envphase=90, beat=True, moddepth=0.5,
                                           contrast=0.5)
            image.draw()
            utils.compareScreenshot('beatandrcos_%s.png' % (self.contextName), win)
            win.flip()
            "{}".format(image)

    def test_radial(self):
        win = self.win
        #using init
        wedge = radial.RadialStim(win, tex='sqrXsqr', color=1, size=2* self.scaleFactor,
            visibleWedge=[0, 45], radialCycles=2, angularCycles=2, interpolate=False)
        wedge.draw()
        thresh = 15  # there are often a slight interpolation differences
        if win.winType != 'pygame':  # pygame definitely gets radialstim wrong!
            utils.compareScreenshot('wedge1_%s.png' %(self.contextName),
                                    win, crit=thresh)
        win.flip()#AFTER compare screenshot

        #using .set()
        wedge.mask = 'gauss'
        wedge.size = 3 * self.scaleFactor
        wedge.angularCycles = 3
        wedge.radialCycles = 3
        wedge.ori = 180
        wedge.contrast = 0.8
        wedge.opacity = 0.8
        wedge.radialPhase += 0.1
        wedge.angularPhase = 0.1
        wedge.draw()
        "{}".format(wedge) #check that str(xxx) is working
        if win.winType != 'pygame': # pygame gets this wrong:
            utils.compareScreenshot('wedge2_%s.png' %(self.contextName),
                                    win, crit=thresh)
        else:
            pytest.skip("Pygame fails to render RadialStim properly :-/")

# variants of the base tests with different backends (copied from psychopy)

class TestPygletNorm(_TestPluginVisualStim):
    @classmethod
    def setup_class(self):
        self.win = visual.Window([128, 128], winType='pyglet', pos=[50, 50],
                                 allowStencil=True, autoLog=False)
        self.contextName = 'norm'
        self.scaleFactor = 1  # applied to size/pos values


class TestPygletHexColor(_TestPluginVisualStim):
    @classmethod
    def setup_class(self):
        self.win = visual.Window([128, 128], winType='pyglet', pos=[50, 50],
                                 color="#FF0099",
                                 allowStencil=True, autoLog=False)
        self.contextName = 'normHexbackground'
        self.scaleFactor = 1  # applied to size/pos values


if not systemtools.isVM_CI():
    class TestPygletBlendAdd(_TestPluginVisualStim):
        @classmethod
        def setup_class(self):
            self.win = visual.Window([128, 128], winType='pyglet', pos=[50, 50],
                                     blendMode='add', useFBO=True)
            self.contextName = 'normAddBlend'
            self.scaleFactor = 1  # applied to size/pos values


class TestPygletNormFBO(_TestPluginVisualStim):
    @classmethod
    def setup_class(self):
        self.win = visual.Window([128, 128], units="norm", winType='pyglet', pos=[50, 50],
                                 allowStencil=True, autoLog=False, useFBO=True)
        self.contextName = 'norm'
        self.scaleFactor = 1  # applied to size/pos values


class TestPygletHeight(_TestPluginVisualStim):
    @classmethod
    def setup_class(self):
        self.win = visual.Window([128, 64], units="height", winType='pyglet', pos=[50, 50],
                                 allowStencil=False, autoLog=False)
        self.contextName = 'height'
        self.scaleFactor = 1  # applied to size/pos values


class TestPygletNormStencil(_TestPluginVisualStim):
    @classmethod
    def setup_class(self):
        self.win = visual.Window([128, 128], units="norm", monitor='testMonitor',
                                 winType='pyglet', pos=[50, 50],
                                 allowStencil=True, autoLog=False)
        self.contextName = 'stencil'
        self.scaleFactor = 1  # applied to size/pos values


class TestPygletPix(_TestPluginVisualStim):
    @classmethod
    def setup_class(self):
        mon = monitors.Monitor('testMonitor')
        mon.setDistance(57)
        mon.setWidth(40.0)
        mon.setSizePix([1024, 768])
        self.win = visual.Window([128, 128], units="pix", monitor=mon,
                                 winType='pyglet', pos=[50, 50],
                                 allowStencil=True, autoLog=False)
        self.contextName = 'pix'
        self.scaleFactor = 60  # applied to size/pos values


class TestPygletCm(_TestPluginVisualStim):
    @classmethod
    def setup_class(self):
        mon = monitors.Monitor('testMonitor')
        mon.setDistance(57.0)
        mon.setWidth(40.0)
        mon.setSizePix([1024, 768])
        self.win = visual.Window([128, 128], units="cm", monitor=mon,
                                 winType='pyglet', pos=[50, 50],
                                 allowStencil=False, autoLog=False)
        self.contextName = 'cm'
        self.scaleFactor = 2  # applied to size/pos values


class TestPygletDeg(_TestPluginVisualStim):
    @classmethod
    def setup_class(self):
        mon = monitors.Monitor('testMonitor')
        mon.setDistance(57.0)
        mon.setWidth(40.0)
        mon.setSizePix([1024, 768])
        self.win = visual.Window([128, 128], units="deg", monitor=mon,
                                 winType='pyglet', pos=[50, 50], allowStencil=True,
                                 autoLog=False)
        self.contextName = 'deg'
        self.scaleFactor = 2  # applied to size/pos values


class TestPygletDegFlat(_TestPluginVisualStim):
    @classmethod
    def setup_class(self):
        mon = monitors.Monitor('testMonitor')
        mon.setDistance(10.0)  # exaggerate the effect of flatness by setting the monitor close
        mon.setWidth(40.0)
        mon.setSizePix([1024, 768])
        self.win = visual.Window([128, 128], units="degFlat", monitor=mon,
                                 winType='pyglet', pos=[50, 50],
                                 allowStencil=True, autoLog=False)
        self.contextName = 'degFlat'
        self.scaleFactor = 4  # applied to size/pos values


class TestPygletDegFlatPos(_TestPluginVisualStim):
    @classmethod
    def setup_class(self):
        mon = monitors.Monitor('testMonitor')
        mon.setDistance(10.0)  # exaggerate the effect of flatness by setting the monitor close
        mon.setWidth(40.0)
        mon.setSizePix([1024, 768])
        self.win = visual.Window([128, 128], units='degFlatPos', monitor=mon,
                                 winType='pyglet', pos=[50, 50],
                                 allowStencil=True, autoLog=False)
        self.contextName = 'degFlatPos'
        self.scaleFactor = 4  # applied to size/pos values
