# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Module stub file."""

class Config:
    def __init__(self, config_file=...) -> None:
        self.coef_max: int = ...
        self.coef_min: int = ...
        self.degree_max: int = ...
        self.degree_min: int = ...
        self.is_verbose: bool = ...
        self.no_tasks: int = ...
    def exists(self) -> bool: ...
    def load_config_file(self, config_file: str) -> None: ...
    def set_config_value(self, key: str, value: bool | int | str) -> None: ...
