#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

A module for checking to see if an integer is even.

@author: Luyando .E. Chitindi
"""


def is_even(number: int) -> bool:
    """
    This checks if an integer is even.

    Parameters:
    number: int, the number to check

    Returns -> bool:
        True if the number is even, false otherwise.

    Raises:
        AssertionError: if the input is not an integer

    Example:
    >>> is_even(4)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
     >>> is_even("hello")
    Traceback (most recent call last):
        ...
    AssertionError: Input must be an integer.
    """
    assert isinstance(number, int), "Input must be an integer"
    if number % 2 == 0:
        return True
    return False
