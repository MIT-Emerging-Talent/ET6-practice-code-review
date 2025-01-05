#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for filtering strings from a mixed list of integers and strings.

Module contents:
    - filter_list: filters out strings from a list, keeping only integers.

Created on 01/03/2025

@author: Hafiz Hussein

Challenge is from leetcode website

List Filtering
In this you will create a function that takes a list of non-negative
integers and strings and returns a new list with the strings filtered out.

"""

# --- before documenting ---
# def filter_list(lst: list) -> list
#'return a new list with the strings filtered out'


# --- after documenting ---


def filter_list(lst):
    """
    Filters out all strings from a list, keeping only non-negative integers.

    Parameters:
        lst: list, a list containing non-negative integers and strings

    Returns -> list: a new list with strings removed

     Raises:
        TypeError: If the input is not a list or contains invalid types (not int or str).

    >>> filter_list([1, 2, 'a', 'b'])
    [1, 2]
    >>> filter_list([1, 'a', 'b', 0, 15])
    [1, 0, 15]
    >>> filter_list([1, 2, 'hussein', '1', '123', 123])
    [1, 2, 123]
    """
    # Defensive assertion: Ensure input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list containing integers and strings.")

    # Defensive assertion: Ensure all elements in the list are either int or str
    if not all(isinstance(item, (int, str)) for item in lst):
        raise TypeError("List elements must be integers or strings.")

    # Initialize an empty list to hold filtered integers

    filtered_list = []  # Initialize an empty list

    for item in lst:
        if isinstance(item, int):
            filtered_list.append(item)
    return filtered_list


# print(filter_list([1, 2, 3, 5, 6, 9, 'a', 'b']))  # Output: [1, 2]
# print(filter_list([1, 'a', 'b', 0, 15]))  # Output: [1, 0, 15]
# print(filter_list([1, 2, 'hussein', '1', '123', 123]))  # Output: [1, 2, 123]
