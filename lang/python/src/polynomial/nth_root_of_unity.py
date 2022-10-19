# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""A simple class to simulate n-th root of unity.

It is implemented merely for FFT and FPM algorithm.
"""
from __future__ import annotations

import cmath


# pylint: disable=too-few-public-methods
class NthRootOfUnity:
    """Multiplying the polynomials and checking the result.

    A simple class to simulate n-th root of unity. It is implemented
    merely for FFT and FPM algorithm.
    """


# ------------------------------------------------------------------
# Computing the complex conjugates.
# ------------------------------------------------------------------
def fft_complex_conjugate(polynomial) -> list[complex]:
    """Computing the complex conjugates.

    The complex conjugate of a complex number is obtained by changing
    the sign of its imaginary part.

    Args:
        polynomial (list[int]): The coefficients of the polynomial.

    Returns:
        list[complex]: The complex conjugates.
    """
    result = fft_recursive([coeff.conjugate() for coeff in polynomial])

    return [coeff.conjugate() / len(polynomial) for coeff in result]


# ------------------------------------------------------------------
# Recursive FFT.
# ------------------------------------------------------------------
def fft_recursive(polynomial: list[int]):
    """Recursive FFT.

    Args:
        polynomial (list[int]): The coefficients of a polynomial.

    Returns:
        list[int]: The coefficients of a new polynomial.
    """
    polynomial_size = len(polynomial)  # n is a power of 2

    if polynomial_size == 1:
        return polynomial

    omega = cmath.exp((2.0 * cmath.pi * 1j) / polynomial_size)

    polynomial_even = polynomial[0::2]
    polynomial_odd = polynomial[1::2]

    polynomial_next_even = fft_recursive(polynomial_even)
    polynomial_next_odd = fft_recursive(polynomial_odd)

    polynomial_next = [0] * polynomial_size

    for degree in range(polynomial_size // 2):
        polynomial_next[degree] = (
            polynomial_next_even[degree] + omega**degree * polynomial_next_odd[degree]
        )
        polynomial_next[degree + polynomial_size // 2] = (
            polynomial_next_even[degree] - omega**degree * polynomial_next_odd[degree]
        )

    return polynomial_next


def multiply_polynomials(polynomial_a, polynomial_b):
    """_summary_

    Args:
        polynomial_a (list[int]):
            The coefficients of the first polynomial.
        polynomial_b (list[int]):
            The coefficients of the second polynomial.

    Returns:
        list[int]: Resulting product of the two polynomials.
    """
    size_total = len(polynomial_a) + len(polynomial_b)

    degree = 1

    while degree < size_total:
        degree = degree * 2

    for _ in range(degree - len(polynomial_a)):
        polynomial_a.append(0)
    for _ in range(degree - len(polynomial_b)):
        polynomial_b.append(0)

    polynomial_a_fft = fft_recursive(polynomial_a)
    polynomial_b_fft = fft_recursive(polynomial_b)

    polynomial_c = []

    for i in range(degree):
        polynomial_c.append(polynomial_a_fft[i] * polynomial_b_fft[i])

    polynomial_d = fft_complex_conjugate(polynomial_c)

    result = []

    for _, value in enumerate(polynomial_d):
        result.append(round(value.real))

    return result
