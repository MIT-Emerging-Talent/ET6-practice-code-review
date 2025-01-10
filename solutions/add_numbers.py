#!/usr/bin/env python3
# -- coding: utf-8 --

"""
A module that takes two numbers and return their sum.

Module contents: Takes two numbers and return their sum.

Created on 2025-01-08

@author: Martha Yelademe Nyekanga
"""


def add_numbers(num1: int, num2: int) -> int:
    """This function takes two numbers and returns their sum.

    Parameters:
    num1 (int): The first number for the function
    num2 (int): The second number for the function

    Returns:
    int: The sum of the two numbers

    Raises:
    TypeError: If the input is not a number

    Examples:
    >>> add_numbers(2, 3)
    5

    >>> add_numbers(-2, 3)
    1

    >>> add_numbers(0, 0)
    0

    >>> add_numbers(2, -3)
    -1
    """

    assert isinstance(num1, int), "Input must be a number."
    assert isinstance(num2, int), "Input must be a number."

    # return  the sum of the two numbers
    return num1 + num2


print(add_numbers(0, 0))
