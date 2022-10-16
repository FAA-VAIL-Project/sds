# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Module polynomial: Entry Point Functionality.

This is the entry point to the application POLYNOMIAL.
"""
from __future__ import annotations

import argparse
import locale
import os
import sys
import time

import generator
import multiplier
import sds_glob
import utils

# -----------------------------------------------------------------------------
# Global variables.
# -----------------------------------------------------------------------------
_ARG_ACTION = "action"
_ARG_ACTION_GENERATE = "generate"
_ARG_ACTION_MULTIPLY = "multiply"
_ARG_METHOD = "method"
_ARG_METHOD_FFT = "fft"
_ARG_METHOD_NUMPY = "numpy"
_ARG_METHOD_SIMPLE = "simple"

_LOCALE = "en_US.UTF-8"


# -----------------------------------------------------------------------------
# Load the command line arguments into memory.
# -----------------------------------------------------------------------------
def _get_args() -> dict[str, str | list[str]]:
    """Load the command line arguments.

    Returns:
        dict[str, bool]: The command line arguments.
    """
    sds_glob.logger.debug(sds_glob.LOGGER_START)

    args: dict[str, str] = {}

    parser = argparse.ArgumentParser(
        description="Perform a polynomial process",
        prog="launcher",
        prefix_chars="--",
        usage="%(prog)s options",
    )

    parser.add_argument(
        "-a",
        "--action",
        help="the action to process: '"
        + _ARG_ACTION_GENERATE
        + "' or '"
        + _ARG_ACTION_MULTIPLY
        + "'",
        metavar="ACTION",
        type=str,
    )

    parser.add_argument(
        "-m",
        "--method",
        default=_ARG_METHOD_FFT,
        help="the method to apply: '"
        + _ARG_METHOD_FFT
        + "' or '"
        + _ARG_METHOD_NUMPY
        + "' or '"
        + _ARG_METHOD_SIMPLE
        + "'",
        metavar="METHOD",
        type=str,
    )

    parsed_args = parser.parse_args()

    args[_ARG_ACTION] = parsed_args.action.lower()

    if not (args[_ARG_ACTION] in [_ARG_ACTION_GENERATE, _ARG_ACTION_MULTIPLY]):
        utils.terminate_fatal(
            "The specified action is neither '"
            + _ARG_ACTION_GENERATE
            + "' nor '"
            + _ARG_ACTION_MULTIPLY
            + f"': {args[_ARG_ACTION]}",
        )

    args[_ARG_METHOD] = parsed_args.method.lower()

    if not (args[_ARG_METHOD] in [_ARG_METHOD_FFT, _ARG_METHOD_NUMPY, _ARG_METHOD_SIMPLE]):
        utils.terminate_fatal(
            "The specified method is neither '"
            + _ARG_METHOD_FFT
            + "', '"
            + _ARG_METHOD_NUMPY
            + "' nor '"
            + _ARG_METHOD_SIMPLE
            + f"': {args[_ARG_METHOD]}",
        )

    # INFO.00.006 Argument {arg}='{value}'
    utils.progress_msg(
        sds_glob.INFO_00_005.replace("{arg}",_ARG_ACTION).replace("{value}",args[_ARG_ACTION])
    )
    utils.progress_msg(
        sds_glob.INFO_00_005.replace("{arg}",_ARG_METHOD).replace("{value}",args[_ARG_METHOD])
    )

    sds_glob.logger.debug(sds_glob.LOGGER_END)

    return args


# -----------------------------------------------------------------------------
# Initialising the logging functionality.
# -----------------------------------------------------------------------------
def main(argv: list[str]) -> None:
    """Entry point.

    The processes to be carried out are selected via command line arguments.

    Args:
        argv (list[str]): Command line arguments.
    """
    # Initialise the logging functionality.
    start_time = time.time_ns()

    utils.progress_msg(
        "=" * 79
    )
    # INFO.00.004 Start Launcher
    utils.progress_msg(
        sds_glob.INFO_00_003
    )

    utils.initialise_logger()

    sds_glob.logger.debug(sds_glob.LOGGER_START)
    sds_glob.logger.debug("param argv=%s", argv)

    locale.setlocale(locale.LC_ALL, _LOCALE)

    # Load the command line arguments.
    args = _get_args()

    file_name = os.getenv(sds_glob.POLYNOMIAL_FILE_NAME)

    if args[_ARG_ACTION].lower() == _ARG_ACTION_GENERATE:
        generator.Generator(file_name)
    elif args[_ARG_ACTION].lower() == _ARG_ACTION_MULTIPLY:
        multiplier.Multiplier(file_name)

    utils.progress_msg_time_elapsed(
        time.time_ns() - start_time,
        "launcher",
    )
    utils.progress_msg(
        "-" * 79
    )
    # INFO.00.005 End   Launcher
    utils.progress_msg(
        sds_glob.INFO_00_006
    )
    utils.progress_msg(
        "=" * 79
    )

    sds_glob.logger.debug(sds_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Program start.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # not testable
    main(sys.argv)
