#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting integers to Roman numerals.

Created on Jan 4, 2025
@author: Dadi Ishimwe
"""

def int_to_roman(num: int) -> str:
    """
    Converts an integer to its Roman numeral representation.

    Args:
        num (int): The integer to convert. Must be between 1 and 3999.
    
    Returns:
        str: The Roman numeral representation of the integer.
    
    Raises:
        AssertionError: If the input is not a valid integer or out of range.

    >>> int_to_roman(3)
    'III'
    >>> int_to_roman(9)
    'IX'
    >>> int_to_roman(58)
    'LVIII'
    """
    assert isinstance(num, int) and 1 <= num <= 3999, "Number must be between 1 and 3999."
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ""
    for i, v in enumerate(val):
        while num >= v:
            roman += syms[i]
            num -= v
    return roman
