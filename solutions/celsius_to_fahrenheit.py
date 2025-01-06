#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to convert temperature from Celsius to Fahrenheit.

This module includes celsius_to_fahrenheit function that takes a temperature in Celsius
and converts it to the equivalent Fahrenheit value.

Created: 04/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Shaima Mohamed
"""


def celsius_to_fahrenheit(celsius: int | float) -> int | float:
    """
    Convert Temperature from Celsius to Fahrenheit.

    Parameters:
        celsius: int or float. The temperature in Celsius to be converted.

    Returns: float.
        The temperature converted to Fahrenheit.

    Raises:
    AssertionError: If the input is not a number or is not a valid temperature.
    AssertionError: If the temperature is below absolute zero (-273.15°C).

    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(100)
    212.0
    >>> celsius_to_fahrenheit(-40)
    -40.0
    >>> celsius_to_fahrenheit(25.5)
    77.9
    """
    # Defensive check to ensure the input is a number and not below absolute zero
    assert isinstance(celsius, (int, float)), "Input must be an int or float"
    assert celsius >= -273.15, "Temperature can't be below absolute zero."

    # Convert Celsius to Fahrenheit using the formula
    fahrenheit = (celsius * 9 / 5) + 32

    return fahrenheit
