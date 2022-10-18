# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Exception of **polynomial** application."""


class PolynomialError(RuntimeError):
    """Exception of **polynomial** application."""

    def __init__(self, error_msg):
        """Constructor."""
        super().__init__(error_msg)
        