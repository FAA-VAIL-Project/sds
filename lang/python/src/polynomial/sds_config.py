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
    terminated with a Runtime exception.

    Typical usage example:

        from polynomial import sds_config

        my_instance = sds_config.Config(config_file="my_config.txt")
        my_instance.set_config_value("no_tasks", 10)
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
        sds_glob.logger.debug(sds_glob.LOGGER_START)

        # ------------------------------------------------------------------
        # Initialize configuration parameters.
        # ------------------------------------------------------------------
        self.degree_min = 3
        self.degree_max = 10
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

        # INFO.00.002 The configuration parameters (polynomial) are checked and loaded
        utils.progress_msg_core(sds_glob.INFO_00_002)

        self.exist = True

        sds_glob.logger.debug(sds_glob.LOGGER_END)

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
        sds_glob.logger.debug(sds_glob.LOGGER_START)

        key_int = key.lower()

        if key_int in sds_glob.CONFIG_PARAM_DEGREE_MAX:
            self.degree_min = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_DEGREE_MIN:
            self.degree_max = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_NO_TASKS:
            self.no_tasks = self._check_config_value_int(value)
            return

        # ERROR.00.903 Unknown configuration parameter: Key='{key}' Value='{value}
        utils.terminate_fatal(
            sds_glob.ERROR_00_903.replace("{key}", key).replace("{value}", str(value))
        )

        sds_glob.logger.debug(sds_glob.LOGGER_END)

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
        sds_glob.logger.debug(sds_glob.LOGGER_START)

        if isinstance(value, bool):
            return value

        if value.lower() == "false":
            return False

        if value.lower() != "true":
            # ERROR.00.905 Illegal configuration parameter value '{value}' -
            # only 'false' or 'true' are allowed
            utils.terminate_fatal(sds_glob.ERROR_00_905.replace("{value}", value))

        sds_glob.logger.debug(sds_glob.LOGGER_END)

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
        sds_glob.logger.debug(sds_glob.LOGGER_START)

        if isinstance(value, str):
            try:
                return int(value)
            except ValueError:
                # ERROR.00.906 Illegal configuration parameter value '{value}' -
                # only integers are allowed
                utils.terminate_fatal(sds_glob.ERROR_00_906.replace("{value}", value))

        sds_glob.logger.debug(sds_glob.LOGGER_END)

        return value

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
        sds_glob.logger.debug(sds_glob.LOGGER_START)

        # INFO.00.003 Initialize the configuration parameters using the file {file}
        utils.progress_msg_core(sds_glob.INFO_00_003.replace("{file}", config_file))

        config_parser = configparser.ConfigParser()
        config_parser.read(config_file)

        for section in config_parser.sections():
            if section in (Config._CONFIG_SECTION,):
                for (key, value) in config_parser.items(section):
                    self._check_config_param(key, value)

        sds_glob.logger.debug(sds_glob.LOGGER_END)

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
        sds_glob.logger.debug(sds_glob.LOGGER_START)
        sds_glob.logger.debug(sds_glob.LOGGER_END)

        self._check_config_param(key, value)
