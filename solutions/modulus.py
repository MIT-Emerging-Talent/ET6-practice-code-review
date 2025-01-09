#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

"""
A module for modulus of two numbers.

Module contents:
    modulus: divide two numbers and returns the reminder.

Created on 06.01.2025
@author : Simi-Solola

"""


def modulus(a: float, b: float) -> float:
    """
    Calculates the remainder when one number is divided by another.

    Parameters:
    a (float): The numerator.
    b (float): The denominator (non-zero).

    Returns:
    float: The remainder of a divided by b.

    Raises:
    ValueError: If the denominator is zero.
    """
    if b == 0:
        raise ValueError(
            "The numerator and denominator can be any real numbers except the denominator cannot be zero."
        )

    remainder = a % b
    # Adjust the result to match the dividend's sign
    if (a < 0 and remainder > 0) or (a > 0 and remainder < 0):
        remainder -= b

    return remainder
