# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Miscellaneous helper functions."""
import datetime
import logging
import logging.config

import polynomial_error
import sds_glob
import yaml

# ------------------------------------------------------------------
# Global constants.
# ------------------------------------------------------------------
_LOGGER_CFG_FILE = "logging_cfg.yaml"
_LOGGER_FATAL_HEAD = "FATAL ERROR: program abort =====> "
_LOGGER_FATAL_TAIL = " <===== FATAL ERROR"
_LOGGER_PROGRESS_UPDATE = "Progress update "


# ------------------------------------------------------------------
# Check the existence of objects.
# ------------------------------------------------------------------
def check_exists_object(
    is_config: bool = False,
) -> None:
    """Check the existence of objects.

    Args:
        is_config (bool, optional):
            Check an object of class Config.
            Defaults to False.
    """
    sds_glob.logger.debug(sds_glob.LOGGER_START)

    # ERROR.00.901 The required instance of the class '{Class}'
    # does not yet exist
    if is_config:
        try:
            sds_glob.inst_config.exists()  # type: ignore
        except AttributeError:
            terminate_fatal(
                sds_glob.ERROR_00_901.replace("{Class}", "Config"),
            )

    sds_glob.logger.debug(sds_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Initialising the logging functionality.
# -----------------------------------------------------------------------------
def initialise_logger() -> None:
    """Initialise the root logging functionality."""
    with open(
        _LOGGER_CFG_FILE, "r", encoding=sds_glob.FILE_ENCODING_DEFAULT
    ) as file_handle:
        log_config = yaml.safe_load(file_handle.read())

    logging.config.dictConfig(log_config)
    sds_glob.logger.setLevel(logging.DEBUG)

    # The logger is configured and ready.
    progress_msg_core(sds_glob.INFO_00_001)


# ------------------------------------------------------------------
# Create a progress message.
# ------------------------------------------------------------------
def progress_msg(is_verbose: bool, msg: str) -> None:
    """Create a progress message.

    Args:
        is_verbose (bool): If true, processing results are reported.
        msg (str): Progress message.
    """
    if is_verbose:
        progress_msg_core(msg)


# ------------------------------------------------------------------
# Create a progress message.
# ------------------------------------------------------------------
def progress_msg_core(msg: str) -> None:
    """Create a progress message.

    Args:
        msg (str): Progress message.
    """
    final_msg = _LOGGER_PROGRESS_UPDATE + str(datetime.datetime.now()) + " : " + msg

    if msg not in ("", "-" * 80, "=" * 80):
        final_msg = final_msg + "."

    print(final_msg)


# ------------------------------------------------------------------
# Terminate the application immediately.
# ------------------------------------------------------------------
def terminate_fatal(error_msg: str) -> None:
    """Terminate the application immediately.

    Args:
        error_msg (str): Error message.
    """
    print("")
    print(_LOGGER_FATAL_HEAD)
    print(_LOGGER_FATAL_HEAD, error_msg, _LOGGER_FATAL_TAIL, sep="")
    print(_LOGGER_FATAL_HEAD)

    raise polynomial_error.PolynomialError(error_msg)
