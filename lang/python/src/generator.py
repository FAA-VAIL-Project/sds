# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Generation of a JSON file with given polynomials."""
from __future__ import annotations

from polynomial import sds_glob


# pylint: disable=too-few-public-methods
class Generator:
    """Generation of a JSON file with given polynomials.

    Generation of a JSON file with a given number of randomly generated
    pairs of polynomials and their multiplication result.
    """

    # ------------------------------------------------------------------
    # Initialise the instance.
    # ------------------------------------------------------------------
    def __init__(self, file_name) -> None:
        """Perform the processing.

        Args:
            file_name (str):
                The name of the JSON file to output.
        """
        # pylint: disable=duplicate-code
        sds_glob.logger.debug(sds_glob.LOGGER_START)

        self._file_name = file_name

        self._polynomials = []

        for _ in range(sds_glob.inst_config.no_tasks):
            self._polynomials.append(self._generate_polynom())

        self._create_json_file()

        self._exist = True

        sds_glob.logger.debug(sds_glob.LOGGER_END)

    # ------------------------------------------------------------------
    # Create the JSON file.
    # ------------------------------------------------------------------
    def _create_json_file(self) -> None:
        """Create the JSON file."""

    # ------------------------------------------------------------------
    # Generate the polynom.
    # ------------------------------------------------------------------
    def _generate_polynom(self) -> None:
        """Generate the polynom."""

    # ------------------------------------------------------------------
    # Check the object existence.
    # ------------------------------------------------------------------
    def exists(self) -> bool:
        """Check the object existence.

        Returns:
            bool: Always true.
        """
        sds_glob.logger.debug(sds_glob.LOGGER_START)
        sds_glob.logger.debug(sds_glob.LOGGER_END)

        return self._exist
