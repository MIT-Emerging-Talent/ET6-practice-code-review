#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for performing bubble sort on an array.

Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements, and swaps them if they are in the wrong order. The
pass through the list is repeated until the list is sorted.

Module contents:
    - bubble_sort(arr): Sorts an array in ascending order using the bubble sort algorithm.

Created on 2025-1-4
@author: Tomas Teclehaimanot
"""


def bubble_sort(arr):
    """
    Sorts a list of elements in ascending order using the bubble sort algorithm.

    Parameters:
        arr: list, A list of comparable elements (integers, floats, etc.).

    Returns:
        None: The function sorts the list in place, and does not return a new list.

    Raises:
        AssertionError: If the input is not a list or if the list contains
        elements that are not comparable.

    Example:
        >>> arr = [5, 2, 9, 1, 5, 6]
        >>> bubble_sort(arr)
        >>> arr
        [1, 2, 5, 5, 6, 9]
                >>> arr2 = [12, 11, 13, 5, 6]
        >>> bubble_sort(arr2)
        >>> arr2
        [5, 6, 11, 12, 13]

        >>> arr3 = [3, 1, 4, 1, 5, 9, 2]
        >>> bubble_sort(arr3)
        >>> arr3
        [1, 1, 2, 3, 4, 5, 9]

    Time Complexity:
        Best case: O(n) when the list is already sorted (optimized with the is_swaped flag).
        Worst case: O(n^2) when the list is sorted in reverse order.

    Space Complexity:
        O(1) because the sorting is done in place and no additional memory is required.
    """
    arrlen = len(arr)

    assert isinstance(arr, list), "Input must be a list."
    assert all(
        isinstance(el, (int, float)) for el in arr
    ), "All elements in the list must be of type int or float."
    assert not any(
        isinstance(el, bool) for el in arr
    ), "Boolean values are not allowed in the list."

    # Outer loop: iterate through the entire array
    # With each iteration, the largest unsorted element "bubbles up" to its correct position
    # The loop runs n times in the worst case, where n is the length of the array
    for i in range(arrlen):
        is_swaped = False

        # Inner loop: compare adjacent elements and swap if they are in wrong order
        # The loop runs (n-i-1) times because:
        # 1. After each outer iteration, the last i elements are already sorted
        # 2. We compare elements j and j+1, so we stop at n-i-1 to avoid index out of range
        for j in range(arrlen - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swaped = True

        if not is_swaped:
            break
