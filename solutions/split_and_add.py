#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Write a function that takes a list and index.
# The function divides the list into two parts and
# returns the first part added to the end(second part).

"""
A module that splits a list on a given index and adds the first part to the end of the second part.


Module contents:
    split_and_add: splits a list and the first part is added to the end of the second part.
"""


def split_and_add(list_to_split: list, index: int) -> list:
    """Takes a list and an index and splits the list into two, then adds the first part to the end of the second part.

    Parameters:
        list_to_split(list): the list to be split and added.
        index(int): the index on which to split the list.

    Returns:
        list: a new list or the input list when the index is zero or not within the range of the list.

    Raises:
        AssertionError: when list_to_split is not a list.
        AssertionError: when the index is not an integer.

    >>> split_and_add([2, 5, 7, 9], 3)
    [9, 2, 5, 7]

    >>> split_and_add([9, "four", 3, 6, "you", "act", "rope"], -4)
    [6, 'you', 'act', 'rope', 9, 'four', 3]

    >>> split_and_add(["pit", "two", "boy", "mat", "three", "bloom"], 6)
    ['pit', 'two', 'boy', 'mat', 'three', 'bloom']

    >>> split_and_add(['at', '3', '6'], 0)
    ['at', '3', '6']
    """

    # input should be the correct datatype
    assert isinstance(index, int)
    assert isinstance(list_to_split, list)

    # returns the list when the index is zero, or not within the range of the list
    if (index == 0) or (index >= len(list_to_split)) or (index <= -len(list_to_split)):
        return list_to_split

    # split and add the list
    first_part = list_to_split[:index]
    second_part = list_to_split[index:]
    added_list = second_part + first_part

    return added_list
