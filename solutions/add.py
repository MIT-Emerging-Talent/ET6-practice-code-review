#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for adding two numbers.

Module contents: 
    -add: adds two numbers and returns the result.
    
Created on 28.12.2024
@author : Ridwan Ayinde

"""


def add(a: float, b: float) -> float:
    """Add two numbers.

    Parameters:
        a:float, the first number
        b:float, the second number

    Returns -> float: the sum of a and b

    Raises:
        AssertionError: if any argument is not a number

    >>> add(4, 6)
    10.0
    >>> add(0, 0)
    0.0

    """
    # Validate inputs
    assert isinstance(a, (int, float)), "a must be a number"
    assert isinstance(b, (int, float)), "b must be a number"
    return float(a + b)
