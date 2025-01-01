#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting a decimal number to a specified base.

Module contents:
    - decimal_to_base: generates the base representation of a decimal number.


Created on Dec 30, 2024.
@author: AL-HASSEN SABEEH
"""

dec = {
    0: "0",
    1: "1",
    2: ("2", "b"),
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: ("8", "o"),
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
    16: ("", "x"),
}


def decimal_to_base(decimal: int, base: int) -> str:
    """The function converts a decimal number to a string in a specified
    base with appropriate prefixes (0b, 0c, 0x).

    Parameters:
        decimal: int, greater than or equal to zero
        base: int, must be 2, 8, or 16

    Returns -> string, base representation (binary, octal, or hexadecimal)

    Raises:
        AssertionError: if either argument is not an integer
        AssertionError: if the first argument is negative
        AssertionError: if the second argument is not 2, 8, or 16



    >>> decimal_to_base(2796202,2)
    '0b1010101010101010101010'

    >>> decimal_to_base(342391,8)
    '0o1234567'

    >>> decimal_to_base(12648430,16)
    '0xc0ffee'
    """
    # The decimal number and base should be an integer
    assert isinstance(decimal, int), "decimal number is not an integer"
    assert isinstance(base, int), "base number is not an integer"
    # The decimal number must be greater than 0, and base 2 or 8 or 16
    assert decimal >= 0, "decimal number is less than 0"
    assert base in {2, 8, 16}, "Base must be 2, 8, or 16"
    # Implementation of the strategy using recursion
    if decimal // base == 0:
        # Base case f(n)="n" for n < b, n is decimal , b is base
        return "0" + dec[base][1] + dec[decimal][0]
    # Recursive case 𝑓(𝑛)=𝑓(𝑛//b)+str(𝑛 mod  b) for 𝑛>b-1
    #       /Recursive Case/  /Reduction Step/    /Concatenating Result/
    return decimal_to_base(decimal // base, base) + dec[decimal % base][0]
