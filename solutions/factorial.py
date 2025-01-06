#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to calculate the factorial of a number using recursion.

This module includes a factorial function that takes a number as input
and returns the factorial of that number using recursion.

Created: 05/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Shaima Mohamed
"""


def factorial(n: int) -> int:
    """
    Calculate the factorial of a number using recursion.

    Parameters:
        n: int. The number for which the factorial is to be calculated.

    Returns:
        int: The factorial of the input number.

    Raises:
    AssertionError: If the input is not an integer.
    AssertionError: If the input is a negative integer.

    >>> factorial(5)
    120
    >>> factorial(3)
    6
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    """
    # Defensive check to ensure the input is an integer
    assert isinstance(n, int), "Input must be an integer"

    # Defensive check to ensure the input is a non-negative integer
    assert n >= 0, "Input must be a non-negative integer"

    # The strategy recursively calculates the factorial by multiplying the number
    # with the factorial of the previous number until the base case (n=0 or n=1) is reached.

    # Base case: factorial of 0 or 1 is 1
    if n in (0, 1):
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)
