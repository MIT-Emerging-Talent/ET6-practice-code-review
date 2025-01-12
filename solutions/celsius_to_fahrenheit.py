#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting temperatures between Celsius and Fahrenheit.
Module contents:
    - celsius_to_fahrenheit: converts a temperature from Celsius to Fahrenheit.
Created on 30 12 2024
@author: Terry Aziaba
"""

import math


def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts a temperature from Celsius to Fahrenheit.
    Parameters:
        celsius: float, the temperature in Celsius.
    Returns -> float:
        The temperature in Fahrenheit.
    Raises:
        AssertionError: if the argument is not a float or int.
    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
        >>> celsius_to_fahrenheit(-40)
        -40.0
    """
    # This line ensures the input (temperature) is a number (int or float)
    assert isinstance(celsius, (int, float)), "Input temperature must be a number."
    assert not math.isnan(celsius), "Input temperature must not be NaN."

    # Conversion
    fahrenheit = (celsius * 9 / 5) + 32

    return fahrenheit
