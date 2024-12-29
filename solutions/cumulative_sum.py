#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module: cumulative_sum

Description:
    This module provides a function to calculate the cumulative sum of
    a list of numbers. It is useful for applications requiring progressive
    accumulation of values, such as financial calculations, data analysis,
    or custom mathematical operations.

Module Contents:
    - cumulative_sum(numbers: list) -> list:
        Computes and returns a list of cumulative sums from the input list.

Author: Falaq Youniss
Date: 29/12/2024
"""


def cumulative_sum(numbers: list) -> list:
    """
    Computes the cumulative sum of a list of numbers.

    Args:
        numbers (list): A list of numeric values (integers or floats).

    Returns:
        list: A list where each element is the cumulative sum up to that index.

    Raises:
        AssertionError:
            - If the input is not a list.
            - If the list contains non-numeric values.
            - If the input is `None`.

    >>> cumulative_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> cumulative_sum([-1, -2, -3, -4])
    [-1, -3, -6, -10]
    >>> cumulative_sum([1.0, 2.0, 3.0, 4.0])
    [1.0, 3.0, 6.0, 10.0]
    """
    # Validate input
    assert numbers is not None, "Input cannot be None."
    assert isinstance(numbers, list), "Input must be a list of numeric values."
    assert all(
        isinstance(num, (int, float)) for num in numbers
    ), "All elements in the list must be numeric."
    # Compute cumulative sums
    cumulative_list = []
    current_sum = 0
    for num in numbers:
        current_sum += num
        cumulative_list.append(current_sum)

    return cumulative_list
