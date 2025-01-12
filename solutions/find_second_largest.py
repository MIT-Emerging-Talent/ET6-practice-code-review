#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A module for finding the second largest unique number in a list.
Module contents:
    - find_second_largest: finding the second largest unique number in a list.

Created on: 06/01/2025
@author: Ermishina Mariia
"""


def find_second_largest(numbers: list) -> int:
    """
    Finding the second largest unique number in a list
    Parameters:
        numbers (list): List of numbers as int.
    Returns:
        int: The second largest unique number.
    Raises:
        ValueError: If there are not enough unique numbers to determine the second largest.
    Examples:
    >>> find_second_largest([2, 3, 6, 6, 5])
    5
    >>> find_second_largest([1, 2, 3, 4, 5])
    4
    >>> find_second_largest([10, 9, 9, 8, 8, 8, 7])
    9
    >>> find_second_largest([1, 1, 1, 1])
    Traceback (most recent call last):
        ...
    ValueError: Not enough unique numbers to determine the second largest.
    """
    # Convert the list to a set to remove duplicates
    unique_numbers = set(numbers)

    # Check if there are enough unique numbers
    if len(unique_numbers) <= 2:
        raise ValueError("Not enough unique numbers to determine the second largest.")

    # Convert back to a sorted list in descending order
    sorted_numbers = sorted(unique_numbers, reverse=True)

    # Return the second largest number
    return sorted_numbers[1]
