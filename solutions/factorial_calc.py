#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the factorial.

Module contents:
    - factorial_calc: calculates the factorial of a given number.

Created on 2 1 2025
@author: Ammar Ibrahim
"""


def factorial_calc(number: int) -> int:
    """Calculate the factorial of a non-negative integer.

    Parameters:
        number: int, the integer to calculate the factorial for.

    Returns -> int: factorial of the number.

    Raises:
        AssertionError: if the argument is negtive or non integer.

    >>> factorial_calc(0)
    1
    >>> factorial_calc(1)
    1
    >>> factorial_calc(5)
    120
    """
    assert isinstance(number, int), "Input must be an integer."
    assert number >= 0, "Input must be a non-negative integer."

    factorial = 1
    for x in range(1, number + 1):
        factorial *= x

    return factorial
