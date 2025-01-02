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


    Example:
    >>> subtract(10, 2, 3)
    5

    """
    if not args:
        return 0

    total = args[0]

    for i in args[1:]:
        total -= i

    return total
