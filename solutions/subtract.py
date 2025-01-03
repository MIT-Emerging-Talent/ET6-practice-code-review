#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for determining whether a given number
is a subtraction of defined numbers.
Module contents:
    - subtract: checks if a given integer
    is a subtraction of those given numbers.
Created on 01/01/2025

@author: Safa Ishag

Challenge is from the Leetcode website.

Defining the subtraction of a given number:

"""


def subtract(*args):
    """
    Return the subtraction of all input numbers

    Parameters:
        *args (int or float): The numbers to subtract

    Returns:
    int or float: The result of subtracting all input numbers

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
