# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""sds_config: coverage testing."""

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

    my_instance.set_config_value(sds_config.sds_glob.CONFIG_PARAM_NO_TASKS, "4711")
    my_instance.set_config_value(sds_config.sds_glob.CONFIG_PARAM_NO_TASKS, 0)

    my_instance.set_config_value(sds_config.sds_glob.CONFIG_PARAM_VERBOSE, "FaLse")
    my_instance.set_config_value(sds_config.sds_glob.CONFIG_PARAM_VERBOSE, "trUE")
    my_instance.set_config_value(sds_config.sds_glob.CONFIG_PARAM_VERBOSE, True)
