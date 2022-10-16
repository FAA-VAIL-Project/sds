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
_ARG_METHOD = "method"

_LOCALE = "en_US.UTF-8"


# -----------------------------------------------------------------------------
# Load the command line arguments into the memory.
# -----------------------------------------------------------------------------
def _get_args() -> dict[str, str]:
    """Load the command line arguments into the memory.

    The two possible command line arguments are 'action' and 'method'.

    'action' is mandatory and determines with the values 'generate'
    and 'multiply' the action to be executed. With 'generate' a JSON
    file with a given number of polynomial pairs and their product
    is generated.  With 'multiply', the polynomial pairs present in
    the JSON file are multiplied and the result is checked against
    the sample solution present in the JSON file.

    'method' is optional and defines the method to be used for the
    polynomial multiplication. 'fft' is the default value at which
    a Fast Fourier Transform is performed. For 'numpy' the polynomial
    module of NumPy is used for the calculation of the product. With
    'simple' all terms of the two polynomials are simply multiplied
    and the like terms are added up.

    Returns:
        dict[str, str]: The command line arguments.
    """
    sds_glob.logger.debug(sds_glob.LOGGER_START)

    args: dict[str, str] = {}

    parser = argparse.ArgumentParser(
        description="Perform a polynomial process",
        prog="launcher",
        prefix_chars="--",
        usage="%(prog)s options",
    )

    # -------------------------------------------------------------------------
    # Definition of the command line arguments.
    # ------------------------------------------------------------------------
    parser.add_argument(
        "-a",
        "--action",
        help="the action to process: '"
        + sds_glob.ARG_ACTION_GENERATE
        + "' (a JSON file with polynomials) or '"
        + sds_glob.ARG_ACTION_MULTIPLY
        + "' (the polynomials from a JSON file)",
        metavar="ACTION",
        type=str,
    )

    parser.add_argument(
        "-m",
        "--method",
        default=sds_glob.ARG_METHOD_FFT,
        help="the method to apply: '"
        + sds_glob.ARG_METHOD_FFT
        + "' (Fast Fourier Transform) or '"
        + sds_glob.ARG_METHOD_NUMPY
        + "' (NumPy Polynomials) or '"
        + sds_glob.ARG_METHOD_SIMPLE
        + "' (simple multiplication)",
        metavar="METHOD",
        type=str,
    )

    # -------------------------------------------------------------------------
    # Load and check the command line arguments.
    # -------------------------------------------------------------------------
    parsed_args = parser.parse_args()

    args[_ARG_ACTION] = parsed_args.action.lower()

    if not (
        args[_ARG_ACTION]
        in [sds_glob.ARG_ACTION_GENERATE, sds_glob.ARG_ACTION_MULTIPLY]
    ):
        utils.terminate_fatal(
            "The specified action is neither '"
            + sds_glob.ARG_ACTION_GENERATE
            + "' nor '"
            + sds_glob.ARG_ACTION_MULTIPLY
            + f"': {args[_ARG_ACTION]}",
        )

    args[_ARG_METHOD] = parsed_args.method.lower()

    if not (
        args[_ARG_METHOD]
        in [
            sds_glob.ARG_METHOD_FFT,
            sds_glob.ARG_METHOD_NUMPY,
            sds_glob.ARG_METHOD_SIMPLE,
        ]
    ):
        utils.terminate_fatal(
            "The specified method is neither '"
            + sds_glob.ARG_METHOD_FFT
            + "', '"
            + sds_glob.ARG_METHOD_NUMPY
            + "' nor '"
            + sds_glob.ARG_METHOD_SIMPLE
            + f"': {args[_ARG_METHOD]}",
        )

    # --------------------------------------------------------------------------
    # Display the command line arguments.
    # --------------------------------------------------------------------------
    # INFO.00.006 Argument {arg}='{value}'
    utils.progress_msg(
        sds_glob.INFO_00_005.replace("{arg}", _ARG_ACTION).replace(
            "{value}", args[_ARG_ACTION]
        )
    )
    utils.progress_msg(
        sds_glob.INFO_00_005.replace("{arg}", _ARG_METHOD).replace(
            "{value}", args[_ARG_METHOD]
        )
    )

    sds_glob.logger.debug(sds_glob.LOGGER_END)

    return args


# -----------------------------------------------------------------------------
# Initialising the logging functionality.
# -----------------------------------------------------------------------------
def main(argv: list[str]) -> None:
    """Entry point.

    The actions to be carried out are selected via command line arguments.

    Args:
        argv (list[str]): Command line arguments.
    """
    # Start time measurement.
    start_time = time.time_ns()

    # Provide progress messages.
    utils.progress_msg("=" * 79)
    # INFO.00.004 Start Launcher.
    utils.progress_msg(sds_glob.INFO_00_003)

    # Initialise the logging functionality..
    utils.initialise_logger()

    sds_glob.logger.debug(sds_glob.LOGGER_START)
    sds_glob.logger.debug("param argv=%s", argv)

    locale.setlocale(locale.LC_ALL, _LOCALE)

    # Load the command line arguments.
    args = _get_args()

    # Take JSON file name from environment variable
    file_name = os.getenv(sds_glob.POLYNOMIAL_FILE_NAME)

    # Perform the processing
    if args[_ARG_ACTION] == sds_glob.ARG_ACTION_GENERATE:
        generator.Generator(file_name)
    elif args[_ARG_ACTION] == sds_glob.ARG_ACTION_MULTIPLY:
        multiplier.Multiplier(file_name, args[_ARG_METHOD])

    # Stop time measurement.
    utils.progress_msg_time_elapsed(
        time.time_ns() - start_time,
        "launcher",
    )

    # Provide progress messages.
    utils.progress_msg("-" * 79)
    # INFO.00.005 End   Launcher
    utils.progress_msg(sds_glob.INFO_00_006)
    utils.progress_msg("=" * 79)

    sds_glob.logger.debug(sds_glob.LOGGER_END)


# -----------------------------------------------------------------------------
# Program start.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # not testable
    main(sys.argv)
