#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for performing insertion sort on an array.

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. 
It works by taking each element from the input and inserting it in the right position in the array.

Module contents:
    - insertion_sort(arr): Sorts an array in ascending order using the insertion sort algorithm.

Created on 2025-1-05
@author: Tomas Teclehaimanot
"""

def insertion_sort(arr):
    """
    Sorts a list of elements in ascending order using the insertion sort algorithm.

    Parameters:
        arr: list, A list of comparable elements (integers, floats, etc.).

    Returns:
        None: The function sorts the list in place, and does not return a new list.

    Raises:
        AssertionError: input is not list or If the list contains elements that are not comparable.
        
    Example:
        >>> arr = [5, 2, 9, 1, 5, 6]
        >>> insertion_sort(arr)
        >>> arr
        [1, 2, 5, 5, 6, 9]

        >>> arr2 = [12, 11, 13, 5, 6]
        >>> insertion_sort(arr2)
        >>> arr2
        [5, 6, 11, 12, 13]

        >>> arr3 = [3, 1, 4, 1, 5, 9, 2]
        >>> insertion_sort(arr3)
        >>> arr3
        [1, 1, 2, 3, 4, 5, 9]

    Time Complexity:
        Best case: O(n) when the list is already sorted.
        Worst case: O(n^2) when the list is sorted in reverse order.

    Space Complexity:
        O(1) because the sorting is done in place and no additional memory is required.
    """

    assert isinstance(arr, list), "Input must be a list."

    assert all(isinstance(el, (int, float)) for el in arr), \
        "All elements in the list must be of type int or float."

    assert not any(isinstance(el, bool) for el in arr), \
        "Boolean values are not allowed in the list."

    for i in range(1, len(arr)):
        tmp = arr[i]

        j = i - 1
        while(j >= 0 and tmp < arr[j]):
            arr[j + 1] = arr[j]
            j-=1

        arr[j + 1] = tmp
