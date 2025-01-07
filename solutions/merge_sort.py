#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting a list of integers and/or floats in the ascending order using the merge sort algorithm and recursion

Module contents:
    - merge_sort function

Created on 8-Jan-2025

@author: Aung Myin Moe
"""


# ---- define function ----
def merge_sort(array: list[int, float]) -> list[int, float]:
    """Sort a list of integers and/or floats in the ascending order using the merge sort algorithm and recursion

    Args: array (list[int, float])
        - a list of numbers to be sorted
        - the list must only contain integers and/or floats

    Returns: list[int, float]
        - return a list of sorted numbers in an ascending order

    Raises: AssertionError
        - if array is not a list
        - if array contains other than integers or floats

    >>> merge_sort([5, 4, 3, 2, 1, 0, -1, -2])
    [-2, -1, 0, 1, 2, 3, 4, 5]

    >>> merge_sort([1.0, 1, 3, 2.5, 4.5, 5, 7])
    [1.0, 1, 2.5, 3, 4.5, 5, 7]

    >>> merge_sort([2.999, 3.0, 4.1, 4.05, 200, 2000, 90000])
    [2.999, 3.0, 4.05, 4.1, 200, 2000, 90000]
    """
    # Ensure the input only contains a list of floats and/or integers
    assert isinstance(array, list), "The array to be sorted must be a list"

    assert all(
        isinstance(item, (int, float)) for item in array
    ), "The elements in the array must be either floats and/or integers"

    # Base case: an array of 1 or 0 elements is already sorted
    if len(array) <= 1:
        return array

    # Break-down: split the array in half
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursion: sort the left half
    sorted_left = merge_sort(left_half)

    # Recursion: sort the right half
    sorted_right = merge_sort(right_half)

    # Build-up: merge the two halves together in a sorted ascending order
    result = []
    i = j = 0

    # Compare smallest element from left half with smallest from right half and put the smaller element into sorted list
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            result.append(sorted_left[i])
            i += 1

        else:
            result.append(sorted_right[j])
            j += 1

    # If one half has no elements left to compare, add remaining elements from the other half into sorted list
    result.extend(sorted_left[i:])
    result.extend(sorted_right[j:])

    return result
