#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 04/01/2025
@author: Peter Ngugi

A module for converting integers to roman.

Module contents:
    - convert_int_to_roman: converts numbers from integer to roman.
"""


def convert_int_to_roman(num: int) -> str:
    """
    Converts an integer to its Roman numeral representation

    parameters:
        num (int): A non negative integer

    Returns:
        str: A string representing a roman numeral

    Raises:
        ValueError: If the input is not between 1 and 3999 inclusive.

    Examples:
    >>> convert_int_to_roman(5)
    "V"
    >>> convert_int_to_roman(100)
    "C"
    >>> convert_int_to_roman(33)
    "XXXIII"
    >>> convert_int_to_roman(1)
    "I"
    """
    if not (1 <= num <= 3999):
        raise ValueError("Input must be between 1 and 3999.")

    romans = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    r = ""
    values = sorted(romans.keys(), reverse=True)
    for n in values:
        while n <= num:
            r += romans[n]
            num -= n
    return r
