#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for string function

Module contents:
    string: to return the item

Created on 03-01-2025
@author:Samir Ahmed Shaifta
"""


def is_in_list(item: str) -> bool:
    """
    Check if the given item is present in at least
    one of the two predefined lists.

    Parameters:
    item (str): The string to check for presence in the lists.

    Returns:
    bool: True if the item is in at least one of the lists, False otherwise.

    Examples:
    >>> is_in_list("apple")
    True
    >>> is_in_list("grape")
    True
    >>> is_in_list("mango")
    False
    """
    list1 = ["apple", "banana", "cherry"]
    list2 = ["grape", "orange", "kiwi"]

    return item in list1 or item in list2
