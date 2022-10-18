# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Class for generating a JSON file with tasks."""
from __future__ import annotations

import json
import random
import time
from typing import Tuple

import numpy
import sds_glob  # type: ignore
import utils  # type: ignore
from numpy.polynomial import Polynomial


# pylint: disable=too-few-public-methods
class Generator:
    """Class for generating a JSON file with tasks."""

    # ------------------------------------------------------------------
    # Initialise the instance.
    # ------------------------------------------------------------------
    def __init__(self, file_name) -> None:
        """Generate the tasks.

        Using configuration parameters in the 'setup.cfg' file, a JSON file
        containing polynomial pairs and their product as tasks can be
        generated with an instance of this class.

        Args:
            file_name (str):
                The name of the JSON file to output.
        """
        # pylint: disable=duplicate-code
        sds_glob.logger.debug(sds_glob.LOGGER_START)

        # Provide progress messages.
        utils.progress_msg("-" * 79)
        # INFO.00.011 Start Generator
        utils.progress_msg(sds_glob.INFO_00_011)
        utils.progress_msg("-" * 79)

        self._file_name = file_name

        # Create polynomial pairs with random values and calculate
        # the product. Each generated triple defines a task for the
        # 'Multiplier' class.
        self._tasks = []

        for no_task in range(sds_glob.inst_config.get_no_tasks()):
            self._tasks.append(self._generate_polynom(no_task))

        # Write the generated polynomials along with their product
        # to a JSON file for use in the 'Multiplier' class.
        self._create_json_file()

        # Provide progress messages.
        utils.progress_msg("-" * 79)
        # INFO.00.012 End   Generator
        utils.progress_msg(sds_glob.INFO_00_012)
        utils.progress_msg("-" * 79)

        sds_glob.logger.debug(sds_glob.LOGGER_END)

    # ------------------------------------------------------------------
    # Create the JSON file.
    # ------------------------------------------------------------------
    def _create_json_file(self) -> None:
        """Create the JSON file.

        The file structure looks as follows:

            {
                "moTasks": 999,
                "tasks": [
                    {
                        "taskNo": 999,
                        "polynom1": {
                            "degree": 999,
                            "coefficients": [
                                999,
                                ...
                            ]
                        },
                        "polynom2": {
                            "degree": 999,
                            "coefficients": [
                                999,
                                ...
                            ]
                        },
                        "product": {
                            "degree": 999,
                            "coefficients": [
                                999,
                                ...
                            ]
                        }
                    },
                    ...
                ]
            }
        """
        tasks = []
        for task_no, (polynom_1, polynom_2, product) in enumerate(self._tasks):
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
                    sds_glob.JSON_NAME_NO_TASKS: sds_glob.inst_config.get_no_tasks(),
                    sds_glob.JSON_NAME_TASKS: tasks,
                },
                file_handle,
                indent=4,
                sort_keys=False,
            )

    # ------------------------------------------------------------------
    # Generation a task consisting of a polynomial pair and
    # their product.
    # ------------------------------------------------------------------
    @staticmethod
    def _generate_task(no_task: int) -> Tuple[Polynomial, Polynomial, Polynomial]:
        """Generation a task consisting of a polynomial pair and their product.

        The degree of the polynomials and the coefficients are
        determined in a given range as random integers

        Args:
            no_task (int): The task number

        Returns:
            Tuple[Polynomial, Polynomial, Polynomial]:
                Polynomial 1, Polynomial 2 and Polynomial 1 * Polynomial 2.
        """
        # Start time measurement.
        start_time = time.time_ns()

        # Creation of the first polynomial.
        polynom_1 = Polynomial(
            numpy.random.randint(
                sds_glob.inst_config.get_coef_min(),
                sds_glob.inst_config.get_coef_max(),
                random.randint(  # nosec
                    sds_glob.inst_config.get_degree_min(),
                    sds_glob.inst_config.get_degree_max(),
                ),
            )
        )

        # Creation of the second polynomial.
        polynom_2 = Polynomial(
            numpy.random.randint(
                sds_glob.inst_config.get_coef_min(),
                sds_glob.inst_config.get_coef_max(),
                random.randint(  # nosec
                    sds_glob.inst_config.get_degree_min(),
                    sds_glob.inst_config.get_degree_max(),
                ),
            )
        )

        # Calculation of the product.
        product = polynom_1 * polynom_2

        # Stop time measurement and store the results.
        utils.progress_msg_time_elapsed(
            time.time_ns() - start_time,
            f"task no. {no_task + 1:2d} (degrees: {polynom_1.degree():5d} - "
            + f"{polynom_2.degree():5d} - {product.degree():5d}) generated",
        )

        return polynom_1, polynom_2, product
