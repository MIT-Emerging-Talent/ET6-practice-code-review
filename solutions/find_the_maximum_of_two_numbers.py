#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for finding the maximum of two numbers.

Module contents:
    -find_the_max

Created on 2025-01-06
@author: Ajanduna Emmanuel
"""

# write a function that finds the max of two number


def find_max_number(num1: int, num2: int):
    """this function takes two numbers and returns the greater value

    Args:
        num1 (int): First argument of the string
        num2 (int): Second argument of the string

    Returns:
        The maximum number of the numbers

    Raises:
        AssertionError: If  the input is not a int

    Examples:
    >>> find_max_number(2,4)
    4

    >>> find_max_number(0, -2)
    0

    >>> find_max_number(1, 9)
    9
    """

    assert isinstance(num1, int), "num1 must be a list"
    assert isinstance(num2, int), "num2 must be a list"

    return num1 if num1 > num2 else num2


print(find_max_number(0, 9))
