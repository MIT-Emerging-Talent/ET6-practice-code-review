#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A function to convert decimal numbers to binary.

Created on 1/1/2025
@author: Heba Shaheen
"""


def decimal_to_binary(decimal_input: int) -> str:
    """Give the binary number for a decimal

    Args:
        decimal_input (int): Decimal number to be converted

    Returns:
        str: Binary representation of the decimal number

    Raises:
        AssertionError: if the input is not an integer

    >>> decimal_to_binary(10)
    "1010"

    >>> decimal_to_binary(20)
    "10100"

    >>> decimal_to_binary(255)
    "11111111"
    """
    # Handle the edge case for 0
    assert isinstance(decimal_input, int), "The input should be integer"
    assert decimal_input >= 0, "Give a positive input"
    if decimal_input == 0:
        return "0"
    binary = ""
    while decimal_input > 0:
        binary = str(decimal_input % 2) + binary
        decimal_input //= 2
    return binary
