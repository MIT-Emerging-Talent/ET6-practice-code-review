#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for merging two lists of items.

Module contents:
    -merge two lists

Created on 2025-01-08
@author: Ajanduna Emmanuel
"""

# write a function that merging two lists of items

from typing import List, Union


def merge_two_given_lists(
    list1: List[Union[int, str]], list2: List[Union[int, str]]
) -> List[Union[int, str]]:
    """
    Merge two lists into one.

    Args:
        list1 (List[Union[int, str]]): The first list to merge.
        list2 (List[Union[int, str]]): The second list to merge.

    Returns:
        List[Union[int, str]]: A new list containing all elements from
        list1 followed by all elements from list2.

    Raises:
        TypeError: If either of the arguments is not a list.

    Examples:
        >>> merge_two_given_lists([1, 2, 3], [4, 5, 6])
        [1, 2, 3, 4, 5, 6]

        >>> merge_two_given_lists(['a', 'b'], ['c', 'd'])
        ['a', 'b', 'c', 'd']

        >>> merge_two_given_lists([], [1, 2, 3])
        [1, 2, 3]
    """
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both arguments must be lists.")

    return list1 + list2
