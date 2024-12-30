#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A Function for removing the duplicates items in a list.

Created on 2024-12-30
Author: Heba Shaheen
"""


def remove_duplicates(nums: list) -> list:
    """
    Given a list, return a new list without any repeated values.
    The function goes item by item; if an item is not in the result list,
    it appends it; otherwise, it skips it.

    Args:
        nums (list): The list from which duplicates will be removed.

    Returns:
        list: A list without duplicates.
    Raises:
        AssertionError: If the input not a list.

    >>> remove_duplicates([2, 4, 2, 5, 5, 7, 2, 6])
    [2, 4, 5, 7, 6]

    >>> remove_duplicates(["a", "v", "e", "e", "q", "v", "q", "a"])
    ['a', 'v', 'e', 'q']

    >>> remove_duplicates(["Heba", "Noor", "Heba", "Noor"])
    ['Heba', 'Noor']
    """
    assert isinstance(nums, list), "The input should be a list"
    result = []  # List to store the result without duplicates

    for num in nums:
        if num not in result:
            result.append(num)  # Add the number to the result list
    return result
