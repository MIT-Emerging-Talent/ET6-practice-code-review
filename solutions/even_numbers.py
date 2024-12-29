#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-12-28

@author: Mykyta Kondratiev
"""


def all_even(numbers: list) -> bool:
    """
    All_even function checks if all numbers in a list are even.

    Input: numbers[list]

    Return: result[bool] True if all numbers are even, False otherwise

    >>> all_even([])
    True

    >>> all_even([2, 4, 6])
    True

    >>> all_even([2, 3, 6])
    False

    >>> all_even([0, -2, 8])
    True

    >>> all_even([1])
    False
    """
    # Check if input is a list
    assert isinstance(numbers, list), "Input should be a list"

    # Check if all elements are even
    return all(num % 2 == 0 for num in numbers)
