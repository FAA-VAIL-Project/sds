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

from polynomial import generator
from polynomial import multiplier
from polynomial import sds_glob
from polynomial import utils

# -----------------------------------------------------------------------------
# Global variables.
# -----------------------------------------------------------------------------
_ARG_ACTION = "action"
_ARG_ACTION_GENERATE = "generate"
_ARG_ACTION_MULTIPLY = "multiply"

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

    parsed_args = parser.parse_args()

    args[_ARG_ACTION] = parsed_args.action

    if not (args[_ARG_ACTION].lower() in [_ARG_ACTION_GENERATE, _ARG_ACTION_MULTIPLY]):
        utils.terminate_fatal(
            "The specified action is neither '"
            + _ARG_ACTION_GENERATE
            + "' nor '"
            + _ARG_ACTION_MULTIPLY
            + f"': {args[_ARG_ACTION]}",
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

    utils.initialise_logger()

    sds_glob.logger.debug(sds_glob.LOGGER_START)
    sds_glob.logger.debug("param argv=%s", argv)

    sds_glob.logger.info("Start launcher.py")

    print("Start launcher.py")

    locale.setlocale(locale.LC_ALL, _LOCALE)

    # Load the command line arguments.
    args = _get_args()

    file_name = os.getenv(sds_glob.POLYNOMIAL_FILE_NAME)

    if args[_ARG_ACTION].lower() == _ARG_ACTION_GENERATE:
        generator.Generator(file_name)
    elif args[_ARG_ACTION].lower() == _ARG_ACTION_MULTIPLY:
        multiplier.Multiplier(file_name)

    sds_glob.logger.info("End   launcher.py")

    duration = time.time_ns() - start_time

    print(f"{f'{duration:,}':>20} ns - Total time launcher")

    sds_glob.logger.debug(sds_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Program start.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # not testable
    main(sys.argv)
