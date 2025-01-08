"""
This module provides a function to find the largest number in a list of integers.
"""

from typing import List


def find_largest_number(numbers: List[int]) -> int:
    """
    Returns the largest number in a list.

    Args:
        numbers (List[int]): A non-empty list of integers.

    Returns:
        int: The largest number in the list.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")
    return max(numbers)


if __name__ == "__main__":
    # Simple test cases
    assert find_largest_number([3, 1, 7, 0, 5]) == 7
    assert find_largest_number([-10, -20, -3, -50]) == -3
    assert find_largest_number([0, 0, 0, 0]) == 0
    assert find_largest_number([1, -1, 3, -5, 2]) == 3
    assert find_largest_number([5]) == 5

    print("All tests passed!")
