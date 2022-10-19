# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Class for multiplying the polynomials and checking the result."""
from __future__ import annotations

import cmath


# ------------------------------------------------------------------
# A simple class to simulate n-th root of unity. It is implemented
# merely for FFT and FPM algorithm.
# ------------------------------------------------------------------
class NthRootOfUnity:
    def __init__(self, n, k=1):
        self.k = k
        self.n = n

    def __pow__(self, other):
        if type(other) is int:
            n = NthRootOfUnity(self.n, self.k * other)
            return n

    # def __eq__(self, other):
    #     if other == 1:
    #         return abs(self.n) == abs(self.k)
    #
    # def __mul__(self, other):
    #     return cmath.exp(2 * 1j * pi * self.k / self.n) * other
    #
    # def __repr__(self):
    #     return str(self.n) + "-th root of unity to the " + str(self.k)

    @property
    def th(self):
        return abs(self.n // self.k)


# ------------------------------------------------------------------
# The Fast Fourier Transform Algorithm
# Input: A, An array of integers of size n representing a polynomial
#        omega, a root of unity
# Output: [A(omega), A(omega^2), ..., A(omega^(n-1))]
# Complexity: O(n log n)
# ------------------------------------------------------------------
def fft(polynomial, omega):
    if omega == 1:
        return [sum(polynomial)]

    polynomials_b = [[], []]

    degree = 0

    for coeff in polynomial:
        polynomials_b[degree % 2].append(coeff)
        degree += 1

    omega_squared = omega**2

    polynomial_1 = fft(polynomials_b[0], omega_squared)
    polynomial_2 = fft(polynomials_b[1], omega_squared)
    polynomial_3 = [None] * omega.th

    for degree in range(omega.th // 2):
        polynomial_3[degree] = (
            polynomial_1[degree] + omega**degree * polynomial_2[degree]
        )
        polynomial_3[degree + omega.th // 2] = (
            polynomial_1[degree] - omega**degree * polynomial_2[degree]
        )

    return polynomial_3


# ------------------------------------------------------------------
# https://www.youtube.com/watch?v=Ty0JcR6Dvis    FFT example, unraveling the recursion
# P: [p0, p1, ...pn-1]  coefficient representation of a polynomial
# ------------------------------------------------------------------
def fft_recursive(polynomial: list[int]):
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


# ------------------------------------------------------------------
# The Fast Polynomial Multiplication Algorithm
# Input: A,B, two arrays of integers representing polynomials
# Output: Coefficient representation of AB
# Complexity: O(n log n)
# ------------------------------------------------------------------
def fpm(polynomial_a_coeff, polynomial_b_coeff):
    degree = 1 << (len(polynomial_a_coeff) + len(polynomial_b_coeff) - 2).bit_length()

    omega = NthRootOfUnity(degree)

    polynomial_a_value = fft(polynomial_a_coeff, omega)
    polynomial_b_value = fft(polynomial_b_coeff, omega)

    polynomial_c = [
        polynomial_a_value[i] * polynomial_b_value[i] for i in range(degree)
    ]

    polynomial_d = [int((a / degree).real) for a in fft(polynomial_c, omega**-1)]

    while True:
        if polynomial_d[-1] != 0:
            return polynomial_d
        else:
            del polynomial_d[-1]


# ------------------------------------------------------------------
# The complex conjugate of a complex number is obtained by changing
# the sign of its imaginary part.
# ------------------------------------------------------------------
def fft_complex_conjugate(polynomial):
    result = fft_recursive([coeff.conjugate() for coeff in polynomial])

    return [coeff.conjugate() / len(polynomial) for coeff in result]


def multiply_polynomials(polynomial_a, polynomial_b):
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

    for i in range(len(polynomial_d)):
        result.append(round(polynomial_d[i].real))

    return result
