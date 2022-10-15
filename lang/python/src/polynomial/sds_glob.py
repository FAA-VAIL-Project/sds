# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Global constants and variables."""
import logging.config

import sds_config

# Configuration parameter.
CONFIG_PARAM_COEFFICIENT_MAX = "coefficient_max"
CONFIG_PARAM_COEFFICIENT_MIN = "coefficient_min"
CONFIG_PARAM_DEGREE_MAX = "degree_max"
CONFIG_PARAM_DEGREE_MIN = "degree_min"
CONFIG_PARAM_NO_TASKS = "no_tasks"
CONFIG_PARAM_VERBOSE = "verbose"

# Error messages.
ERROR_00_901 = (
    "ERROR.00.901 The required instance of the class '{Class}' does not yet exist"
)
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
    "ERROR.00.910 The maximum coefficient {coefficient_max} must be at least "
    + "equal to the minimum coefficient {coefficient_min}"
)

# Default file encoding UTF-8.
FILE_ENCODING_DEFAULT = "utf-8"

# Informational messages.
INFO_00_001 = "INFO.00.001 The logger is configured and ready"
INFO_00_002 = (
    "INFO.00.002 The configuration parameters (polynomial) are checked and loaded"
)
INFO_00_003 = (
    "INFO.00.003 Initialize the configuration parameters using the file '{file}'"
)

INFORMATION_NOT_YET_AVAILABLE = "n/a"

# Logging constants.
LOGGER_END = "End"
LOGGER_NAME = "polynomial"
LOGGER_START = "Start"

POLYNOMIAL_FILE_NAME = "POLYNOMIAL_FILE_NAME"

inst_config: sds_config.Config = sds_config.Config()

# Logger instance.
logger: logging.Logger = logging.getLogger(LOGGER_NAME)
