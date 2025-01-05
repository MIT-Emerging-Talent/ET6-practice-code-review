#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting temperature from Fahrenheit to Kelvin.

Module contents:
    - fahrenheit_to_kelvin: converts a temperature from Fahrenheit to Kelvin.

Created on 5 1 2025
@author: Ammar Ibrahim
"""


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Convert a temperature from Fahrenheit to Kelvin.

    Parameters:
        fahrenheit: float, the entered temperature in Fahrenheit.

    Returns -> float: The returned temperature in Kelvin.

    Raises:
        AssertionError: if the argument is not a number (float).

    >>> fahrenheit_to_kelvin(32)
    273.15
    >>> fahrenheit_to_kelvin(212)
    373.15
    >>> fahrenheit_to_kelvin(-40)
    233.15
    """
    assert isinstance(fahrenheit, (float, int)), "Input must be a number (float)."

    # Step 1: Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5 / 9

    # Step 2: Convert Celsius to Kelvin
    kelvin_accurate = celsius + 273.15

    kelvin_with_precision = round(kelvin_accurate, 2)

    return kelvin_with_precision
