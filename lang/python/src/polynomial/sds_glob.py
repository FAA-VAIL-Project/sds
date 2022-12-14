# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Global constants and variables."""
import logging.config

import sds_config

ARG_ACTION_GENERATE = "generate"
ARG_ACTION_MULTIPLY = "multiply"
ARG_METHOD_FFT = "fft"
ARG_METHOD_NUMPY = "numpy"
ARG_METHOD_SIMPLE = "simple"

# Configuration parameter.
CONFIG_PARAM_COEF_MAX = "coef_max"
CONFIG_PARAM_COEF_MIN = "coef_min"
CONFIG_PARAM_DEGREE_MAX = "degree_max"
CONFIG_PARAM_DEGREE_MIN = "degree_min"
CONFIG_PARAM_NO_TASKS = "no_tasks"
CONFIG_PARAM_VERBOSE = "verbose"

# Error messages.
ERROR_00_902 = "ERROR.00.902 The specified JSON file {file_name} does not exist"
ERROR_00_903 = (
    "ERROR.00.903 Unknown configuration parameter: Key='{key}' Value='{value}"
)
ERROR_00_904 = (
    "ERROR.00.904 The specified configuration file '{file}' is either not a "
    + "file or does not exist at all"
)
ERROR_00_905 = (
    "ERROR.00.905 Illegal configuration parameter value '{value}' - "
    + "only 'false' or 'true' are allowed"
)
ERROR_00_906 = (
    "ERROR.00.906 Illegal configuration parameter value '{value}' - "
    + "only integers are allowed"
)
ERROR_00_907 = "ERROR.00.907 The number of tasks must be at least 1 and not {no_tasks}"
ERROR_00_908 = "ERROR.00.908 The minimum degree must be at least 1 and not {degree_min}"
ERROR_00_909 = (
    "ERROR.00.909 The maximum degree {degree_max} must be at least "
    + "equal to the minimum degree {degree_min}"
)
ERROR_00_910 = (
    "ERROR.00.910 The maximum coef {coef_max} must be at least "
    + "equal to the minimum coef {coef_min}"
)
ERROR_00_911 = (
    "ERROR.00.911 Difference in task no. {task_no} degree {degree} "
    + "got {got} instead of {instead}"
)

# Default file encoding UTF-8.
FILE_ENCODING_DEFAULT = "utf-8"

# Informational messages.
INFO_00_001 = (
    "INFO.00.001 Initialize the configuration parameters using the file '{file}'"
)
INFO_00_002 = (
    "INFO.00.002 The configuration parameters (polynomial) are checked and loaded"
)
INFO_00_003 = "INFO.00.003 Start Launcher"
INFO_00_004 = "INFO.00.004 The logger is configured and ready"
INFO_00_005 = "INFO.00.005 Argument {arg}='{value}'"
INFO_00_006 = "INFO.00.006 End   Launcher"
INFO_00_011 = "INFO.00.011 Start Generator"
INFO_00_012 = "INFO.00.012 End   Generator"
INFO_00_021 = "INFO.00.021 Start Multiplier - Python - {method}"
INFO_00_022 = "INFO.00.022 End   Multiplier - Python - {method}"

INFORMATION_NOT_YET_AVAILABLE = "n/a"

JSON_NAME_COEFFICIENTS = "coefficients"
JSON_NAME_DEGREE = "degree"
JSON_NAME_NO_TASKS = "moTasks"
JSON_NAME_POLYNOM_1 = "polynom1"
JSON_NAME_POLYNOM_2 = "polynom2"
JSON_NAME_PRODUCT = "product"
JSON_NAME_TASK_NO = "taskNo"
JSON_NAME_TASKS = "tasks"

# Logging constants.
LOGGER_END = "End"
LOGGER_NAME = "polynomial"
LOGGER_START = "Start"

POLYNOMIAL_FILE_NAME = "POLYNOMIAL_FILE_NAME"

inst_config: sds_config.Config = sds_config.Config()

# Logger instance.
logger: logging.Logger = logging.getLogger(LOGGER_NAME)
