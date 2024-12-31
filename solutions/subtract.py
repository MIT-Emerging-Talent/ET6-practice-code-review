#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

""" 
A module for subtracting two numbers.

Module contents:
    subtract: subtract one number from another and returns the result.

Created on 31.12.2024
@author : Ridwan Ayinde

"""


def subtract(a: float, b: float) -> float:
    """
    Subtract one number from the other.

    Parameters:
        a:float, the first number
        b:float, the second number

    Returns -> float : the subtraction of b from a

    Raises:
        AssertionError: if any argument is not a number

    >>> subtract (10, 5)
    5.0
    >>> subtract (-5, 5)
    -10.0

    """

    # Validate inputs
    assert isinstance(a, (int, float)), "a must be a number"
    assert isinstance(b, (int, float)), " b must be a number"
    return float(a - b)
