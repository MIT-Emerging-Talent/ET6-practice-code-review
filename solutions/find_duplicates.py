#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding duplicate elements in a list.

Module contents:
    - find_duplicates: identifies duplicate items in a list.

Created on 2025-01-08
@author: Karina
"""

from collections import Counter

def find_duplicates(items: list) -> list:
    """
    Find duplicate items in a list.

    Parameters:
        items: list, the input list to search for duplicates

    Returns:
        list: a list of items that appear more than once in the input list,
              in order of their first appearance.

    Raises:
        TypeError: if the input is not a list

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
    if not isinstance(items, list):
        raise TypeError("Input must be a list")

    # Count occurrences of each item
    counts = Counter(items)
    
    # Filter items that appear more than once in order of first appearance
    duplicates = [item for item in items if counts[item] > 1]

    # Return unique duplicates preserving the order
    return list(dict.fromkeys(duplicates))


if __name__ == "__main__":
    # Example usage
    examples = [
        [1, 2, 2, 3, 3, 3],
        ['a', 'b', 'a', 'c', 'b'],
        [1, 2, 3, 4],
        [],
        ['hello', 'world', 'hello']
    ]

    for example in examples:
        print(f"Input: {example}")
        print(f"Duplicates: {find_duplicates(example)}")
        print()
