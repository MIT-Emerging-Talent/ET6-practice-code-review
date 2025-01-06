#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating quotient of two numbers (inputs) "a" and "b"

Module contents:
    - Division: finds the quotient of two numbers; both integers and floats.

Created on 05.01.2025
@author: Zephaniah Okoye
"""

def divide(a: float, b: float) -> float:
    """Divides one number by another and returns the result.

    Parameters:
        a (float): the numerator
        b (float): the denominator

    Returns -> (float): the result of the division

    Raises:
        ZeroDivisionError: if the denominator is zero
        TypeError: if either argument is not a number

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(9, 3)
        3.0
        >>> divide(7, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Cannot divide by zero
    """

    if not isinstance(a, (int, float)):
        raise TypeError("Both arguments must be numbers")

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b

if __name__ == "__main__": 
    import doctest
    doctest.testmod()