#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting numbers between different bases
(binary, octal, decimal, and hexadecimal).

Module contents:
    - base_to_base: Converts a number from one base (binary, octal, decimal,
    or hexadecimal) to another base.


Team Number: 28
Team Name: MIT Alpha
Created on Jan 4, 2025.
@author: AL-HASSEN SABEEH
"""

from typing import Union
from .base_to_decimal import base_to_decimal
from .decimal_to_base import decimal_to_base


def base_to_base(number: Union[str, int], target_base: int) -> Union[str, int]:
    """
    Converts a number from one base (binary, decimal, octal, or hexadecimal) to another base.

    Args:
        number (Union[str, int]): The number in the original base, which can be provided as
                            a string (e.g., "0b111" for binary, "0o10" for octal, "0x1F" for
                            hexadecimal) or as an integer (for decimal input).

        target_base (int): The base to convert to (e.g., 10 for decimal, 8 for octal,
                            2 for binary, 16 for hexadecimal).

    Returns:
        Union[str, int]: The number in the target base. If the target base is decimal (10),
                            the output will be an integer; otherwise, the output will be
                            a string in the corresponding base.

    Raises:
        AssertionError: if the argument is not a string or int
        AssertionError: if the string is empty
        AssertionError: if the string contains characters other than
        '0' or '1' (for binary), '0' to '7' (for octal), or '0' to '9'
        and 'a' to 'f' (for hexadecimal)

    >>> base_to_base('0b101', 8)
    '0o5'

    >>> base_to_base('0o5', 16)
    '0x5'

    >>> base_to_base('0x5', 10)
    5

    >>> base_to_base(5, 2)
    '0b101'

    """
    # All assertion errors will be arise by helper functions
    if target_base == 10:
        return base_to_decimal(number)

    if isinstance(number, int):  # no need to call base to decimal
        return decimal_to_base(number, target_base)

    # first convert the origin base to decimal
    return decimal_to_base(base_to_decimal(number), target_base)
