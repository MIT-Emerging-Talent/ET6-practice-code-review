#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the mean of a list of numbers.

Module contents:
    - mean: finds the mean of a list of numbers.

Created on XX XX XX
@author: Mohammed Elfadil
"""


def mean(a: list) -> float:
    """Finds the mean of a list of numbers.
    Parameter:
        a: list
    Return -> float: the mean of the list
    Raises:
        AssertionError: if the argument is not a list
    >>> mean([1, 2, 3, 4, 5])
    3.0
    >>> mean([10, 20, 30, 40, 50])
    30.0
    >>> mean([1.5, 2.5, 3.5])
    2.5
    >>>mean([2])
    2.0
    """
    if not isinstance(a, list):
        return "invalid input"
    # return the mean of the list by dividing the sum of the list by the length of the list
    return sum(a) / len(a)
