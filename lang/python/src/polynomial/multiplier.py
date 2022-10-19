# Copyright (c) 2022 FAA-VAIL-Project. All rights reserved.
# Use of this source code is governed by the GNU LESSER GENERAL
# PUBLIC LICENSE, that can be found in the LICENSE.md file.

"""Class for multiplying the polynomials and checking the result."""
from __future__ import annotations

import cmath
import json
import os
import time
from cmath import exp
from math import pi

import numpy
import sds_glob  # type: ignore
import utils  # type: ignore
from numpy import ndarray


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

    def __eq__(self, other):
        if other == 1:
            return abs(self.n) == abs(self.k)

    def __mul__(self, other):
        return exp(2 * 1j * pi * self.k / self.n) * other

    def __repr__(self):
        return str(self.n) + "-th root of unity to the " + str(self.k)

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
def FFT(A, omega):
    if omega == 1:
        return [sum(A)]
    B = [[], []]
    i = 0
    for a in A:
        B[i % 2].append(a)
        i += 1
    o2 = omega**2
    C1 = FFT(B[0], o2)
    C2 = FFT(B[1], o2)
    C3 = [None] * omega.th
    for i in range(omega.th // 2):
        C3[i] = C1[i] + omega**i * C2[i]
        C3[i + omega.th // 2] = C1[i] - omega**i * C2[i]
    return C3


# ------------------------------------------------------------------
# The Fast Polynomial Multiplication Algorithm
# Input: A,B, two arrays of integers representing polynomials
# Output: Coefficient representation of AB
# Complexity: O(n log n)
# ------------------------------------------------------------------
def FPM(A, B):
    n = 1 << (len(A) + len(B) - 2).bit_length()
    o = NthRootOfUnity(n)
    AT = FFT(
        A, o
    )
    # FFT input: coefficient representation of polynomial,
    # output: value representation of polynomial
    BT = FFT(B, o)
    C = [AT[i] * BT[i] for i in range(n)]
    # nm = (len(A) + len(B) - 1)
    D = [int((a / n).real) for a in FFT(C, o**-1)]
    while True:
        if D[-1] != 0:
            return D
        else:
            del D[-1]


# ------------------------------------------------------------------
# https://www.youtube.com/watch?v=Ty0JcR6Dvis    FFT example, unraveling the recursion
# ------------------------------------------------------------------
def fft2(P):
    # P: [p0, p1, ...pn-1]  coefficient representation of a polynomial
    n = len(P)  # n is a power of 2
    if n == 1:
        return P
    w = cmath.exp((2.0 * cmath.pi * 1j) / n)  # this is omega
    P_even = P[0::2]
    P_odd = P[1::2]
    y_even = fft2(P_even)
    y_odd = fft2(P_odd)
    y = [0] * n
    for j in range(n // 2):
        y[j] = y_even[j] + w**j * y_odd[j]
        y[j + n // 2] = y_even[j] - w**j * y_odd[j]
    return y


# ------------------------------------------------------------------
# The complex conjugate of a complex number is obtained by changing
# the sign of its imaginary part.
# ------------------------------------------------------------------
def ifft(X):
    result = fft2([x.conjugate() for x in X])
    return [x.conjugate() / len(X) for x in result]


def multiply_polynomials(p, q):
    x = len(p) + len(q)
    n = 1

    while n < x:
        n = n * 2

    for i in range(n - len(p)):
        p.append(0)
    for i in range(n - len(q)):
        q.append(0)

    pfft = fft2(p)
    qfft = fft2(q)

    c = []
    for i in range(n):
        c.append(pfft[i] * qfft[i])

    d = ifft(c)
    result = []
    for i in range(len(d)):
        result.append(round(d[i].real))

    # Eliminate the leading zero terms and determine
    # the final degree of the polynomial product.
    zeros = []

    for degree in range(len(result) - 1, -1, -1):
        if result[degree] == 0:
            zeros.append(degree)
        else:
            break

    if zeros:
        result = numpy.delete(result, zeros)

    return result


# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
class Multiplier:
    """Class for multiplying the polynomials and checking the resulting
    product."""

    # ------------------------------------------------------------------
    # Initialise the instance.
    # ------------------------------------------------------------------
    def __init__(self, file_name: str, method: str) -> None:
        """Perform the tasks from the JSON file.

        An instance of this class processes a JSON file created by the
        'Generator' class. Three different methods for calculating the
        polynomial products are provided:

            'fft'    - a Fast Fourier Transform oriented method.
            'numpy'  - the polynomial multiplication of the polynomial
                       module of NumPy
            'simple' - a sequential multiplication of all terms of
                       the two polynomials with each other and then
                       a summation of the like terms

        Args:
            file_name (str):
                The name of the JSON file to process.
            method (str):
                The processing method: fft, numpy or simple.
        """
        # pylint: disable=duplicate-code
        # Start the run-related time measurement.
        start_time = time.time_ns()

        sds_glob.logger.debug(sds_glob.LOGGER_START)

        # Provide progress messages.
        utils.progress_msg("-" * 79)
        # INFO.00.021 Start Multiplier - Python - {method}
        utils.progress_msg(sds_glob.INFO_00_021.replace("{method}", method))
        utils.progress_msg("-" * 79)

        self._file_name = file_name
        self._method = method

        # Check if the specified JSON file with the polynomials exists.
        if not os.path.isfile(file_name):
            # ERROR.00.902 The specified JSON file {file_name} does not exist
            utils.terminate_fatal(
                sds_glob.ERROR_00_902.replace("{file_name}", file_name)
            )

        self._poly_1_coeff: list[int] = []
        self._poly_1_degree = 0
        self._poly_2_coeff: list[int] = []
        self._poly_2_degree = 0
        self._poly_no_coeff = 0
        self._prod_coeff: list[int] = []
        self._prod_degree = 0
        self._statistics: list[tuple[int, int, int, int]] = []
        self._task_no = 0

        # Process the polynomial multiplication tasks contained in the JSON file.
        with open(
            self._file_name, "r", encoding=sds_glob.FILE_ENCODING_DEFAULT
        ) as file_handle:
            json_data = json.load(file_handle)
            for task_no, task in enumerate(json_data[sds_glob.JSON_NAME_TASKS]):
                # Start the task-related time measurement.
                start_time_task = time.time_ns()

                # Store the data from the JSON file for polynomial multiplication
                # in instance variables
                self._poly_1_coeff = task[sds_glob.JSON_NAME_POLYNOM_1][
                    sds_glob.JSON_NAME_COEFFICIENTS
                ]
                self._poly_1_degree = task[sds_glob.JSON_NAME_POLYNOM_1][
                    sds_glob.JSON_NAME_DEGREE
                ]
                self._poly_2_coeff = task[sds_glob.JSON_NAME_POLYNOM_2][
                    sds_glob.JSON_NAME_COEFFICIENTS
                ]
                self._poly_2_degree = task[sds_glob.JSON_NAME_POLYNOM_2][
                    sds_glob.JSON_NAME_DEGREE
                ]
                self._prod_coeff = task[sds_glob.JSON_NAME_PRODUCT][
                    sds_glob.JSON_NAME_COEFFICIENTS
                ]
                self._prod_degree = task[sds_glob.JSON_NAME_PRODUCT][
                    sds_glob.JSON_NAME_DEGREE
                ]
                self._task_no = task_no

                # Calculate and check the polynomial product.
                self._process_task()

                # Stop the timing and save the measurement results.
                duration_task = time.time_ns() - start_time_task
                self._statistics.append(
                    (
                        duration_task,
                        self._poly_1_degree,
                        self._poly_2_degree,
                        self._prod_degree,
                    )
                )

        # Print the statistics data for this run.
        self._show_statistics()

        # Provide progress messages.
        utils.progress_msg("-" * 79)
        utils.progress_msg_time_elapsed(
            time.time_ns() - start_time,
            "Python - " + self._method,
        )

        utils.progress_msg("-" * 79)
        # INFO.00.022 End   Multiplier - Python - {method}
        utils.progress_msg(sds_glob.INFO_00_022.replace("{method}", self._method))
        utils.progress_msg("-" * 79)

        sds_glob.logger.debug(sds_glob.LOGGER_END)

    # ------------------------------------------------------------------
    # Multiply the polynomials by applying the Fast Fourier transform.
    # ------------------------------------------------------------------
    def _multiply_fft(self) -> ndarray:
        """Multiply the polynomials by applying Fast Fourier transform.

        Returns:
            ndarray: The product of the polynomials.
        """
        return multiply_polynomials(self._poly_1_coeff, self._poly_2_coeff)

    # ------------------------------------------------------------------
    # Multiply the polynomials by applying the NumPy polynomial methods.
    # ------------------------------------------------------------------
    def _multiply_numpy(self) -> ndarray:
        """Multiply the polynomials by applying the NumPy polynomial methods.

        Returns:
            ndarray: The product of the polynomials.
        """
        return numpy.polynomial.Polynomial(
            self._poly_1_coeff
        ) * numpy.polynomial.Polynomial(self._poly_2_coeff)

    # ------------------------------------------------------------------
    # Multiply the polynomials by applying the simple method.
    # ------------------------------------------------------------------
    def _multiply_simple(
        self,
    ) -> ndarray:
        """Multiply the polynomials by applying the simple method.

        Returns:
            ndarray: The product of the polynomials.
        """
        result = numpy.zeros(
            len(self._poly_1_coeff) + len(self._poly_2_coeff), dtype=numpy.int64
        )

        # Multiply abd collect the like terms
        for degree_1, coeff_1 in enumerate(self._poly_1_coeff):
            if coeff_1 != 0:
                for degree_2, coeff_2 in enumerate(self._poly_2_coeff):
                    if coeff_2 != 0:
                        result[degree_1 + degree_2] += coeff_1 * coeff_2

        # Eliminate the leading zero terms and determine
        # the final degree of the polynomial product.
        zeros = []

        for degree in range(len(result) - 1, -1, -1):
            if result[degree] == 0:
                zeros.append(degree)
            else:
                break

        if zeros:
            result = numpy.delete(result, zeros)

        return result

    # ------------------------------------------------------------------
    # Perform the processing of a polynomial multiplication task.
    # ------------------------------------------------------------------
    def _process_task(self):
        """Perform the processing of a polynomial multiplication task."""
        result = []

        if self._method == sds_glob.ARG_METHOD_FFT:
            self._multiply_fft()
        elif self._method == sds_glob.ARG_METHOD_NUMPY:
            self._multiply_numpy()
        else:
            result = self._multiply_simple()

        # Compare the new calculated product with the given product
        # in the JSON file.
        for degree, coeff in enumerate(result):
            if coeff != self._prod_coeff[degree]:
                # ERROR.00.911 Difference in task no. {task_no} degree {degree}
                # got {got} instead of {instead}
                utils.terminate_fatal(
                    sds_glob.ERROR_00_911.replace("{task_no}", str(self._task_no + 1))
                    .replace("{degree}", str(degree))
                    .replace("{got}", str(coeff))
                    .replace(
                        "{instead}",
                        str(self._prod_coeff[degree]),
                    )
                )

    # ------------------------------------------------------------------
    # Display the statistics.
    # ------------------------------------------------------------------
    def _show_statistics(self):
        """Display the statistics."""
        for task_no, (
            duration,
            poly_1_degree,
            poly_2_degree,
            prod_degree,
        ) in enumerate(self._statistics):
            utils.progress_msg_time_elapsed(
                duration,
                f"task no. {task_no + 1:2d} (degrees: {poly_1_degree:5d} - "
                + f"{poly_2_degree:5d} - {prod_degree:5d}) executed",
            )
