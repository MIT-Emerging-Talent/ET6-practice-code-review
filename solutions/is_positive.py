#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

A module for checking if an integer is positive.

@author: Luyando .E. Chitindi
"""


def is_positive(number: int) -> bool:
    """
    This checks if an integer is positive.

    Parameters:
    number: int, the number to check

    Returns -> bool:
        True if the number is positive, false otherwise.

    Raises:
        AssertionError: if the input is not an integer

    Example:
    >>> is_positive(4)
    True
    >>> is_positive(-3)
    False
    >>> is_positive(0)
    False
    >>> is_positive("hello")
    Traceback (most recent call last):
        ...
    AssertionError: Input must be an integer.
    """
    assert isinstance(number, int), "Input must be an integer"
    return number > 0
