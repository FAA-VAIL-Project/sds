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
    """Managing the application configuration parameters."""

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

        Args:
            config_file (str, optional):
                The name of the configuration file. Defaults to '"setup.cfg'.
        """
        # pylint: disable=duplicate-code

        # ------------------------------------------------------------------
        # Initialize configuration parameters.
        # ------------------------------------------------------------------
        self._coef_max = 9999
        self._coef_min = -9999
        self._degree_max = 5200
        self._degree_min = 4800
        self._is_verbose = True
        self._no_tasks = 10

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

        self._check_all_config_params()

        # INFO.00.002 The configuration parameters (polynomial) are checked and loaded
        utils.progress_msg_core(sds_glob.INFO_00_002)

    # ------------------------------------------------------------------
    # Check all configuration parameters.
    # ------------------------------------------------------------------
    def _check_all_config_params(self) -> None:
        """Check all configuration parameters."""
        # ERROR.00.907 The number of tasks must be at least 1 and not {no_tasks}
        if self._no_tasks < 1:
            utils.terminate_fatal(
                sds_glob.ERROR_00_907.replace("{no_tasks}", str(self._no_tasks))
            )

        # ERROR.00.908 The minimum degree must be at least 1 and not {degree_min}
        if self._degree_min < 1:
            utils.terminate_fatal(
                sds_glob.ERROR_00_908.replace("{degree_min}", str(self._degree_min))
            )

        # ERROR.00.909 The maximum degree {degree_max} must be at least
        # equal to the minimum degree {degree_min}
        if self._degree_max < self._degree_min:
            utils.terminate_fatal(
                sds_glob.ERROR_00_909.replace(
                    "{degree_max}",
                    str(self._degree_max).replace(
                        "{degree_min}", str(self._degree_min)
                    ),
                )
            )

        # ERROR.00.910 The maximum coef {coef_max} must be at least
        # equal to the minimum coef {coef_min}
        if self._coef_max < self._coef_min:
            utils.terminate_fatal(
                sds_glob.ERROR_00_910.replace(
                    "{coef_max}",
                    str(self._coef_max).replace("{coef_min}", str(self._coef_min)),
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
    # Check a single configuration parameter.
    # ------------------------------------------------------------------
    def _check_single_config_param(self, key: str, value: bool | int | str) -> None:
        """Check a single configuration parameter.

        Args:
            key (str):
                The name of the configuration parameter.
            value (bool | int | str):
                The given value of the configuration parameter.
        """
        key_int = key.lower()

        if key_int in sds_glob.CONFIG_PARAM_COEF_MAX:
            self._coef_max = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_COEF_MIN:
            self._coef_min = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_DEGREE_MAX:
            self._degree_max = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_DEGREE_MIN:
            self._degree_min = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_NO_TASKS:
            self._no_tasks = self._check_config_value_int(value)
            return
        if key_int in sds_glob.CONFIG_PARAM_VERBOSE:
            self._is_verbose = self._check_config_value_bool(value)
            return

        # ERROR.00.903 Unknown configuration parameter: Key='{key}' Value='{value}
        utils.terminate_fatal(
            sds_glob.ERROR_00_903.replace("{key}", key).replace("{value}", str(value))
        )

    # ------------------------------------------------------------------
    # Getter method: _coef_max.
    # ------------------------------------------------------------------
    def get_coef_max(self) -> int:
        """Getter method: _coef_max.

        Returns:
            int: The upper limit for the random generation of the coefficients.
        """
        return self._coef_max

    # ------------------------------------------------------------------
    # Getter method: _coef_min.
    # ------------------------------------------------------------------
    def get_coef_min(self) -> int:
        """Getter method: _coef_min.

        Returns:
            int: The lower limit for the random generation of the coefficients.
        """
        return self._coef_min

    # ------------------------------------------------------------------
    # Getter method: _degree_max.
    # ------------------------------------------------------------------
    def get_degree_max(self) -> int:
        """Getter method: _degree_min.

        Returns:
            int: The upper limit for the random generation of the degrees.
        """
        return self._degree_max

    # ------------------------------------------------------------------
    # Getter method: _degree_min.
    # ------------------------------------------------------------------
    def get_degree_min(self) -> int:
        """Getter method: _degree_min.

        Returns:
            int: The lower limit for the random generation of the degrees.
        """
        return self._degree_min

    # ------------------------------------------------------------------
    # Getter method: _is_verbose.
    # ------------------------------------------------------------------
    def get_is_verbose(self) -> bool:
        """Getter method: _is_verbose.

        Returns:
            bool: Showing progress messages.
        """
        return self._is_verbose

    # ------------------------------------------------------------------
    # Getter method: _no_tasks.
    # ------------------------------------------------------------------
    def get_no_tasks(self) -> int:
        """Getter method: _no_tasks.

        Returns:
            int: The number of tasks to be generated.
        """
        return self._no_tasks

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
                    self._check_single_config_param(key, value)

    # ------------------------------------------------------------------
    # Setter method: _coef_min & _coef_max.
    # ------------------------------------------------------------------
    def set_coef(self, coef_min: int, coef_max: int) -> None:
        """Setter method: _coef_min & _coef_max.

        Args:
            coef_min (int):
                The lower limit for the random generation of the coefficients.
            coef_max (int):
                The upper limit for the random generation of the coefficients.
        """
        self._coef_min = coef_min
        self._coef_max = coef_max

        self._check_all_config_params()

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
        self._check_single_config_param(key, value)

    # ------------------------------------------------------------------
    # Setter method: _degree_min & _degree_max.
    # ------------------------------------------------------------------
    def set_degree(self, degree_min: int, degree_max: int) -> None:
        """Setter method: _degree_min & _degree_max.

        Args:
            degree_min (int):
                The lower limit for the random generation of the degrees.
            degree_max (int):
                The upper limit for the random generation of the degrees.
        """
        self._degree_min = degree_min
        self._degree_max = degree_max

        self._check_all_config_params()

    # ------------------------------------------------------------------
    # Setter method: _is_verbose.
    # ------------------------------------------------------------------
    def set_is_verbose(self, is_verbose: bool) -> None:
        """Setter method: _is_verbose.

        Args:
            is_verbose (bool): Showing progress messages.
        """
        self._is_verbose = is_verbose

        self._check_all_config_params()

    # ------------------------------------------------------------------
    # Setter method: _no_tasks.
    # ------------------------------------------------------------------
    def set_no_tasks(self, no_tasks: int) -> None:
        """Setter method: _no_tasks.

        Args:
            no_tasks (int): The number of tasks to be generated
        """
        self._no_tasks = no_tasks

        self._check_all_config_params()
