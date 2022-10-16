# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Generation of a JSON file with given polynomials."""
from __future__ import annotations

import json
import random
import time

import numpy
import sds_glob
import utils
from numpy.polynomial import Polynomial


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

        utils.progress_msg(
            "-"*79
        )
        # INFO.00.011 Start Generator
        utils.progress_msg(
            sds_glob.INFO_00_011
        )
        utils.progress_msg(
            "-"*79
        )

        self._file_name = file_name

        self._polynomials = []

        for no_task in range(sds_glob.inst_config.no_tasks):
            self._polynomials.append(self._generate_polynom(no_task))

        self._create_json_file()

        self._exist = True

        utils.progress_msg(
            "-"*79
        )
        # INFO.00.012 End   Generator
        utils.progress_msg(
            sds_glob.INFO_00_012
        )
        utils.progress_msg(
            "-"*79
        )
        sds_glob.logger.debug(sds_glob.LOGGER_END)

    # ------------------------------------------------------------------
    # Create the JSON file.
    # ------------------------------------------------------------------
    def _create_json_file(self) -> None:
        """Create the JSON file."""

        tasks = []
        for task_no, (polynom_1, polynom_2, product) in enumerate(self._polynomials):
            tasks.append(
                {
                    sds_glob.JSON_NAME_TASK_NO: task_no + 1,
                    sds_glob.JSON_NAME_POLYNOM_1: {
                        sds_glob.JSON_NAME_DEGREE: polynom_1.degree(),
                        sds_glob.JSON_NAME_COEFFICIENTS: list(
                            int(x) for x in polynom_1.coef
                        ),
                    },
                    sds_glob.JSON_NAME_POLYNOM_2: {
                        sds_glob.JSON_NAME_DEGREE: polynom_2.degree(),
                        sds_glob.JSON_NAME_COEFFICIENTS: list(
                            int(x) for x in polynom_2.coef
                        ),
                    },
                    sds_glob.JSON_NAME_PRODUCT: {
                        sds_glob.JSON_NAME_DEGREE: product.degree(),
                        sds_glob.JSON_NAME_COEFFICIENTS: list(
                            int(x) for x in product.coef
                        ),
                    },
                }
            )

        with open(
            self._file_name, "w", encoding=sds_glob.FILE_ENCODING_DEFAULT
        ) as file_handle:
            json.dump(
                {
                    sds_glob.JSON_NAME_NO_TASKS: sds_glob.inst_config.no_tasks,
                    sds_glob.JSON_NAME_TASKS: tasks,
                },
                file_handle,
                indent=4,
                sort_keys=False,
            )

    # ------------------------------------------------------------------
    # Generate the polynom.
    # ------------------------------------------------------------------
    @staticmethod
    def _generate_polynom(no_task: int) -> (Polynomial, Polynomial, Polynomial):
        """Generate the polynom."""
        start_time = time.time_ns()

        polynom_1 = Polynomial(
            numpy.random.randint(
                sds_glob.inst_config.coef_min,
                sds_glob.inst_config.coef_max,
                random.randint(  # nosec
                    sds_glob.inst_config.degree_min, sds_glob.inst_config.degree_max
                ),
            )
        )

        polynom_2 = Polynomial(
            numpy.random.randint(
                sds_glob.inst_config.coef_min,
                sds_glob.inst_config.coef_max,
                random.randint(  # nosec
                    sds_glob.inst_config.degree_min, sds_glob.inst_config.degree_max
                ),
            )
        )

        product = polynom_1 * polynom_2

        utils.progress_msg_time_elapsed(
            time.time_ns() - start_time,
            f"polynom no. {no_task + 1:2d} (degrees: {polynom_1.degree():5d} - "
            + f"{polynom_2.degree():5d} - {product.degree():5d}) generated",
        )

        return polynom_1, polynom_2, product

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
