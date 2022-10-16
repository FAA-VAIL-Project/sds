# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Performing polynomial multiplication."""
from __future__ import annotations

import os

import sds_glob
import utils


# pylint: disable=too-few-public-methods
class Multiplier:
    """Performing polynomial multiplication."""

    # ------------------------------------------------------------------
    # Initialise the instance.
    # ------------------------------------------------------------------
    def __init__(self, file_name) -> None:
        """Perform the processing.

        Args:
            file_name (str):
                The name of the JSON file to process.
        """
        # pylint: disable=duplicate-code
        sds_glob.logger.debug(sds_glob.LOGGER_START)

        self._file_name = file_name

        if not os.path.isfile(file_name):
            # ERROR.00.902 The specified JSON file {file_name} does not exist
            utils.terminate_fatal(
                sds_glob.ERROR_00_902.replace("{file_name}", file_name)
            )

        self._exist = True

        sds_glob.logger.debug(sds_glob.LOGGER_END)

    # ------------------------------------------------------------------
    # Check the object existence.
    # ------------------------------------------------------------------
    def exists(self) -> bool:
        """Check the object existence.

        Returns:
            bool: Always true.
        """
        return self._exist
