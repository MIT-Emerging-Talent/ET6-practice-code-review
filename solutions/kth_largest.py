"""
Module for finding the kth largest element in a list.
This module provides a function to find the kth largest element in a list of strings,
where each string represents an integer without leading zeros.

Created: 04/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Ahd Abdelrahim
"""


def kth_largest(nums, k):
    """
    Return the string that represents the kth largest integer in nums.

    Parameters:
        nums (list): A list of strings where each string represents a positive integer.
        k (int): The position (1-indexed) of the largest element to find.

    Returns:
        str: The string representation of the kth largest integer in the list.

    Raises:
        ValueError: If any element in nums is not a valid integer string.
        IndexError: If k is less than 1 or greater than the length of nums.

    Examples:
    >>> kth_largest(["3", "2", "1", "5", "6", "4"], 2)
    '5'

    >>> kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 4)
    '4'

    >>> kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 9)
    '1'

    >>> kth_largest([], 1)
    Traceback (most recent call last):
    IndexError: k must be between 1 and the length of the list
    """

    # Ensure the requested position (k) is valid to avoid accessing elements
    # outside the list's bounds
    if not 1 <= k <= len(nums):
        raise IndexError("k must be between 1 and the length of the list")

    # Validate and convert the input list to integers for accurate comparison and sorting
    try:
        nums = sorted([int(num) for num in nums], reverse=True)
    except ValueError as exc:
        raise ValueError(
            "All elements in the list must be valid integers as strings."
        ) from exc

    # Sorting in descending order simplifies finding the kth largest element by its position
    # Convert the result back to a string to match the input format
    return str(nums[k - 1])
