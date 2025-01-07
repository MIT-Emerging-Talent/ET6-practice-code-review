#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Function to calculate BMI and determine weight category.

BMI Categories:
- Underweight: BMI < 18.5
- Normal weight: 18.5 ≤ BMI < 24.9
- Overweight: 25 ≤ BMI < 29.9
- Obese: BMI ≥ 30

Supports both metric and imperial systems.

Examples:
    >>> calculate_bmi(70, 1.75, "metric")
    'Normal weight'
    >>> calculate_bmi(150, 68, "imperial")
    'Normal weight'
    >>> calculate_bmi(50, 1.6, "metric")
    'Normal weight'
    >>> calculate_bmi(200, 72, "imperial")
    'Overweight'

Raises:
    ValueError: If input is invalid or system is not recognized.

Created on 2025-01-04
Author: Cynthia Wairimu
"""

from typing import Union


def calculate_bmi(
    weight: Union[int, float], height: Union[int, float], system: str
) -> str:
    """
    Calculate BMI and return the weight category.

    Args:
        weight (int | float): The person's weight.
        height (int | float): The person's height.
        system (str): The measurement system, either "metric" or "imperial".

    Returns:
        str: The weight category ("Underweight", "Normal weight", "Overweight", "Obese").

    Raises:
        ValueError: If input is invalid or system is not recognized.
    """
    if (
        not isinstance(weight, (int, float))
        or not isinstance(height, (int, float))
        or weight <= 0
        or height <= 0
    ):
        raise ValueError("Weight and height must be positive numbers.")
    if system.lower() not in ["metric", "imperial"]:
        raise ValueError("System must be 'metric' or 'imperial'.")

    # Calculate BMI based on the system
    if system.lower() == "metric":
        bmi = weight / (height**2)
    else:  # Imperial
        bmi = 703 * weight / (height**2)

    # Determine weight category
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"