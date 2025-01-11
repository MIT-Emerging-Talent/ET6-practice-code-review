#!/usr/bin/env python3
"""
Module to convert hexadecimal to decimal.

Author: Majd Abualsoud
"""


def hex_to_decimal(hex_value: str) -> int:
    """
    Converts a hexadecimal value to a decimal.

    Parameters:
        hex_value (str): The hexadecimal value to convert.

    Returns:
        int: The decimal equivalent of the hexadecimal value.

    Examples:
        >>> hex_to_decimal("1A")
        26
        >>> hex_to_decimal("FF")
        255
        >>> hex_to_decimal("0")
        0
    """
    # Ensure the hex_value is a valid hexadecimal string
    assert isinstance(hex_value, str), "Input must be a string"
    assert all(
        c in "0123456789ABCDEFabcdef" for c in hex_value
    ), "Invalid hexadecimal character"
    # Convert hexadecimal to decimal
    return int(hex_value, 16)
