#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating sum of integers in a given list.

Module contents:
    - sum_elements: A function to calculate the sum of integers in a list.

Created on 2025-01-06
@author: Rumiya Ismatova
"""


def sum_elements(numbers: list) -> int:
    """
    Calculate the sum of all elements in a list.

    Args:
        numbers[int]: A list of integers

    Returns:
        int: the sum of the numbers in the list

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the list is not an integer.


    >>> sum_elements([1,2,3])
    6

    >>> sum_elements([2,3,3])
    8

    >>> sum_elements([])
    0
    """

    if numbers is None:
        raise TypeError("No arguments provided. Please pass a list of integers.")

    assert isinstance(numbers, list), "The input must be a list."

    if len(numbers) == 0:
        return 0

    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")

    return sum(numbers)
