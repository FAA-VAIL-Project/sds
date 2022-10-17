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

    my_instance.set_config_value(sds_config.sds_glob.CONFIG_PARAM_NO_TASKS, "4711")
    my_instance.set_config_value(sds_config.sds_glob.CONFIG_PARAM_NO_TASKS, 1)

    my_instance.set_config_value(sds_config.sds_glob.CONFIG_PARAM_VERBOSE, "FaLse")
    my_instance.set_config_value(sds_config.sds_glob.CONFIG_PARAM_VERBOSE, "trUE")
    my_instance.set_config_value(sds_config.sds_glob.CONFIG_PARAM_VERBOSE, True)

    my_instance.set_is_verbose(True)


# -----------------------------------------------------------------------------
# Test case: __init__(setup_ok.cfg) - File setup.cfg.
# -----------------------------------------------------------------------------
def test_setup_1():
    """Test case: Test case: __init__(setup_ok.cfg) - File setup.cfg."""
    sds_config.Config(
        pytest.helpers.get_full_name_from_components(
            pytest.helpers.get_test_files_source_directory_name(), "setup_ok.cfg"
        )
    )
