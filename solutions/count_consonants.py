#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the function `count_consonants` to count the number of consonants
in a given string. The function handles different character cases and ignores non-alphabetical characters.

Author: Norbert Ndayisenga
Date: 07 01 2024
"""


def count_consonants(s: str) -> int:
    """
    Counts the number of consonants in a given string, ignoring vowels, numbers, and symbols.

    Parameters:
        s (str): The input string to evaluate.

    Returns:
        int: The number of consonants in the input string.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> count_consonants("Hello, World!")
        7
        >>> count_consonants("123@#$")
        0
        >>> count_consonants("bcdfghjklmnpqrstvwxyz")
        21
    """
    # Ensure the input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Define consonants using a set for faster membership testing
    consonants = set("bcdfghjklmnpqrstvwxyz")

    # Count consonants in the string
    return sum(1 for char in s.lower() if char in consonants)
