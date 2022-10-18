# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""sds_config: fatal testing."""

import pytest

from polynomial import polynomial_error
from polynomial import sds_config
from polynomial import sds_glob

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# ------------------------------------------------------------------
# ERROR.00.903 Unknown configuration parameter: Key='{key}'
# Value='{value}
# ------------------------------------------------------------------
def test_error_00_903():
    """Test ERROR_00_903."""
    sds_glob.inst_config = sds_config.Config()

    with pytest.raises(polynomial_error.PolynomialError) as expt:
        sds_config.Config(
            pytest.helpers.get_full_name_from_components(
                pytest.helpers.get_test_files_source_directory_name(), "setup_903.cfg"
            )
        )

    assert expt.type == polynomial_error.PolynomialError, "ERROR.00.903"
    assert str(expt.value)[:12] == "ERROR.00.903"


# ------------------------------------------------------------------
# ERROR.00.904 The specified configuration file '{file}' is either
# not a file or does not exist at all
# ------------------------------------------------------------------
def test_error_00_904():
    """Test ERROR_00_904."""
    sds_glob.inst_config = sds_config.Config()

    with pytest.raises(polynomial_error.PolynomialError) as expt:
        sds_config.Config(
            pytest.helpers.get_full_name_from_components(
                pytest.helpers.get_test_files_source_directory_name(), "setup_904.cfg"
            )
        )

    assert expt.type == polynomial_error.PolynomialError, "ERROR.00.904"
    assert str(expt.value)[:12] == "ERROR.00.904"


# ------------------------------------------------------------------
# ERROR.00.905 Illegal configuration parameter value '{value}' -
# only 'false' or 'true' are allowed
# ------------------------------------------------------------------
def test_error_00_905():
    """Test ERROR_00_905."""
    sds_glob.inst_config = sds_config.Config()

    with pytest.raises(polynomial_error.PolynomialError) as expt:
        sds_config.Config(
            pytest.helpers.get_full_name_from_components(
                pytest.helpers.get_test_files_source_directory_name(), "setup_905.cfg"
            )
        )

    assert expt.type == polynomial_error.PolynomialError, "ERROR.00.905"
    assert str(expt.value)[:12] == "ERROR.00.905"


# ------------------------------------------------------------------
# ERROR.00.906 Illegal configuration parameter value '{value}' -
# only integers are allowed
# ------------------------------------------------------------------
def test_error_00_906():
    """Test ERROR_00_906."""
    sds_glob.inst_config = sds_config.Config()

    with pytest.raises(polynomial_error.PolynomialError) as expt:
        sds_config.Config(
            pytest.helpers.get_full_name_from_components(
                pytest.helpers.get_test_files_source_directory_name(), "setup_906.cfg"
            )
        )

    assert expt.type == polynomial_error.PolynomialError, "ERROR.00.906"
    assert str(expt.value)[:12] == "ERROR.00.906"


# ------------------------------------------------------------------
# ERROR.00.907 The number of tasks must be at least 1 and
# not {no_tasks}
# ------------------------------------------------------------------
def test_error_00_907():
    """Test ERROR_00_907."""
    sds_glob.inst_config = sds_config.Config()

    with pytest.raises(polynomial_error.PolynomialError) as expt:
        sds_glob.inst_config.set_no_tasks(0)

    assert expt.type == polynomial_error.PolynomialError, "ERROR.00.907"
    assert str(expt.value)[:12] == "ERROR.00.907"


# ------------------------------------------------------------------
# ERROR.00.908 The minimum degree must be at least 1 and
# not {degree_min}
# ------------------------------------------------------------------
def test_error_00_908():
    """Test ERROR_00_908."""
    sds_glob.inst_config = sds_config.Config()

    with pytest.raises(polynomial_error.PolynomialError) as expt:
        sds_glob.inst_config.set_degree(0, 1)

    assert expt.type == polynomial_error.PolynomialError, "ERROR.00.908"
    assert str(expt.value)[:12] == "ERROR.00.908"


# ------------------------------------------------------------------
# ERROR.00.909 The maximum degree {degree_max} must be at least
# equal to the minimum degree {degree_min}
# ------------------------------------------------------------------
def test_error_00_909():
    """Test ERROR_00_909."""
    sds_glob.inst_config = sds_config.Config()

    with pytest.raises(polynomial_error.PolynomialError) as expt:
        sds_glob.inst_config.set_degree(1, 0)

    assert expt.type == polynomial_error.PolynomialError, "ERROR.00.909"
    assert str(expt.value)[:12] == "ERROR.00.909"


# ------------------------------------------------------------------
# ERROR.00.910 The maximum coef {coef_max} must be at least equal
# to the minimum coef {coef_min}
# ------------------------------------------------------------------
def test_error_00_910():
    """Test ERROR_00_910."""
    sds_glob.inst_config = sds_config.Config()

    with pytest.raises(polynomial_error.PolynomialError) as expt:
        sds_glob.inst_config.set_coef(1, 0)

    assert expt.type == polynomial_error.PolynomialError, "ERROR.00.910"
    assert str(expt.value)[:12] == "ERROR.00.910"
