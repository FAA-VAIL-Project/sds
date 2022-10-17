# pylint: disable=duplicate-code

# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""sds_config: coverage testing."""
import pytest

from polynomial import sds_config

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test case: exists() - Check the object existence.
# -----------------------------------------------------------------------------
def test_exists():
    """Test case: exists() - Check the object existence."""
    my_instance = sds_config.Config()

    assert (
        my_instance.exists()
    ), "exists() - the instance of the class 'Config' is missing"

    my_instance.load_config_file(
        pytest.helpers.get_full_name_from_components(
            pytest.helpers.get_test_files_source_directory_name(),
            "setup.complete_false.cfg",
        )
    )
