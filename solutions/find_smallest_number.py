#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the smallest number in a list of integers.

Module contents:
    - find_smallest_number: finds the smallest number in a list.

Created on XX XX XX
@author: Saliha Kalender
"""

from typing import List


def find_smallest_number(numbers: List[int]) -> int:
    """
    Finds the smallest number in a given list of integers.

    Args:
        numbers (List[int]): A list of integers. Must contain at least one element.

    Returns:
        int: The smallest number in the list.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If any element in the list is not an integer.

    Examples:
        >>> find_smallest_number([3, 1, 4, 1, 5, 9])
        1
        >>> find_smallest_number([-10, -20, 0, 5, 10])
        -20
        >>> find_smallest_number([42])
        42
    """
    # Defensive assertions
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    if not numbers:
        raise ValueError("Input list must not be empty.")

    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements in the list must be integers.")

    # Find and return the smallest number
    return min(numbers)


if __name__ == "__main__":
    # Example usage
    example_list = [3, 1, 4, 1, 5, 9]
    print("The smallest number is:", find_smallest_number(example_list))
