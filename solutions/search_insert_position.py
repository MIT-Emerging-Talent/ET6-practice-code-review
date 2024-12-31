#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides the `search_insert_position` function.

Functionality:
    - Determines the index of a target value in a sorted list of integers.
    - Returns the position where the target would be inserted if not found.

Created on 2024-12-31
Author: Omnia
"""


def search_insert_position(numbers: list[int], target: int) -> int:
    """
    Returns the index of the target in a sorted list, or the position where it should be inserted.

    Parameters:
        numbers (list[int]): A list of distinct integers sorted in ascending order.
        target (int): The integer to search for.

    Returns:
        int: The index or insertion position.

    Raises:
        AssertionError: If inputs are of incorrect type or format and if input lists are not sorted

    Examples:
        >>> search_insert_position([1, 3, 5, 6], 5)
        2
        >>> search_insert_position([1, 3, 5, 6], 2)
        1
        >>> search_insert_position([1, 3, 5, 6], 7)
        4
        >>> search_insert_position([], 5)
        0
    """
    # Assertions to validate input types
    assert isinstance(numbers, list), "First input must be a list"
    assert isinstance(target, int), "Second input must be an integer"
    assert all(
        isinstance(x, int) for x in numbers
    ), "Numbers list must only contain integers"
    assert numbers == sorted(
        numbers
    ), "The input list must be sorted in ascending order"

    for index in range(len(numbers)):
        # Check if the current number is greater than or equal to the target
        # If so, return the current index as the insertion point
        if numbers[index] >= target:
            return index

    # If no number in the list is greater than or equal to the target,
    # the target should be inserted at the end of the list.
    return len(numbers)
