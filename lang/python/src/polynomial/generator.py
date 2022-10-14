# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Generation of a JSON file with given polynomials."""
from __future__ import annotations

import sds_config
import sds_glob
import utils


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

        sds_glob.inst_config = sds_config.Config()

        self._check_config_params()

        self._polynomials = []

        for _ in range(sds_glob.inst_config.no_tasks):
            self._polynomials.append(self._generate_polynom())

        self._create_json_file()

        self._exist = True

        sds_glob.logger.debug(sds_glob.LOGGER_END)

    # ------------------------------------------------------------------
    # Check the configuration parameters.
    # ------------------------------------------------------------------
    @staticmethod
    def _check_config_params() -> None:
        """Check the configuration parameters."""
        # ERROR.00.907 The number of tasks must be at least 1 and not {no_tasks}
        if sds_glob.inst_config.no_tasks < 1:
            utils.terminate_fatal(
                sds_glob.ERROR_00_907.replace(
                    "{no_tasks}", str(sds_glob.inst_config.no_tasks)
                )
            )

        # ERROR.00.908 The minimum degree must be at least 1 and not {degree_min}
        if sds_glob.inst_config.degree_min < 1:
            utils.terminate_fatal(
                sds_glob.ERROR_00_908.replace(
                    "{degree_min}", str(sds_glob.inst_config.degree_min)
                )
            )

        #
        if sds_glob.inst_config.degree_max < sds_glob.inst_config.degree_min:
            utils.terminate_fatal(
                sds_glob.ERROR_00_909.replace(
                    "{degree_max}",
                    str(sds_glob.inst_config.degree_max).replace(
                        "{degree_min}", str(sds_glob.inst_config.degree_min)
                    ),
                )
            )

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
        return self._exist
