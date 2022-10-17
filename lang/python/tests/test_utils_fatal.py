# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""utils: fatal testing."""
import pytest

from polynomial import utils
from polynomial.polynomial_error import PolynomialError

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# ERROR.00.901 The required instance of the class '{Class}' does not yet exist.
# -----------------------------------------------------------------------------
def test_error_00_901():
    """Test case: check_exists_object() - Check the existence of objects."""
    utils.check_exists_object(is_config=False)

    with pytest.raises(PolynomialError) as expt:
        utils.check_exists_object(is_config=True)

    assert expt.type == PolynomialError, "ERROR.00.901"
    assert str(expt.value)[:12] == "ERROR.00.901"


# -----------------------------------------------------------------------------
# Test case: terminate_fatal() - Terminate the application immediately.
# -----------------------------------------------------------------------------
@pytest.mark.issue
def test_terminate_fatal():
    """Test case: terminate_fatal() - Terminate the application immediately."""
    with pytest.raises(PolynomialError) as expt:
        utils.terminate_fatal(error_msg="Good bye World! (from terminate_fatal())")

    assert (
        expt.type == PolynomialError
    ), "Function terminate_fatal() not terminating as expected"
