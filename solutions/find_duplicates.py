#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Key Implementation Features of find_duplicates.py:

1. Type Hints and Documentation:
   - Clear parameter and return type annotations
   - Comprehensive docstring with examples
   - Explicit error conditions

2. Data Structure Usage:
   - Uses dictionary (seen_count) for O(1) lookups
   - Uses list (first_seen) to maintain order
   - Uses hashable conversion for nested lists

3. Algorithm Efficiency:
   - Single pass to track counts
   - Preserves order of first appearance
   - Handles duplicate detection without sorting

4. Error Handling:
   - Input validation with assertions
   - Clear error messages
   - Robust handling of nested structures

5. Edge Cases:
   - Empty list handling
   - Mixed type support
   - Nested list support
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