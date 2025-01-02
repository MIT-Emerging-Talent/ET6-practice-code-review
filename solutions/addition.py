#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for determining whether a given number is a sum of define number.

Module contents:
    - sum: checks if a given integer is a sum of those given numbers.

Created on 01/01/2025

@author: Safa Ishag

Challenge is from the Leetcode website.

Defining the sum of a given number:

"""


def sum(*args):
    """
    Return the sum of all input numbers.

    Parameters:
        *args (int or float): The number to check and is the variable.

    Returns:
    int or float: The sum of all input numbers.

    Example:
    >>> sum(1, 2, 3, 4, 5)
    15

    """
    total = 0

    for i in args:
        total += i

    return total
