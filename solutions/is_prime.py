# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
is_prime.py

This module provides a function to determine whether a given number is prime.
A prime number is a natural number greater than 1 that is not divisible by any
number other than 1 and itself.

Author: Fahed Daibes
Date: Fri Jan 10 2025
Group: ET6-foundations-group-16
"""


def is_prime(number: int) -> bool:
    """
    Determines if a given number is prime.

    Parameters:
    - number (int): The number to check.

    Returns:
    - bool: True if the number is prime, False otherwise.

    Raises:
    - AssertionError: If the input is not an integer.

    Examples:
        >>> is_prime(2)
        True

        >>> is_prime(4)
        False

        >>> is_prime(17)
        True

        >>> is_prime(1)
        False

        >>> is_prime(-5)
        False

        >>> is_prime("eleven")
        Traceback (most recent call last):
            ...
        AssertionError: Input must be an integer.
    """
    # Defensive check
    assert isinstance(number, int), "Input must be an integer."

    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True
