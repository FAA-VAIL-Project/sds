# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

# pylint: disable=redefined-outer-name
"""Test Configuration and Fixtures.

Setup test configuration and store fixtures.

Returns:
    [type]: None.
"""
import configparser
import os
import pathlib
import shutil

import pytest

from polynomial import sds_config
from polynomial import sds_glob

# Constants & Globals.
# -----------------------------------------------------------------------------
CONFIG_PARSER: configparser.ConfigParser = configparser.ConfigParser()


# -----------------------------------------------------------------------------
# Copy files from the sample test file directory.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def copy_file_4_pytest(file_name: pathlib.Path | str) -> None:
    """Copy file from the sample test file directory.

    Args:
        file_name: pathlib.Path | str): list of files to be copied.
    """
    assert os.path.isdir(
        get_os_independent_name(get_test_files_source_directory_name())
    ), ("source directory '" + get_test_files_source_directory_name() + "' missing")

    source_file = get_full_name_from_components(
        get_test_files_source_directory_name(), file_name
    )
    assert os.path.isfile(source_file), "source file '" + str(source_file) + "' missing"

    target_file = os.environ[sds_glob.POLYNOMIAL_FILE_NAME]

    shutil.copy(source_file, target_file)
    assert os.path.isfile(target_file), (
        "target file '" + str(target_file) + "' is missing"
    )


# -----------------------------------------------------------------------------
# Fixture - Before any test.
# -----------------------------------------------------------------------------
# pylint: disable=protected-access
@pytest.fixture(scope="session", autouse=True)
def fxtr_before_any_test():
    """Fixture Factory: Before any test."""
    os.environ[sds_glob.POLYNOMIAL_FILE_NAME] = "tests/polynom_data.json"

    set_sds_config()


# ------------------------------------------------------------------
# Get the full name of a file from its components.
# ------------------------------------------------------------------
@pytest.helpers.register
def get_full_name_from_components(
    directory_name: pathlib.Path | str,
    stem_name: str = "",
    file_extension: str = "",
) -> str:
    """Get the full name of a file from its components.

    The possible components are directory name, stem name and file extension.

    Args:
        directory_name (pathlib.Path or str): Directory name or directory path.
        stem_name (str, optional): Stem name or file name including file extension.
            Defaults to "".
        file_extension (str, optional): File extension.
            Defaults to "".

    Returns:
        str: Full file name.
    """
    file_name_int = (
        stem_name if file_extension == "" else stem_name + "." + file_extension
    )

    if directory_name == "" and file_name_int == "":
        return ""

    if isinstance(directory_name, pathlib.Path):
        directory_name_int = str(directory_name)
    else:
        directory_name_int = directory_name

    return get_os_independent_name(str(os.path.join(directory_name_int, file_name_int)))


# ------------------------------------------------------------------
# Get the platform-independent name.
# ------------------------------------------------------------------
@pytest.helpers.register
def get_os_independent_name(file_name: pathlib.Path | str) -> str:
    """Get the platform-independent name..

    Args:
        file_name (pathlib.Path | str): File name or file path.

    Returns:
        str: Platform-independent name.
    """
    return file_name.replace(("\\" if os.sep == "/" else "/"), os.sep)


# -----------------------------------------------------------------------------
# Provide the file directory name where the test files are located.
# -----------------------------------------------------------------------------
@pytest.helpers.register
def get_test_files_source_directory_name():
    """Provide test file directory.

    Provide the file directory name where the test files are located.
    """
    return "tests/__PYTEST_FILES__/"


# ------------------------------------------------------------------
# Set the configuration variables.
# ------------------------------------------------------------------
@pytest.helpers.register
def set_sds_config() -> None:
    """Set the configuration variables."""
    sds_glob.inst_config = sds_config.Config()

    sds_glob.inst_config.coef_max = 19
    sds_glob.inst_config.coef_min = -19
    sds_glob.inst_config.degree_max = 5
    sds_glob.inst_config.degree_min = 3
    sds_glob.inst_config.is_verbose = True
    sds_glob.inst_config.no_tasks = 10
