"""Module for merging even numbers from first list and odd numbers from second list.
Given two lists, this module combines even numbers from the first list and odd numbers from the second list.

@author: MUSABKAYMAK
@created: 01/05/2025
"""


def merge_even_odd_lists(list1: list[int], list2: list[int]) -> list[int]:
    """Merge even numbers from first list and odd numbers from second list.

    Parameters:
        list1 (list[int]): First list of integers to extract even numbers from
        list2 (list[int]): Second list of integers to extract odd numbers from

    Returns:
        list[int]: A new list containing even numbers from list1 and odd numbers from list2

    Raises:
        TypeError: If either parameter is not a list
        TypeError: If any item in either list is not an integer

    Examples:
        >>> merge_even_odd_lists([4, 16, 7, 26, 34, 7], [6, 13, 23, 18, 45])
        [4, 16, 26, 34, 13, 23, 45]
        >>> merge_even_odd_lists([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
        [2, 4, 6, 1, 3, 5]
        >>> merge_even_odd_lists([1, 3, 5], [2, 4, 6])
        []
        >>> merge_even_odd_lists([], [])
        []
    """
    # Validate parameter types
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both parameters must be lists")

    # Validate all items in the lists are integers
    if not all(isinstance(x, int) for x in list1 + list2):
        raise TypeError("All items must be integers")

    # Extract even numbers from first list
    even_numbers = []
    for num in list1:
        if num % 2 == 0:
            even_numbers.append(num)

    # Extract odd numbers from second list
    odd_numbers = []
    for num in list2:
        if num % 2 != 0:
            odd_numbers.append(num)

    # Combine and Return the results
    return even_numbers + odd_numbers
