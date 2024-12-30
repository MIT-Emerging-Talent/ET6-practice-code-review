#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Name: intersection_of_two

Description: This module provides a function to find the intersection of two lists.
and returns a new list containing the common elements between them.

The module includes: the following function:
    - intersection_of_two(list1,list2): Returns a new list with the intersection

Author: Linah Khayri
Date Created: 30-12-2024
"""


def intersection_of_two(list1: list, list2: list) -> list:
    """This function takes two lists and returns a list containing the intersection of them.

    The intersection includes only the items that are present in both
    list1 and list2. The items in the intersection are returned only once,
    even if they appear multiple times in the input lists. The input lists
    can contain any type of items that are allowed in a list (e.g., integers,
    strings, floats, special characters, etc.)

    Parameters:
        list1 (list): The first list of items
        list2 (list): The second list of items

    Returns:
        list:A list containing the items that are common to both
              list1 and list2 and will not contain duplicate items.

    Raises:
      AssertionError: if list1 is not a list
      AssertionError: if list2 is not a list
      AssertionError: if any of the lists are empty

    >>> intersection_of_two([1, 2, 3, 4],[3, 4, 5, 6])
    [3, 4]
    >>> intersection_of_two(['a', 'cat', 'ABC', 'dog'],['c', 'abc', 'cat'])
    ['cat']
    >>> intersection_of_two(['$', '&', '@'],['$', '&', '@'])
    ['$', '&', '@']
    >>> intersection_of_two(['1', 3, 'girl'],['a', 4, 3, '1', 'boy'])
    ['1', 3]

    """
    assert isinstance(list1, list), "first list must be a list"
    assert isinstance(list2, list), "second list must be a list"
    assert len(list1) > 0, "list1 can't be empty"
    assert len(list2) > 0, "list2 can't be empty"

    intersection = []

    for item in list1:
        if item in list2 and item not in intersection:
            # Check if the item is in the second list and not already in the intersection

            intersection.append(item)

    return intersection
