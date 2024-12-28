#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting a binary string to a decimal number.

Module contents:
    - binary_to_decimal: generates the decimal representation of a binary string.

Created on Dec 28, 2024.
@author: AL-HASSEN SABEEH
"""


def binary_to_decimal(binary: str) -> int:
    """
    Converts a binary string to its decimal representation.

    Parameters:
        binary: string, containing only '0' or '1' characters

    Returns -> int, represent the decimal value of a binary string

    Raises:
        AssertionError: if the argument is not a string
        AssertionError: if it contains characters other than '0' or '1'

    >>> binary_to_decimal('100')
    4

    >>> binary_to_decimal('1000')
    8

    >>> binary_to_decimal('111')
    7

    >>> binary_to_decimal('1010101010101010101010')
    2796202
    """
    # The binary input should be a string containing only '0' or '1' characters
    assert isinstance(binary, str), "Binary is not a string"
    assert set(binary) <= {"0", "1"}, "Binary string contains invalid characters"
    # The strategy recursively converts a binary string to its decimal value
    # by processing each digit and reducing the string until empty
    if len(binary) == 0:
        # Base Case,  f(ϵ)=0
        return 0
    # Recursive Case, f(b1b2…bn) = b1 . 2^(n−1) + f(b2b3…b<n-1>)
    #      /Return Step/                         /Recursive Case/ /Reduction Step/
    return int(binary[0]) * 2 ** (len(binary) - 1) + binary_to_decimal(binary[1:])
