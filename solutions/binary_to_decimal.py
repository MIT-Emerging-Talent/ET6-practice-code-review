#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
created on 2025-12-29
@author:Alemayehu-Desta

"""


def binary_to_decimal(binary_str):
    """
    Converts a binary string to a decimal number.

    Args:
        binary_str (str): A string representing a binary number.

    Returns:
        int: The decimal equivalent of the binary number.

    Raises:
        ValueError: If the input string is empty or contains invalid characters.

    Examples:
        >>> binary_to_decimal("101")
        5
        >>> binary_to_decimal("")  # Raises ValueError: Input must not be empty.
        Traceback (most recent call last):
        ...
        ValueError: Input must not be empty.
        >>> binary_to_decimal("102")  # Raises ValueError: Input must only contain '0' and '1'.
        Traceback (most recent call last):
        ...
        ValueError: Input must only contain '0' and '1'.
    """
    if not binary_str:
        raise ValueError("Input must not be empty.")
    if any(c not in "01" for c in binary_str):
        raise ValueError("Input must only contain '0' and '1'.")
    return int(binary_str, 2)
