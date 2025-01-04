#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module to verify if a number results from subtracting a sequence of defined numbers.

Module contents:

- subtract: determines whether an input integer is a result of subtraction involving given numbers.

Created on 01/01/2025

@author: Hafiz Hussein

Inspired by a challenge from the Leetcode website.

Explanation of subtraction for a given number:

"""


def subtract(*args):
    """
    Calculate the result of subtracting a series of numbers.


    Parameters:
        *args (int or float): Numbers to be subtracted in sequence.

    Returns:
    int or float: The result obtained after performing the subtraction.

    Raises:
        TypeError: If any input is not a number.

    Example:
    >>> subtract(10, 2, 3)
    5
    >>> subtract(11, 3, 6)
    2
    >>> subtract(14, 3, 6)
    5

    """
    # Defensive assertion: Check if all arguments are numbers
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("All inputs must be numeric (int or float).")

    # Handle the case where no arguments are provided
    if not args:
        return 0

    # Approach: Start with the first number and subtract the rest in sequence
    total = args[0]

    for i in args[1:]:
        total -= i

    return total
