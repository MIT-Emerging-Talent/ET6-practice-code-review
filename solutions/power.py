#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a recursive function to calculate a power of an integer number.

Module contents:
    - power: returns the power of an integer number.

Created on 2025-01-04
@author: Nay Win Hlaing
"""


def power(base, exponent):
    """
    Returns the power of an integer number.

    Parameters:
        base: int
        exponent: int

    Returns:
        int

    Raises:
        TypeError: if the base parameter is not an int.
        TypeError: if the exponent parameter is not an int.
        ValueError: if the base is 0 and the exponent is 0.
        ValueError: if the base is 0 and the exponent is a negative value.

    >>> power(1000, 0):
    1
    >>> power(2003, 1):
    2003
    >>> power(10, 3):
    1000
    >>> power(10, 8):
    100000000
    """
    # Validate base input is a number.
    if not isinstance(base, (int)):
        raise TypeError("Input must be an integer type.")

    # Validate exponent input is a number.
    if not isinstance(exponent, (int)):
        raise TypeError("Input must be an integer type.")

    # Check for undefined cases:
    # 0 raised to the power of 0 is mathematically ambiguous.
    if base == 0 and exponent == 0:
        raise ValueError("0 power 0 is undefined.")

    # 0 raised to a negative exponent is undefined.
    if base == 0 and exponent < 0:
        raise ValueError("0 raised to a negative exponent is undefined.")

    # Compute exponent 0 of any base value; results in 1.
    if exponent == 0:
        output = 1

    # Compute exponent 1 of any base value; results in the base value itself.
    elif exponent == 1:
        output = base

    # Compute exponent -1 of any base value; results in the reciprocal of the base value.
    elif exponent == -1:
        output = 1 / base

    # If the exponent is even:
    elif exponent % 2 == 0:
        # n^p = (n*n)^(p/2)
        output = power(base * base, exponent // 2)

    # If the exponent is odd:
    else:
        # n^p = n * (n*n)^(p-1)/2
        output = base * (power(base * base, (exponent - 1) // 2))

    return output
