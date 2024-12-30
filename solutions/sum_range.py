#!/usr/bin/env python3
# --#coding: utf-8 --
"""
Description: This file contains the test cases for the sum_range function.

This module defines the sum_range function that calculates the sum of all
integers from start to end (inclusive).

parameters:
- The start and end arguments must be integers.
- The start argument must be less than or equal to the end argument.
- Return integer value of the sum of all integers from start to end.

Example:
    The sum_range function can be used as follows:
    # Calculate the sum of all integers from 1 to 20
    total = sum_range(1, 20)
    print(total)  # Output: 210
    # Calculate the sum of all integers from -10 to 10
    total = sum_range(-10, 10)
    print(total)  # Output: 0
    # Calculate the sum of all integers from 10 to 1
    total = sum_range(10, 1)
    print(total)  # Output: 55

date:2024-12-31
@ author: Zeinab Mommed
"""


def sum_range(start: int, end: int) -> int:
    """
    Calculate the sum of all integers from start to end (inclusive).
    Args:
        start (int): The starting integer.
        end (int): The ending integer.
    Returns:
        int: The sum of all integers from start to end.
    Raises:
        TypeError: If start or end is not an integer.
    """
    assert isinstance(start, int), "start must be an integer"
    assert isinstance(end, int), "end must be an integer"
    # Ensure start is less than or equal to end
    if start > end:
        start, end = end, start
    # Calculate the sum of the range
    total = 0
    for number in range(start, end + 1):
        total += number
    return total
