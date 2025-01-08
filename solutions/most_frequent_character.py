#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for finding the most frequent character in a string.

Module contents:
- most_frequent_character: accepts a string and returns its most frequent character.

Created on 08/01/2025
@author: Mohamad Ziadah
"""


def most_frequent_character(string: str) -> str:
    """
    Finds the most frequent character in a string.

    Parameters:
        string (str): The input string to find the most frequent character from.

    Returns:
        str: The most frequent character in the string.
             If the string is empty, None is returned.
             If there are multiple characters with the same frequency,
             the first one encountered is returned.

    Raises:
        AssertionError: If the input is not a string.

    Assumptions:
        - The input string may contain alphanumeric characters and special symbols.
        - Spaces are ignored, and the comparison is case-insensitive.

    Examples:
        >>> most_frequent_character("abracadabra")
        'a'
        >>> most_frequent_character("aabbcc")
        'a'
        >>> most_frequent_character("Hello, World!")
        'l'
        >>> most_frequent_character("") is None
        True
    """
    assert isinstance(string, str), "Input must be a string"

    # Handle edge case: ensure empty input is identified early to avoid unnecessary processing
    if not string:
        return None

    # Standardize the input for consistent comparison of character frequencies
    string = "".join(char for char in string if char.isalnum()).lower()

    # Track the frequency of each character in the input
    char_count = {}

    # Build frequency counts by traversing each character in the string
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Determine the most frequent character by identifying the maximum frequency
    most_frequent = max(char_count, key=char_count.get)

    return most_frequent
