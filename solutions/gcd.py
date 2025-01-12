# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
gcd.py

This module provides a function to calculate the greatest common divisor (GCD)
of two integers using the Euclidean algorithm.

Author: Fahed Daibes
Date: Jan 12 2025
Group: ET6-foundations-group-16
"""


def gcd(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two integers.

    Parameters:
    - a (int): The first integer.
    - b (int): The second integer.

    Returns:
    - int: The GCD of the two numbers.

    Raises:
    - AssertionError: If either input is not an integer.

    Examples:
        >>> gcd(48, 18)
        6

        >>> gcd(101, 103)
        1

        >>> gcd(0, 25)
        25

        >>> gcd(0, 0)
        0

        >>> gcd("eight", 16)
        Traceback (most recent call last):
            ...
        AssertionError: Both inputs must be integers.
    """
    # Defensive check
    assert isinstance(a, int) and isinstance(b, int), "Both inputs must be integers."

    while b != 0:
        a, b = b, a % b

    return abs(a)
