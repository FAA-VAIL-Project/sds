# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""multiplier: coverage testing."""
import os

import pytest

from polynomial import multiplier
from polynomial import sds_glob

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test case: Multiplier() - Create an instance - Method 'fft'.
# -----------------------------------------------------------------------------
def test_cover_multiplier_fft_01():
    """Test case: Multiplier() - Create an instance - Method 'fft'."""
    # -------------------------------------------------------------------------
    pytest.helpers.copy_file_4_pytest("polynom_data_01.json")

    # -------------------------------------------------------------------------
    multiplier.Multiplier(
        file_name=os.environ[sds_glob.POLYNOMIAL_FILE_NAME],
        method=sds_glob.ARG_METHOD_FFT,
    )


# -----------------------------------------------------------------------------
# Test case: Multiplier() - Create an instance - Method 'fft'.
# -----------------------------------------------------------------------------
def test_cover_multiplier_fft_02():
    """Test case: Multiplier() - Create an instance - Method 'fft'."""
    # -------------------------------------------------------------------------
    pytest.helpers.copy_file_4_pytest("polynom_data_02.json")

    # -------------------------------------------------------------------------
    multiplier.Multiplier(
        file_name=os.environ[sds_glob.POLYNOMIAL_FILE_NAME],
        method=sds_glob.ARG_METHOD_FFT,
    )


# -----------------------------------------------------------------------------
# Test case: Multiplier() - Create an instance - Method 'numpy'.
# -----------------------------------------------------------------------------
def test_cover_multiplier_numpy():
    """Test case: Multiplier() - Create an instance - Method 'numpy'."""
    # -------------------------------------------------------------------------
    pytest.helpers.copy_file_4_pytest("polynom_data_01.json")

    # -------------------------------------------------------------------------
    multiplier.Multiplier(
        file_name=os.environ[sds_glob.POLYNOMIAL_FILE_NAME],
        method=sds_glob.ARG_METHOD_NUMPY,
    )


# -----------------------------------------------------------------------------
# Test case: Multiplier() - Create an instance - Method 'simple'.
# -----------------------------------------------------------------------------
def test_cover_multiplier_simple():
    """Test case: Multiplier() - Create an instance - Method 'simple'."""
    # -------------------------------------------------------------------------
    pytest.helpers.copy_file_4_pytest("polynom_data_01.json")

    # -------------------------------------------------------------------------
    multiplier.Multiplier(
        file_name=os.environ[sds_glob.POLYNOMIAL_FILE_NAME],
        method=sds_glob.ARG_METHOD_SIMPLE,
    )
