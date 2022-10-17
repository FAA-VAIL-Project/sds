# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""sds_config: fatal testing."""

import pytest

from polynomial import sds_config
from polynomial import sds_glob
from polynomial.polynomial_error import PolynomialError

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# ------------------------------------------------------------------
# ERROR.00.903 Unknown configuration parameter: Key='{key}' Value='{value}
# ------------------------------------------------------------------
def test_error_00_903():
    """Test ERROR_00_903."""
    my_config = sds_config.Config()

    with pytest.raises(PolynomialError) as expt:
        my_config.set_config_value(sds_glob.INFORMATION_NOT_YET_AVAILABLE, False)

    assert expt.type == PolynomialError, "ERROR.00.903"
    assert str(expt.value)[:12] == "ERROR.00.903"


# ------------------------------------------------------------------
# ERROR.00.904 The specified configuration file '{file}' is either not
# a file or does not exist at all.
# ------------------------------------------------------------------
def test_error_00_904():
    """Test ERROR_00_904."""
    with pytest.raises(PolynomialError) as expt:
        sds_config.Config(sds_glob.INFORMATION_NOT_YET_AVAILABLE)

    assert expt.type == PolynomialError, "ERROR.00.904"
    assert str(expt.value)[:12] == "ERROR.00.904"


# ------------------------------------------------------------------
# ERROR.00.905 Illegal configuration parameter value '{value}' -
# only 'false' or 'true' are allowed
# ------------------------------------------------------------------
def test_error_00_905():
    """Test ERROR_00_905."""
    my_config = sds_config.Config()

    with pytest.raises(PolynomialError) as expt:
        my_config.set_config_value(
            sds_glob.CONFIG_PARAM_VERBOSE,
            sds_glob.INFORMATION_NOT_YET_AVAILABLE,
        )

    assert expt.type == PolynomialError, "ERROR.00.905"
    assert str(expt.value)[:12] == "ERROR.00.905"
