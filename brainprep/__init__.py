# -*- coding: utf-8 -*-
##########################################################################
# NSAp - Copyright (C) CEA, 2021
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
Package that provides tools for brain MRI Deep Leanring PreProcessing.
"""

# Imports
from .info import __version__
from .utils import (
    write_matlabbatch, check_command, check_version, execute_command)
from .spatial import (
    scale, bet2, reorient2std, biasfield, register_affine, apply_affine,
    apply_mask)
from .cortical import recon_all, localgi
