#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module generates the least of comparing
two umbers and the sum if they are equal.

Created on 12 24 2024

@author : Osei Agyemang Sarfo
"""


def compare_numbers(num1: int, num2: int) -> int:
    """Compares two numbers and  generates the least number but adds them if they are equal.

    Parameters :

    num1 -> first input of the function(Integer)
    num2 -> Second input of the function.(Integer)

    Returns: -> integer.
    The least number if either is less than the other but twice the number if they are the same.

    >>> compare_numbers(23,78)
    23

    >>> compare_numbers(23,23)
    46

    >>> compare_numbers(-26,-91)
    -91
    """

    # num1 and num2 must be integers
    assert isinstance(num1, int), "The number must be an integer"
    assert isinstance(num2, int), "The number must be an integer"

    # Compares the two integers and print the greater value.
    # Generate num1 if it is less than num2
    if num1 < num2:
        return num1
    # Generate num2 if it is less than num1
    elif num1 > num2:
        return num2

    # Generate the sum of the numbers if they are the same.
    else:
        return num1 + num2
