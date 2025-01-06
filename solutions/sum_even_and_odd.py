#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module provides a function sum_even_and_odd
that calculates the sums of positive and negative,
even and odd numbers in a given list.
"""

from typing import Dict, List, Union


def sum_even_and_odd(numbers: List[Union[int, float]]) -> Dict[str, float]:
    """
    Calculate the sum of even and odd numbers in a list.

    Parameters:
        numbers (list of int or float): List of numbers to process.

    Returns:
        dict: Dictionary with sums of positive even, positive odd,
            ls  negative even, and negative odd numbers.

    Raises:
        ValueError: If input is not a list or contains non-numeric values.

    Examples:
    >>> sum_even_and_odd([1, -2, 3, 4, -5, 0])
    {'positive_even': 4, 'positive_odd': 4, 'negative_even': -2, 'negative_odd': -5}
    >>> sum_even_and_odd([])
    {'positive_even': 0, 'positive_odd': 0, 'negative_even': 0, 'negative_odd': 0}
    >>> sum_even_and_odd([1.5, -2.5, 4, -3])
    {'positive_even': 4, 'positive_odd': 1.5, 'negative_even': 0, 'negative_odd': -5.5}
    >>> sum_even_and_odd([0])
    {'positive_even': 0, 'positive_odd': 0, 'negative_even': 0, 'negative_odd': 0}
    >>> sum_even_and_odd([1000000000, -1000000000])
    {'positive_even': 1000000000, 'positive_odd': 0, 'negative_even': -1000000000, 'negative_odd': 0}
    >>> sum_even_and_odd("not a list")  # Invalid input type
    Traceback (most recent call last):
        ...
    ValueError: Input must be a list.

    >>> sum_even_and_odd([1, "two", 3])  # Invalid element type
    Traceback (most recent call last):
        ...
    ValueError: All elements must be integers or floats.

    """
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be integers or floats.")

    result = {
        "positive_even": 0,
        "positive_odd": 0,
        "negative_even": 0,
        "negative_odd": 0,
    }

    for num in numbers:
        if isinstance(num, (int, float)) and num > 0 and num % 2 == 0:
            result["positive_even"] += num
        elif isinstance(num, (int, float)) and num > 0:
            result["positive_odd"] += num
        elif isinstance(num, (int, float)) and num < 0 and num % 2 == 0:
            result["negative_even"] += num
        elif isinstance(num, (int, float)) and num < 0:
            result["negative_odd"] += num

    return result
