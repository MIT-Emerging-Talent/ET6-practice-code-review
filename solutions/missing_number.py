"""
A module to find the missing number from a range of numbers.

Module contents:
    - find_missing_number: returns the missing number from the given array.

Created on 11th Jan 2025
@author: muqaddas96
"""


def missing_number(nums: list[int]) -> int:
    """Find the missing number from an array of distinct integers.

    Parameters:
        nums (list[int]): List of integers from the range 0 to n.

    Returns:
        int: The missing number.

    Raises:
        AssertionError: If nums is not a list or contains invalid values.

    Examples:
    >>> find_missing_number([3, 0, 1])
    2
    >>> find_missing_number([0, 1])
    2
    >>> find_missing_number([9,6,4,2,3,5,7,0,1])
    8
    >>> find_missing_number([0])
    1
    """
    assert isinstance(nums, list), "Input must be a list."
    assert all(isinstance(num, int) for num in nums), "List elements must be integers."
    assert len(nums) == len(set(nums)), "List must contain distinct integers."

    n = len(nums)
    expected_sum = n * (n + 1) // 2  # Sum of 0 to n
    actual_sum = sum(nums)
    return expected_sum - actual_sum
