#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding duplicate elements in a list.

Module contents:
    - find_duplicates: identifies duplicate items in a list.

Created on 2025-01-08
@author: AI Developer
"""


def find_duplicates(items: list) -> list:
    """
    Find duplicate items in a list.

    Parameters:
        items: list, the input list to search for duplicates

    Returns:
        list: a list of items that appear more than once in the input list,
              in order of their first appearance

    Raises:
        AssertionError: if the input is not a list

    Examples:
        >>> find_duplicates([1, 2, 2, 3, 3, 3])
        [2, 3]
        >>> find_duplicates(['a', 'b', 'a', 'c', 'b'])
        ['a', 'b']
        >>> find_duplicates([1, 2, 3, 4])
        []
        >>> find_duplicates([])
        []
        >>> find_duplicates(['hello', 'world', 'hello'])
        ['hello']
    """
    # Input validation
    assert isinstance(items, list), "Input must be a list"

    # Function to convert item to hashable type if needed
    def to_hashable(item):
        return tuple(item) if isinstance(item, list) else item

    # Track both counts and first appearances
    seen_count = {}  # Track count of items
    first_seen = []  # Track order of first appearance
    duplicates = []  # Store duplicates in order

    # First pass: Track counts and first appearances
    for item in items:
        hashable_item = to_hashable(item)
        if hashable_item not in seen_count:
            seen_count[hashable_item] = 1
            first_seen.append(item)  # Keep track of order
        else:
            seen_count[hashable_item] += 1
            if seen_count[hashable_item] == 2:  # Only add when we see it second time
                duplicates.append(item)

    # Return duplicates in order of first appearance
    ordered_duplicates = []
    for item in first_seen:
        hashable_item = to_hashable(item)
        if seen_count[hashable_item] > 1 and item not in ordered_duplicates:
            ordered_duplicates.append(item)

    return ordered_duplicates
