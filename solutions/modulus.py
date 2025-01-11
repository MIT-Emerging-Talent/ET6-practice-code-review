#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for modulus of two numbers.

This module contains a function that calculates the remainder when
one number is divided by another.

Created on 06.01.2025
@author : Simi-Solola
"""


def modulus(a: float, b: float) -> float:
    """
    Calculates the remainder when one number is divided by another.

    Parameters:
    a (float): The numerator (the number to be divided).
    b (float): The denominator (the number to divide by, must be non-zero).

    Returns:
    float: The remainder when 'a' is divided by 'b'.

    Raises:
    ValueError: If the denominator 'b' is zero.
    TypeError: If 'a' or 'b' is not a float or int.

    Assumptions:
    - Both 'a' and 'b' are numeric values (either integers or floats).
    - If 'a' or 'b' is not a number, a TypeError will be raised.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both numerator and denominator must be numbers.")

    if b == 0:
        raise ValueError("Denominator cannot be zero.")

    remainder = a % b

    # Adjust the result to match the dividend's sign
    if (a < 0 and remainder > 0) or (a > 0 and remainder < 0):
        remainder -= b

    return remainder
