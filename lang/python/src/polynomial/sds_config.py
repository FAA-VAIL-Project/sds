# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Managing the application configuration parameters."""
from __future__ import annotations

import configparser
import os

import sds_glob
import utils


# pylint: disable=too-few-public-methods
class Config:
    """Managing the application configuration parameters.

    Configuration parameters are managed with class `Config`.

    With the instantiation of the object first the agreed
    default values are assigned to the configuration parameters.

    Subsequently, a configuration file optionally specified with
    the instantiation call is read. If no configuration file
    was specified, then an optionally existing `setup.cfg` is
    used as configuration file. The configuration file must be
    in `Disutils` format in any case. Example:

        [polynomial]
        no_tasks = 10

    In case of an error, the instantiation of the Config class is
    terminated with a PolynomialError exception.
    """

    # ------------------------------------------------------------------
    # Global constants.
    # ------------------------------------------------------------------
    _CONFIG_FILE = "setup.cfg"
    _CONFIG_SECTION = "polynomial"

    # ------------------------------------------------------------------
    # Initialise the instance.
    # ------------------------------------------------------------------
    def __init__(self, config_file=_CONFIG_FILE) -> None:
        """Initialise the instance.

        Args:
            config_file (str, optional):
                The name of the configuration file. Defaults to '"setup.cfg'.
        """
        # pylint: disable=duplicate-code

        # ------------------------------------------------------------------
        # Initialize configuration parameters.
        # ------------------------------------------------------------------
        self.coef_max = 9999
        self.coef_min = -9999
        self.degree_max = 15500
        self.degree_min = 14500
        self.is_verbose = True
        self.no_tasks = 10

        # ------------------------------------------------------------------
        # Update optionally the configuration parameters from a
        # configuration file.
        # ------------------------------------------------------------------

        # ERROR.00.904 The specified configuration file '{file}' is either not
        # a file or does not exist at all.
        if config_file != Config._CONFIG_FILE and not os.path.isfile(config_file):
            utils.terminate_fatal(sds_glob.ERROR_00_904.replace("{file}", config_file))

        if os.path.isfile(config_file):
            self.load_config_file(config_file)

        self._check_config_params()

        # INFO.00.002 The configuration parameters (polynomial) are checked and loaded
        utils.progress_msg_core(sds_glob.INFO_00_002)

        self.exist = True

    # ------------------------------------------------------------------
    # Check the configuration parameters.
    # ------------------------------------------------------------------
    def _check_config_param(self, key: str, value: bool | int | str) -> None:
        """Check the configuration parameters.

        Args:
            key (str):
                The name of the configuration parameter.
            value (bool | int | str):
                The given value of the configuration parameter.
        """
        key_int = key.lower()

        if key_int in sds_glob.CONFIG_PARAM_COEF_MAX:
            self.coef_max = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_COEF_MIN:
            self.coef_min = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_DEGREE_MAX:
            self.degree_max = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_DEGREE_MIN:
            self.degree_min = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_NO_TASKS:
            self.no_tasks = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_VERBOSE:
            self.is_verbose = self._check_config_value_bool(value)
            return

        # ERROR.00.903 Unknown configuration parameter: Key='{key}' Value='{value}
        utils.terminate_fatal(
            sds_glob.ERROR_00_903.replace("{key}", key).replace("{value}", str(value))
        )

    # ------------------------------------------------------------------
    # Check the configuration parameters.
    # ------------------------------------------------------------------
    def _check_config_params(self) -> None:
        """Check the configuration parameters."""
        # ERROR.00.907 The number of tasks must be at least 1 and not {no_tasks}
        if self.no_tasks < 1:
            utils.terminate_fatal(
                sds_glob.ERROR_00_907.replace("{no_tasks}", str(self.no_tasks))
            )

        # ERROR.00.908 The minimum degree must be at least 1 and not {degree_min}
        if self.degree_min < 1:
            utils.terminate_fatal(
                sds_glob.ERROR_00_908.replace("{degree_min}", str(self.degree_min))
            )

        # ERROR.00.909 The maximum degree {degree_max} must be at least
        # equal to the minimum degree {degree_min}
        if self.degree_max < self.degree_min:
            utils.terminate_fatal(
                sds_glob.ERROR_00_909.replace(
                    "{degree_max}",
                    str(self.degree_max).replace("{degree_min}", str(self.degree_min)),
                )
            )

        # ERROR.00.910 The maximum coef {coef_max} must be at least
        # equal to the minimum coef {coef_min}
        if self.coef_max < self.coef_min:
            utils.terminate_fatal(
                sds_glob.ERROR_00_910.replace(
                    "{coef_max}",
                    str(self.coef_max).replace("{coef_min}", str(self.coef_min)),
                )
            )

    # ------------------------------------------------------------------
    # Check a boolean configuration parameter value.
    # ------------------------------------------------------------------
    @staticmethod
    def _check_config_value_bool(
        value: bool | str,
    ) -> bool:
        """Check a boolean configuration parameter value.

        Args:
            value (bool|str):
                The configuration parameter value to be checked.

        Returns:
            bool:
                The boolean configuration parameter value.
        """
        if isinstance(value, bool):
            return value

        if value.lower() == "false":
            return False

        if value.lower() != "true":
            # ERROR.00.905 Illegal configuration parameter value '{value}' -
            # only 'false' or 'true' are allowed
            utils.terminate_fatal(sds_glob.ERROR_00_905.replace("{value}", value))

        return True

    # ------------------------------------------------------------------
    # Check an integer configuration parameter value.
    # ------------------------------------------------------------------
    @staticmethod
    def _check_config_value_int(
        value: int | str,
    ) -> int:
        """Check an integer configuration parameter value.

        Args:
            value (int|str):
                The configuration parameter value to be checked.

        Returns:
            int:
                The integer configuration parameter value.
        """
        if isinstance(value, str):
            try:
                return int(value)
            except ValueError:
                # ERROR.00.906 Illegal configuration parameter value '{value}' -
                # only integers are allowed
                utils.terminate_fatal(sds_glob.ERROR_00_906.replace("{value}", value))

        return value

    # ------------------------------------------------------------------
    # Check the object existence.
    # ------------------------------------------------------------------
    def exists(self) -> bool:
        """Check the object existence.

        Returns:
            bool: Always true.
        """
        return self.exist

    # ------------------------------------------------------------------
    # Load and check the configuration parameters from a
    # configuration file.
    # ------------------------------------------------------------------
    def load_config_file(self, config_file: str) -> None:
        """Load and check the configuration parameters from a configuration
        file.

        Args:
            config_file (str):
                Configuration file name.
        """
        # INFO.00.003 Initialize the configuration parameters using the file {file}
        utils.progress_msg_core(sds_glob.INFO_00_001.replace("{file}", config_file))

        config_parser = configparser.ConfigParser()
        config_parser.read(config_file)

        for section in config_parser.sections():
            if section in (Config._CONFIG_SECTION,):
                for (key, value) in config_parser.items(section):
                    self._check_config_param(key, value)

    # ------------------------------------------------------------------
    # Modify the value of an existing configuration parameter.
    # ------------------------------------------------------------------
    def set_config_value(self, key: str, value: bool | int | str) -> None:
        """Modify the value of an existing configuration parameter.

        Args:
            key (str):
                The name of the configuration parameter.
            value (bool | int | str):
                The new value of the configuration parameter.
        """
        self._check_config_param(key, value)
