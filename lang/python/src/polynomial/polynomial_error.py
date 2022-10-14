# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""User-defined Exception."""


class PolynomialError(RuntimeError):
    """User-defined Exception."""

    def __init__(self, error_msg):
        """Constructor."""
        super().__init__(error_msg)
