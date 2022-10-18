# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""multiplier: fatal testing."""

import pytest

from polynomial import multiplier
from polynomial import sds_glob
from polynomial.polynomial_error import PolynomialError

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# ------------------------------------------------------------------
# ERROR.00.902 The specified JSON file {file_name} does not exist
# ------------------------------------------------------------------
@pytest.mark.issue
def test_error_00_902():
    """Test ERROR_00_902."""
    with pytest.raises(PolynomialError) as expt:
        multiplier.Multiplier(
            file_name=sds_glob.INFORMATION_NOT_YET_AVAILABLE,
            method=sds_glob.INFORMATION_NOT_YET_AVAILABLE,
        )

    assert expt.type == PolynomialError, "ERROR.00.902"
    assert str(expt.value)[:12] == "ERROR.00.902"
