#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A module containing a function to find the largest number in a list.
Module contents:
largest_number: Determines the largest number in a list.

Created on 2025-01-03
Author: Solara Hamza
"""

def largest_number(numbers: list) -> int:
    """Determines the largest number in a list.
    This function takes a list of numbers as input and returns the largest number.
    
    Parameters:
        numbers: list, the list of numbers to find the largest number.
    
    Returns -> int: The largest number in the list.
    
    Examples:
        >>> largest_number([1, 2, 3, 4, 5])
        5
        >>> largest_number([5, 4, 3, 2, 1])
        5
        >>> largest_number([1, 3, 5, 2, 4])
        5
        >>> largest_number([1, 2, 3, 4, 5, 5])
        5
    """
    if not numbers:
        raise ValueError("List must not be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number