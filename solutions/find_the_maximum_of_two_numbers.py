#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the maximum of two numbers.

Module contents:
    -find_the_max

Created on 2025-01-06
@author: Ajanduna Emmanuel
"""


def find_the_maximum_of_two_numbers(num1, num2):
    """
    This function finds the maximum of two given numbers.

    Args:
      num1: The first number.
      num2: The second number.

    Returns:
      The maximum of num1 and num2.
    """
    if num1 > num2:
        return num1
    else:
        return num2


# Test cases
print(find_the_maximum_of_two_numbers(5, 3))
# Output: 5
print(find_the_maximum_of_two_numbers(2, 8))
# Output: 8
print(find_the_maximum_of_two_numbers(7, 7))
# Output: 7
