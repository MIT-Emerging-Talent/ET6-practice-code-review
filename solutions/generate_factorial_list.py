#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating mathematical sequences.

Module contents:
    - prime_list: generates a list of prime numbers up to a given limit.
    - factorial_list: generates a list of factorials up to a given number.
    - pascals_triangle: generates Pascal's Triangle up to a given number of rows.

Created on Jan 3, 2025
@author: Dadi Ishimwe
"""

import math

def factorial_list(n: int) -> list[int]:
    """Generates a list of factorials up to a given number.

    Parameters:
        n: int, the number up to which factorials are calculated.

    Returns:
        list[int]: A list of factorials from 0! to n!.

    Raises:
        AssertionError: if the argument is not a non-negative integer.

    >>> factorial_list(5)
    [1, 1, 2, 6, 24, 120]
    >>> factorial_list(0)
    [1]
    >>> factorial_list(3)
    [1, 1, 2, 6]
    """
    assert isinstance(n, int) and n >= 0, "n must be a non-negative integer."
    return [math.factorial(i) for i in range(n + 1)]
