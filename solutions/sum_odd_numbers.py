#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-01-02

@author: Sukhrob Muborakshoev
"""


def sum_odd_numbers(numbers: list[int]) -> int | None:
    """
    Calculate the sum of only odd numbers in a given list.

    Parameters:
    numbers (list[int]): The input list of integers.

    Returns:
    int: The sum of all odd numbers in the provided list.
    None: If the list is invalid.

    Raises:
    TypeError: If the input is not a list.

    Examples:
    >>> sum_of_odds([1, 2, 3, 4, 5])
    9
    >>> sum_of_odds([2, 4, 6, 8])
    0
    >>> sum_of_odds([1, -3, 5, -7])
    -4
    >>> sum_of_odds([])
    0
    """
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total
