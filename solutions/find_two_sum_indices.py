#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for providing the indices of two numbers in a list that add up to a target sum.

Module contents: Takes a list of numbers (integers or floats) and a target sum as input and returns the indices of the two numbers that add up to the target sum.

Created on 2025-01-04

@author: Jeffery Offei Darko
"""


def find_two_sum_indices(nums: list[float], target: float) -> list[int]:
    """
    Find two indices in the list such that their values add up to the target.

    Parameters:
    nums (list[float]): The list of numbers (integers or floats).
    target (float): The target sum.

    Returns:
    list[int]: The indices of the two numbers that add up to the target.

    Raises:
    AssertionError: If the input is not valid or no solution is found.

    Examples:
    >>> find_two_sum_indices([2, 7, 11, 15], 9)
    [0, 1]

    >>> find_two_sum_indices([3, 2.5, 4], 6.5)
    [1, 2]

    >>> find_two_sum_indices([3.0, 3], 6.0)
    [0, 1]
    """
    import math

    # Validate inputs
    assert isinstance(nums, list), "Input must be a list."
    assert all(isinstance(num, (int, float)) for num in nums), (
        "List must contain numbers."
    )
    assert isinstance(target, (int, float)), "Target must be a number."
    assert len(nums) > 1, "List must contain at least two numbers."
    assert not any(math.isnan(x) for x in nums), (
        "Input list must not contain NaN values."
    )
    assert not math.isnan(target), "Target must not be NaN."

    # Main logic with floating-point precision handling
    epsilon = 1e-7
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        for seen_num, seen_index in num_map.items():
            if abs(seen_num - complement) < epsilon:
                return [seen_index, i]
        num_map[num] = i

    assert False, "No two numbers add up to the target sum."
