#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to find the maximum of three numbers.

This module defines the `find_max` function, which takes three numerical inputs
and returns the largest value among them.

Created: 04/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Shaima Mohamed
"""


def find_max(num1: int | float, num2: int | float, num3: int | float) -> int | float:
    """
    Find the Maximum of Three Numbers.

    Parameters:
        num1: int or float. The first number. Must be a valid number.
        num2: int or float. The second number. Must be a valid number.
        num3: int or float. The third number. Must be a valid number.

    Returns: int or float.
        The largest number among the three inputs.

    Raises:
        AssertionError: If any input is not an integer or float.

    >>> find_max(3, 1, 2)
    3
    >>> find_max(-1, -2, -3)
    -1
    >>> find_max(0, 0, 0)
    0
    >>> find_max(2.5, 3.1, 2.9)
    3.1
    """
    # Defensive checks to ensure all inputs are numbers
    assert isinstance(num1, (int, float)), "Input 'a' must be an int or float."
    assert isinstance(num2, (int, float)), "Input 'b' must be an int or float."
    assert isinstance(num3, (int, float)), "Input 'c' must be an int or float."

    # Return the largest of the three numbers
    return max(num1, num2, num3)
