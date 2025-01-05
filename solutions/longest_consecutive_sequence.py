#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module provides a function to find the length of
the longest consecutive sequence in a list of integers.
Created on: 2025/1/5
@author: Hamidullah Rajabi
"""

"""
longest_consecutive_sequence.py

This module provides a function to find the length of the longest consecutive sequence in a list of integers.
"""

from typing import List


def longest_consecutive_sequence(nums: List[int]) -> int:
    """
    Finds the length of the longest sequence of consecutive integers in a list.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        int: The length of the longest consecutive sequence.

    Raises:
        TypeError: If `nums` is not a list.
        TypeError: If `nums` contains non-integer elements.
        ValueError: If the list contains `None`values.
        ValueError: If the list contains `NaN` values.

    Doctests:
        >>> longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
        4
        >>> longest_consecutive_sequence([0, -1, 1, 2, 3, 7, 8, 9])
        5
        >>> longest_consecutive_sequence([])
        0
    """

    if not isinstance(nums, list):
        raise AssertionError("Input must be a list.")
    if any(num is None for num in nums):
        raise ValueError("List must not contain None values.")
    if any(num != num for num in nums):  # NaN check
        raise ValueError("List must not contain NaN values.")
    if not all(isinstance(num, int) for num in nums):
        raise AssertionError("All elements in the list must be integers.")
    if not nums:
        return 0

    nums_set = set(nums)
    max_length = 0

    for num in nums:
        if num - 1 not in nums_set:  # Start of a sequence
            current_num = num
            current_length = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length
