# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""generator: coverage testing."""
import os

from polynomial import generator
from polynomial import sds_glob

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test case: Generator() - Create an instance.
# -----------------------------------------------------------------------------
def test_generator():
    """Test case: Generator() - Create an instance."""
    # -------------------------------------------------------------------------
    generator.Generator(os.environ[sds_glob.POLYNOMIAL_FILE_NAME])
