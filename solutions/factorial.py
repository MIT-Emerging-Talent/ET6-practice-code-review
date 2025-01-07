#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for Computing the factorial of a non-negative integer n.

Module contents:
    - factorial: is the product of all positive integers less than or equal to n.

Created on XX XX XX
@author: Saad M. Ashour
"""


def factorial(n: int) -> int:
    """
    Computes the factorial of a non-negative integer n.

    The factorial of a non-negative integer n
    is the product of all positive integers less than or equal to n.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of the input integer n.

    Raises:
        ValueError: If n is negative, as factorial is not defined for negative numbers.
        TypeError: If n is not an integer, as factorials are only defined for integers.

    Examples:
    >>> factorial(0)
    1

    >>> factorial(1)
    1

    >>> factorial(5)
    120

    >>> factorial(3)
    6
    """
    # Validate input type and value
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    # Base case for recursion: 0! = 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)
