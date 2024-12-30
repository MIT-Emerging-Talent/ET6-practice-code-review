#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for a function that performs binary search on a sorted list.

Module contents:
    - binary_search: Performs binary search on a sorted list.

Created on 2024-12-27
Author: Awaab98"""

from typing import List, Union


def binary_search(
    list_to_be_searched: List[Union[int, float, str]],
    target_element: Union[int, float, str]
) -> int:
    """Performs binary search on a sorted list to find the index of a target element
    using recursion.
    if there are multiple occurrences of the target element in the list, the function
    returns the index of the first occurrence.

    Parameters:
        list_to_be_searched: int, float, str: A sorted list in ascending order to be searched.
        target_element: int, float, str: The element to be searched for in the list.

    Returns:
        int: The index of the target element in the list if it is found.

    Raises:
        TypeError: If the first argument is not a list.
        TypeError: If the list is not a list of integers, floats or strings.
        TypeError: If the elements of the list are not of the same type.
        TypeError: If the second argument is not of the same type as the elements of the list.
        ValueError: If the list is empty.
        ValueError: If the target element is not found in the list.
        AssertionError: If the list is not sorted in ascending order.

    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
        >>> binary_search([1.0, 2.0, 3.0, 4.0, 5.0], 3.0)
        2
        >>> binary_search(['a', 'b', 'c', 'd', 'e'], 'c')
        2
        >>> binary_search(['a', 'b', 'c', 'd', 'e'], 'f')
        -1
    """
    
    # Make sure the first argument is a list
    if not isinstance(list_to_be_searched, list):
        raise TypeError("The first argument must be a list.")

    # Make sure the list is not empty
    if len(list_to_be_searched) == 0:
        raise ValueError("The list must not be empty.")

    # Ensure that all elements of the list are of the same type
    if not all(isinstance(x, type(list_to_be_searched[0])) for x in list_to_be_searched):
        raise TypeError("All elements in the list must be of the same type.")

    # Ensure that the elements of the list belong to one of the following types: int, float, str
    if type(list_to_be_searched[0]) not in [int, float, str]:
        raise TypeError("The list must contain elements of type int, float or str.")

    # Ensure that the second argument is of the same type as the elements of the list
    if not isinstance(target_element, type(list_to_be_searched[0])):
        raise TypeError(
            "The second argument must be of the same type as the elements of the list."
        )

    # Ensure that the list is sorted in ascending order
    assert list_to_be_searched == sorted(
        list_to_be_searched
    ), "The list must be sorted in ascending order."
    
    return 9
