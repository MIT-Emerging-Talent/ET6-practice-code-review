#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the body mass index (BMI).

Module contents:
    - calculate_bmi: calculates the BMI of a person.

Created on 6 1 2025
@author: Collins Ochieng
"""


def calculate_bmi(weight: float, height: float) -> float:
    """Calculate the body mass index (BMI) of a person.

    Parameters:
        weight: float, the weight of the person in kilograms.
        height: float, the height of the person in meters.

    Returns -> float: The calculated BMI.

    Raises:
        AssertionError: if the arguments are not numbers (float).
        ValueError: if either weight or height is less or equal to 0

    >>> calculate_bmi(63, 1.68)
    22.32
    >>> calculate_bmi(80, 1.75)
    26.12
    >>> calculate_bmi(50, 1.50)
    22.22
    >>> calculate_bmi(69, 1.49)
    31.08
    """

    assert isinstance(weight, (float, int)), "Weight must be a number (float)."
    assert isinstance(height, (float, int)), "Height must be a number (float)."

    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive numbers.")

    bmi = weight / (height**2)
    return round(bmi, 2)
