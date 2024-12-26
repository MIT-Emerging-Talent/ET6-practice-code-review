#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the average of two numbers.

Module contents:
    - calculate_average: calculates the average of two numbers.

Created on 26.12.2024
@author: Yevheniia Rudenko
"""

def calculate_average(num1: float, num2: float) -> float:
    """Calculate the average of two numbers.
    
    Parameters:
        num1: float, the first number
        num2: float, the second number
        
    Returns -> float: the average of num1 and num2

    Raises:
        AssertionError: if any argument is not a number
    
    >>> calculate_average(4, 6)
    5.0
    
    >>> calculate_average(10, 20)
    15.0
    
    >>> calculate_average(-3, 3)
    0.0
    """
    assert isinstance(num1, (int, float)), "num1 must be a number"
    assert isinstance(num2, (int, float)), "num2 must be a number"
    
    return (num1 + num2) / 2
