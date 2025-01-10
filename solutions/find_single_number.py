"""
Module: single_number

Author: Mudassra Taskeen
Date: 2025-01-07

This module provides a function to find the single number in a list where all other numbers appear twice.
"""

def find_single_number(nums: list[int]) -> int:
    """
    Returns the number that appears only once in the list, where all other numbers appear twice.

    Parameters:
        nums (list[int]): A list of integers where every element appears twice except for one.

    Returns:
        int: The single number that appears only once.

    Assumptions:
        - The input is always a list of integers.

    Examples:
        >>> find_single_number([2, 2, 1])
        1

        >>> find_single_number([4, 1, 2, 1, 2])
        4

        >>> find_single_number([1])
        1

    Example:
        nums = [4, 1, 2, 1, 2]
        print(find_single_number(nums))
        # Output: 4

    Defensive Assertions:
        - Ensures the input is a list of integers.
    """
    assert isinstance(nums, list), "Input must be a list"
    assert all(isinstance(i, int) for i in nums), "All elements in the list must be integers"

    result = 0
    for num in nums:
        result ^= num  # XOR operation, all duplicate numbers cancel out

    return result
