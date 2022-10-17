# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""launcher: coverage testing."""
import os
import platform

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test case: launcher() - -a generate.
# -----------------------------------------------------------------------------
def test_launcher_generate():
    """Test case: launcher() - Generator."""
    # -------------------------------------------------------------------------
    if platform.system() == "Windows":
        os.system("src\\polynomial\\launcher.py -a generate")
    elif platform.system() == "Linux":
        os.system("src/polynomial/launcher.py -a generate")


# -----------------------------------------------------------------------------
# Test case: launcher() - -a multiply -m fft.
# -----------------------------------------------------------------------------
def test_launcher_multiply_numpy():
    """Test case: launcher() - Multiplier - numpy."""
    # -------------------------------------------------------------------------
    if platform.system() == "Windows":
        os.system("src\\polynomial\\launcher.py -a multiply -m numpy")
    elif platform.system() == "Linux":
        os.system("src/polynomial/launcher.py -a multiply -m numpy")
