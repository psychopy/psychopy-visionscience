#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Originally from the PsychoPy library
# Copyright (C) 2002-2018 Jonathan Peirce (C) 2019-2022 Open Science Tools Ltd.
# Distributed under the terms of the GNU General Public License (GPL).

"""Various visual stimuli classes and Builder components useful to vision
scientists.
"""

import importlib.metadata

try:
    __version__ = importlib.metadata.version("psychopy-visionscience")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.dev"

# NOTE: Be sure to register entry points in the `pyproject.toml` file.

# ------------------------------------------------------------------------------
# Library Classes
#
from .noise import NoiseStim
from .secondorder import EnvelopeGrating
from .radial import RadialStim

# ------------------------------------------------------------------------------
# Components
#
from .components import NoiseStimComponent, EnvGratingComponent, RadialStimComponent
