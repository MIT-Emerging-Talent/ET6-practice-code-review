#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

A module that determines which number is missing out of a list.

Module contents:
    - missing_number: finds the missing number from a list.

created on 04/01/2025
@author: Alaa Mohamed

"""


def missing_number(nums: list, n: int) -> int:
    """Finds the missing numbers out of a list.

    Parameters:
        nums: list, starting with zero and of any length
        n: int, greater than or equal to zero

    Returns:
        list: with the missing numbers.

    Raises:
        AssertionError: if one of the arguments is invalid.

    Examples:
    >>> missing_number([0,2], 3)
    [1]
    >>> missing_number([0,1,3], 5)
    [2,4]

    """
    # the nums length should be an integer greater than 0
    assert n >= 0, "n must be greater than or equal to zero"

    full_set = set(range(n + 1))
    # The expected set of numbers is from 0 to n

    nums_set = set(nums)
    # The actual set of numbers present in the 'nums' list

    missing = list(full_set - nums_set)
    # The missing numbers are the difference between the full set and the actual set

    return missing
