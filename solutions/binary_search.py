#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for performing binary search on a sorted list.

Binary Searching is a searching algorithm used in a sorted array by repeatedly dividing the search
interval in half. It works by repeatedly dividing the search interval in half until the target value
is found or the interval is empty..

Module contents:
    - binary_search(arr, item, start, end): Searches for an item in a sorted list
        within a specified range using the binary search algorithm.

Created on 2025-01-02
@author: Alexander Andom
"""


def binary_search(arr: list[int], item: int, start: int, end: int):
    """
    Perform binary search to find the index of an item in a sorted list.

    Parameters:
        arr : list[int], A sorted list of integers to search within.
        item : int, The target item to search for.
        start : int, The starting index of the search range.
        end : int, The ending index of the search range.

    Returns:
        int: The index of the item if found; otherwise, -1.

    Raises:
        AssertionError:
            - If 'arr' is not a list.
            - If 'item' is not an integer.
            - If 'start' or 'end' are not integers or are negative.
            - If the input list is not sorted in ascending order.

    Example:
        >>> arr = [1, 2, 3, 4, 5]
        >>> binary_search(arr, 3, 0, len(arr) - 1)
        2

        >>> binary_search(arr, 6, 0, len(arr) - 1)
        -1

        >>> binary_search(arr, 1, 0, len(arr) - 1)
        0
    """

    assert isinstance(arr, list), "Input 'arr' must be a list."
    assert isinstance(item, int), "Input 'item' must be an integer."
    assert isinstance(start, int), "Input 'start' must be an integer."
    assert start >= 0, "Input 'start' must be greater than or equal to 0."
    assert isinstance(end, int), "Input 'end' must be an integer."
    assert end >= 0, "Input 'end' must be greater than or equal to 0."
    assert arr == sorted(arr), "Input list must be sorted."

    if len(arr) < 1 or end < 0 or start < 0:
        return -1
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if item == arr[mid]:
        return mid
    if item < arr[mid]:
        return binary_search(arr, item, start, mid - 1)

    return binary_search(arr, item, mid + 1, end)
