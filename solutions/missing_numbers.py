#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module that returns a sorted list of all the missing numbers in a string containing integers separated by spaces.

Module contents:
    - missing_numbers: creates a list with all the missing integers.

Created on 06/01/2025
@author: Amin
"""


def missing_numbers(nums_string: str) -> list:
    """Find the missing numbers in a list of integers.

    Parameters:
        nums_string: string, the input string containing the integers to be checked

    Returns -> list: the list of the missing integers in the input string
    Raises:
        AssertionError: if the argument is not a list of integers
    >>> missing_numbers("0 1")
    []
    >>> missing_numbers("0 2 3")
    [1]
    >>> missing_numbers("0    4")
    [1, 2, 3]
    >>> missing_numbers("3 1 7")
    [2, 4, 5, 6]
    """
    assert isinstance(
        nums_string, str
    ), "input must be a string containing integers separated by spaces"
    # Transform the original numbers string into a list by splitting it
    nums_list = nums_string.split()
    nums = []
    # Transform each element of the list from str into an integer
    for i in nums_list:
        try:
            num = int(i)
            nums.append(num)

        except:
            return "The input contains non-integer values"
    miss = []
    # Identify the maximal number in the list
    maximum = nums[0]
    for i in nums:
        if i > maximum:
            maximum = i
    # Identify the minimal number in the list
    minimum = nums[0]
    for i in nums:
        if i < minimum:
            minimum = i
    for num in range(minimum + 1, maximum):
        if num not in nums:
            miss.append(num)
    return miss
