#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the factorial of a non-negative integer

Created on 4 1 2025
@author: Ahmed Hussein
"""


def calculate_factorial(number: int) -> int:
    """Calculate the factorial of a non-negative number.

    Parameters:
        number: int, The number to calculate the factorial of, greater than or equal to zero

    Returns -> int, the factorial of the number, greater than zero

    Raises:
        AssertionError: if the argument is not an integer
        ValueError: if the argument is less than 0

    >>> calculate_factorial(0)
    1

    >>> calculate_factorial(2)
    2

    >>> calculate_factorial(5)
    120

    >>> calculate_factorial(10)
    3628800

    >>> calculate_factorial(42)
    1405006117752879898543142606244511569936384000000000

    """
    # Validate the input data type
    assert isinstance(number, int)

    # Validate input as the factorial is not defined for negative integers
    if number < 0:
        raise ValueError("The number should be greater or equal to zero")

    # Handle edge case: factorial of 0
    if number == 0:
        return 1

    factorial = 1

    # Iterate to calculate the factorial
    while number > 1:
        factorial = factorial * number
        number = number - 1

    return factorial
