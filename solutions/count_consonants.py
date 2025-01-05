#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 03 01 2024

@author: Norbert Ndayisenga
"""


def count_consonants(s: str) -> int:
    """
    Counts the number of consonants in a given string.

    Parameters:
        s (str): The input string.

    Returns:
        int: The number of consonants in the string.

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
