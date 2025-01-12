#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sum_list.py
# Author: Jha-mal
"""
Module: sum_list

A function that sums all numeric items in a list.

This file:
- Provides the 'sum_list' function.
- Does not call 'sum_list' directly (to comply with "The function is not called in the function file").

Strategy:
- We ensure every item in the list is numeric using a simple defensive assertion.
- Then we use Python's built-in sum function.

Implementation:
- We keep the function simple with minimal lines of code.
- We maintain snake_case for variables and function names.
- We include 3 or more doctests as required.

Doctests:
    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([-1, -2, -3])
    -6
    >>> sum_list([0, 0, 1.5])
    1.5
    >>> sum_list([])
    0
"""

from typing import List


def sum_list(numbers: List[float]) -> float:
    """
    Return the sum of all numbers in the list.

    Behavior:
      - Accepts a list of numeric values (int, float).
      - Returns the total as a float.

    Arguments:
      :param numbers: List[float]
        The list of items to sum. Must be numeric values.

    Return Value:
      :return: float
        The sum of all items in 'numbers' as a float.

    Raises:
      TypeError:
        If any item in 'numbers' is not numeric (int or float).

    :examples:
      >>> sum_list([1.0, 2.0, 3.0])
      6.0
      >>> sum_list([-1, -2.5, 3])
      -0.5
      >>> sum_list([])
      0
    """

    # Defensive assertion (checks exactly one assumption: item must be numeric)
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError("All items must be numeric (int or float).")

    # Summation strategy: use Python built-in 'sum'
    return sum(numbers)
