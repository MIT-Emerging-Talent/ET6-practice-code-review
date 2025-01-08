#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting a list of numbers based on their colors.

Module contents:
    - sort_colors: Sorts a list of integers representing colors (0, 1, 2) in ascending order.

Dependencies:
    - typing: Used for type annotations (List).

Created on 26 12 2024
@author: Mohamed-Elnageeb
"""

from typing import List


def sort_colors(nums: List[int]) -> None:
    """
    Sorts a given list of integers representing colors (0, 1, 2) in-place.

    Parameters:
        nums: List[int]
            A list of integers where each integer is 0, 1, or 2. Modified in-place.

    Returns:
        None

    Raises:
        AssertionError: If the input is not a list or contains invalid elements (numbers out of the range 0 to 2).

    Examples:
    >>> nums = [0, 2, 1]
    >>> sort_colors(nums)
    >>> nums
    [0, 1, 2]

    >>> nums = [1]
    >>> sort_colors(nums)
    >>> nums
    [1]

    >>> nums = [2, 1, 1, 0, 2]
    >>> sort_colors(nums)
    >>> nums
    [0, 1, 1, 2, 2]
    """
    # Input validation
    assert isinstance(nums, list), "Input must be a list."
    assert all(0 <= number <= 2 for number in nums), "All elements must be 0, 1, or 2."

    # Count occurrences of 0, 1, and 2
    counter_list = [0] * 3
    for number in nums:
        counter_list[number] += 1

    # Rebuild the list based on counts
    index = 0
    for number in range(3):
        for _ in range(counter_list[number]):
            nums[index] = number
            index += 1
