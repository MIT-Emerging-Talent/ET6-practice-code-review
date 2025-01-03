#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting a base string (binary, octal, or hexadecimal)
to a decimal number.

Module contents:
    - base_to_decimal: Converts a base string (binary, octal, or hexadecimal)
    to its decimal representation.

Team Number: 28
Team Name: MIT Alpha
Created on Jan 2, 2025.
@author: AL-HASSEN SABEEH
"""

digit = {
    "0": 0,
    "1": 1,
    "2": 2,
    "0b": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "0o": 8,
    "9": 9,
    "a": 10,
    "A": 10,
    "b": 11,
    "B": 11,
    "c": 12,
    "C": 12,
    "d": 13,
    "D": 13,
    "e": 14,
    "E": 14,
    "f": 15,
    "F": 15,
    "0x": 16,
}


def base_to_decimal(base: str) -> int:
    """
    Converts a base string (binary, octal, or hexadecimal) to its decimal
    representation.




    Parameters:
        base: string, containing valid characters for binary ('0' or '1'),
        octal ('0' to '7'), or hexadecimal ('0' to '9' and 'a' to 'f').



    Returns -> int, representing the decimal value of the base string.


    Raises:
        AssertionError: if the argument is not a string
        AssertionError: if the string is empty
        AssertionError: if the string contains characters other than
        '0' or '1' (for binary), '0' to '7' (for octal), or '0' to '9'
        and 'a' to 'f' (for hexadecimal)

    >>> base_to_decimal('0b101')
    5

    >>> base_to_decimal('0o17')
    15

    >>> base_to_decimal('0x1A')
    26

    >>> base_to_decimal(bin(2796202))
    2796202
    """
    # Ensure correct input
    assert isinstance(base, str), "Base must be a string"
    assert len(base) >= 3, "Base must not be empty."
    assert (
        (base.startswith("0b") and all(c in "01" for c in base[2:]))
        or (base.startswith("0o") and all(c in "01234567" for c in base[2:]))
        or (
            base.startswith("0x")
            and all(c in "0123456789abcdefABCDEF" for c in base[2:])
        )
    ), "Argument must start with '0b', '0o', or '0x' followed by valid digits."

    if len(base) == 3:
        # Base Case,  f("0xm")=m, f("0cm")=m, f("0bm")=m, m is a digit
        return digit[base[2]]

    # Recursive Case, f(b1b2…bn) = b1 . base^(n−3) + f(b2b3…b<n-4>)
    #      /Return Step/   b1 . base^(n−3)
    decimal = digit[base[2]] * digit[base[0:2]] ** (len(base) - 3)
    #               f(b2b3…b<n-4>)    /Reduction Step/
    return decimal + base_to_decimal(base[0:2] + base[3:])
