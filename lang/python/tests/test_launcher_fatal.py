# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""launcher: coverage testing."""
import os
import platform

from polynomial import sds_glob

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test case: launcher() - -a n/a.
# -----------------------------------------------------------------------------
def test_launcher_action():
    """Test case: launcher() - Action."""
    # -------------------------------------------------------------------------
    if platform.system() == "Windows":
        os.system(
            "src\\polynomial\\launcher.py -a " + sds_glob.INFORMATION_NOT_YET_AVAILABLE
        )
    elif platform.system() == "Linux":
        os.system(
            "src/polynomial/launcher.py -a " + sds_glob.INFORMATION_NOT_YET_AVAILABLE
        )


# -----------------------------------------------------------------------------
# Test case: launcher() - -m n/a.
# -----------------------------------------------------------------------------
def test_launcher_method():
    """Test case: launcher() - Method."""
    # -------------------------------------------------------------------------
    if platform.system() == "Windows":
        os.system(
            "src\\polynomial\\launcher.py -a multiply -m "
            + sds_glob.INFORMATION_NOT_YET_AVAILABLE
        )
    elif platform.system() == "Linux":
        os.system(
            "src/polynomial/launcher.py -a multiply -m "
            + sds_glob.INFORMATION_NOT_YET_AVAILABLE
        )
