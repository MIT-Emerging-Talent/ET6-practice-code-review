#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for factorial function

Module contents:
    factorial: to calculate the factorial of input numbers

Created on 02-01-2025
@author: Samir Ahmed Shaifta
"""


def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer.

    Returns:
    int: The factorial of the input number.

    Raises:
    ValueError: If the input is negative.
    TypeError: If the input is not an integer.

    Examples:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    """
    assert isinstance(n, int), "input must be integer"
    assert n >= 0, "input can not be negative"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
