"""
A module for finding duplicate elements in a list while preserving order.

Module contents:
    - find_duplicates: identifies duplicate items in a list while maintaining
      the order of first appearance.

Created on 2025-01-12
@author: Karina
"""


def to_hashable(item):
    """Convert an item to a hashable type if needed.

    Parameters:
        item: any Python object to be converted

    Returns:
        A hashable version of the input item
    """
    return tuple(item) if isinstance(item, list) else item


def find_duplicates(items: list) -> list:
    """Find duplicate items in a list while preserving order of first appearance.

    This function identifies elements that appear more than once in the input list
    and returns them in the order of their first appearance. It supports various
    data types including numbers, strings, and nested lists.

    Parameters:
        items: list
            The input list to search for duplicates. Can contain elements of
            any hashable type or lists.

    Returns:
        list: A list of items that appear more than once in the input list,
              in order of their first appearance.

    Raises:
        AssertionError: If the input is not a list.

    Examples:
        >>> find_duplicates([1, 2, 2, 3, 3, 3])
        [2, 3]
        >>> find_duplicates(['a', 'b', 'a', 'c', 'b'])
        ['a', 'b']
        >>> find_duplicates([1, 2, 3, 4])
        []
        >>> find_duplicates([])
        []
        >>> find_duplicates([[1], [2], [1], [3]])
        [[1]]
    """
    # Input validation
    assert isinstance(items, list), "Input must be a list"

    # Track counts and order
    seen = {}  # Dictionary to track count and first position of each item
    first_occurrences = []  # List to track first appearances in order
    duplicates = []  # List to store duplicates in order of first appearance

    # Process each item to track first occurrences
    for i, item in enumerate(items):
        # Convert lists to tuples for hashing
        hashable_item = tuple(item) if isinstance(item, list) else item

        if hashable_item not in seen:
            seen[hashable_item] = {'count': 1, 'first_pos': i}
            first_occurrences.append((item, i))  # Track item and its position
        else:
            seen[hashable_item]['count'] += 1
            # Add to duplicates only on second occurrence
            if seen[hashable_item]['count'] == 2:
                duplicates.append((item, seen[hashable_item]['first_pos']))

    # Sort duplicates by their first occurrence position
    duplicates.sort(key=lambda x: x[1])

    # Return only the items, maintaining their order of first appearance
    return [item for item, _ in duplicates]
