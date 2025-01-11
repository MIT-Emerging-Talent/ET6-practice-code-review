#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting a non-negative integer to its binary representation.

Created on 9 1 2025
@author: Dadi Ishimwe
"""


def int_to_binary(number: int) -> str:
    """Convert a non-negative integer to its binary representation.

    Parameters:
        number: int, The number to convert to binary, greater than or equal to zero.

    Returns -> str, the binary representation of the number as a string.

    Raises:
        AssertionError: if the argument is not an integer.
        ValueError: if the argument is less than 0.

    >>> int_to_binary(0)
    '0'

    >>> int_to_binary(1)
    '1'

    >>> int_to_binary(2)
    '10'

    >>> int_to_binary(10)
    '1010'

    >>> int_to_binary(42)
    '101010'
    """
    # Validate the input data type
    assert isinstance(number, int)

    # Validate input as binary representation is not defined for negative integers
    if number < 0:
        raise ValueError("The number should be greater or equal to zero")

    # Handle edge case: binary representation of 0
    if number == 0:
        return "0"

    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2

    return binary
