#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for summing the positive numbers in a list.

Module contents:
    - sum_positive_numbers: calculates the sum of all positive numbers
    in a given list.

Created on 2025-01-10
@author: Huda Alamassi
"""


def sum_positive_numbers(numbers: list) -> float:
    """
    The function takes a list of numbers and returns the sum of all positive
    numbers in the list. Negative numbers and zeros are ignored.

    Arguments:
    numbers (list): A list of numbers (integers or floats) to be summed.
        - Assumed that the list contains numeric elements (integers or floats).


    Returns:
    float:
        - The sum of all positive numbers in the list.
        - If there are no positive numbers, it returns 0.


    Raises:
    AssertionError:If the input is not a list.
    AssertionError: If the list contains non-numeric elements.

    Examples:
        >>> sum_positive_numbers([1, 2, 3, -1, 0])
        6

        >>> sum_positive_numbers([-1, -2, -3])
        0

        >>> sum_positive_numbers([5, 0, 10.5, 2])
        17.5

        >>> sum_positive_numbers([0, 0, 0])
        0
    """

    # Validate input type
    assert isinstance(numbers, list), "Input must be a list"

    for num in numbers:
        assert isinstance(num, (int, float)), (
            f"List must contain only numeric elements, but found: {type(num)}"
        )

    # Ensures that if there's no data to process, we handle it efficiently
    if not numbers:
        return 0

    total = 0

    # Sum the positive numbers only
    for num in numbers:
        if num > 0:
            total += num

    return total
