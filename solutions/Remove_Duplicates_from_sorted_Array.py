#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/01/2025
@author: Dorcas Wanja Njeri
"""


def remove_Duplicates_from_sorted_array(nums: list[int]) -> int:
    """
    Challenge: Remove Duplicates from Sorted Array
    Removes duplicates from a sorted array in place and returns the new length.

    Parameters:
        nums (list): A sorted list of integers.

    Returns:
        int: The length of the array after removing duplicates.
             The first part of the array (up to the returned length)
             will contain only unique elements.

    Raises:
        TypeError: If Nums is not a list of integers.
        IndexError: If Nums is modified externally during execution.

    Examples:
    >>> nums = [1, 1, 2]
    >>> remove_duplicates_from_sorted_array(nums)
    2
    >>> nums[:2]
    [1, 2]

    >>> nums = [0, 0, 1, 1, 2, 2, 3, 3, 4]
    >>> remove_duplicates_from_sorted_array(nums)
    5
    >>> nums[:5]
    [0, 1, 2, 3, 4]

    >>> nums = []
    >>> remove_duplicates_from_sorted_array(nums)
    0
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in nums):
        raise TypeError("All elements in the input list must be integers.")

    if not nums:
        return 0

    j = 0  # Initialize the pointer for the unique elements

    for i in range(1, len(nums)):  # Start from the second element
        if nums[i] != nums[j]:  # If the current element is different
            j += 1  # Move to the next unique position
            nums[j] = nums[i]  # Place the unique element in its position

    return j + 1
