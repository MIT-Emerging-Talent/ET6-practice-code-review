#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting a list of numbers based on their colors.

Module contents:
    - sort_colors: sorts a list of integers representing colors (0, 1, 2) in ascending order.

Dependencies:
    - typing: Used for type annotations (List).

Notes:
    - Does not use built-in sorting functions or libraries such as `sorted()` or `sort()`.
    - Implements an in-place counting sort approach.
    - Time complexity: O(n)
    - Space complexity: O(1) (in-place).

Created on 26 12 2024
@author: Mohamed-Elnageeb
"""

from typing import List  # Importing List for type annotations


def sort_colors(nums: List[int]) -> None:
    """
    Sorts a given list of integers representing colors (0, 1, 2) in-place.

    This function implements sorting logic manually using a counting sort approach and does not use
    any built-in sorting functions or libraries, such as `sorted()` or `sort()`.

    Time Complexity:
        O(n): Iterates through the list once to count occurrences and again to modify it in-place.

    Space Complexity:
        O(1): Uses a fixed-size counter list of size 3. No additional space is used.

    Parameters:
        nums: List[int]
            A list of integers where each integer is 0, 1, or 2. Modified in-place.

    Returns:
        None

    Raises:
        AssertionError: if the input is not a list or contains invalid elements (numbers out of the range 0 to 2).

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
    # Validate input
    assert isinstance(nums, list), "Input must be a list."
    assert all(0 <= number <= 2 for number in nums), "All elements must be 0, 1, or 2."

    # Create a counter list to store the count of each number
    counter_list = [0] * 3

    # Count occurrences of each number
    for number in nums:
        counter_list[number] += 1

    # Rebuild the nums list in-place
    index = 0
    for number in range(3):
        for _ in range(counter_list[number]):
            nums[index] = number
            index += 1
