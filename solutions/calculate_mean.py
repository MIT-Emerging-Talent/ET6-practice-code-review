#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to calculate the mean (average) of a list of numbers.

Date created: Dec 30,2024
Author: @Abel Teka
"""

from typing import List, Optional


def calculate_mean(numbers: List[float]) -> Optional[float]:
    """
    Calculate the mean (average) of a list of numbers.

    Args:
        numbers (List[float]): A list of numbers (integers or floats).
            - The list can include positive, negative, or zero values.

    Returns:
        Optional[float]: The mean (average) of the numbers in the list.
            - Returns nothing if the list is empty.

    Raises:
        TypeError: If `numbers` is not a list or contains non-numeric elements.
        Exception: If the list contains infinite or NaN values.

    Examples:
        >>> calculate_mean([1, 2, 3, 4, 5])
        3.0
        >>> calculate_mean([10, 20, 30])
        20.0
        >>> calculate_mean([])

        >>> calculate_mean([5])
        5.0
        >>> calculate_mean([1.5, 2.5, 3.5])
        2.5
        >>> calculate_mean([-1, 2, -3, 4, -5])
        -0.6
        >>> calculate_mean("123")
        Traceback (most recent call last):
        ...
        TypeError: Input must be a list.
        >>> calculate_mean([1, 2, "3"])
        Traceback (most recent call last):
        ...
        TypeError: All elements in the list must be numbers.
        >>> calculate_mean([1, 2, float("inf")])
        Traceback (most recent call last):
        ...
        ValueError: The list contains NaN or infinity, which are not allowed.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if any(not isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements in the list must be numbers.")
    if any(x != x or x in {float("inf"), float("-inf")} for x in numbers):
        raise ValueError("The list contains NaN or infinity, which are not allowed.")

    if not numbers:
        return None

    return sum(numbers) / len(numbers)
