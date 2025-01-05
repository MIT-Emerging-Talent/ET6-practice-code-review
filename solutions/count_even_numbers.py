#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 04 01 2025

@author: Norbert Ndayisenga
"""


def count_even_numbers(numbers):
    """
    Counts the even numbers in a list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The count of even numbers.

    Raises:
        AssertionError: If any element in the list is not an integer.
    """
    assert all(isinstance(num, int) for num in numbers), "All elements must be integers."
    return sum(1 for num in numbers if num % 2 == 0)
