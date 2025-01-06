#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for finding the largest perfect square less than a given number.

Module contents:
    - largest_perfect_square_less_than_number:
    returns the largest perfect square that is less than the given number.


Created on 2025-01-06
@author: Huda Alamassi
"""

from typing import Union


def largest_perfect_square_less_than_number(number: Union[int, float]) -> int:
    """
    The function takes in a number (either int or float) and returns the largest perfect square
    that is less than the given number.

    Arguments:
    number (int, float): The input number to check for the largest perfect square less than it.

    Assumptions:
    - The input number must be a non-negative number (either integer or float).

    Returns:
    int:
        - The largest perfect square that is less than the input number.
        - If no perfect square exists (i.e., for inputs less than or equal to 1 or equal to 0),
        the function will return 0.



    Raises:
    AssertionError: If the input is a negative number (integer or float).
    AssertionError: If the input is not a number (neither integer nor float).

    Examples:
        >>> largest_perfect_square_less_than_number(50)
        49

        >>> largest_perfect_square_less_than_number(16.5)
        9

        >>> largest_perfect_square_less_than_number(1)
        0

        >>> largest_perfect_square_less_than_number(100.99)
        81
    """
    # Validate input type to avoid errors in mathematical operations
    assert isinstance(
        number, (int, float)
    ), "Input must be a number (either integer or float)."

    # Negative numbers do not have valid perfect squares
    assert number >= 0, "Input must be a non-negative number."

    # Handle edge cases where no perfect square exists below 1
    if number <= 1:
        return 0

    square_root = number**0.5

    # Ensure we work with the integer part of the square root
    square_root = int(square_root)

    # Find the largest perfect square less than the number
    perfect_square = square_root * square_root

    # Adjust when the number is exactly or close to a perfect square
    if perfect_square == int(number):
        perfect_square = (square_root - 1) * (square_root - 1)

    return perfect_square
