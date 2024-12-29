#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the percentage of one number relative to another.

Module contents:
    - calculate_percentage: calculates what percentage the first number is of the second.

Created on 26.12.2024
@author: Yevheniia Rudenko
"""


def calculate_percentage(numerator: float, denominator: float) -> float:
    """Calculate what percentage the first number is of the second. This function calculates the percentage by dividing part by whole and then multiplying by 100.

    Parameters:
        part: float, the numerator value
        whole: float, the denominator value

    Returns -> float: the percentage of `part` in `whole`

    Raises:
        AssertionError: if any argument is not a number
        ZeroDivisionError: if `whole` is zero

    >>> calculate_percentage(50, 200)
    25.0
    >>> calculate_percentage(5, 20)
    25.0
    >>> calculate_percentage(0, 100)
    0.0
    """
    assert isinstance(part, (int, float)), "part must be a number"
    assert isinstance(whole, (int, float)), "whole must be a number"
    if whole == 0:
        raise ZeroDivisionError("whole must not be zero")

    return (part / whole) * 100
