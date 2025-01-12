
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting characters in a string.

Module contents: Takes a string as input and returns a dictionary with character counts.

Created on 2025-01-12

@author: Karina
"""

def count_characters(input_string: str) -> dict:
    """Count the occurrences of each character in a string.

    Parameters:
    input_string (str): The string to analyze

    Returns:
    dict: A dictionary with characters as keys and their counts as values

    Raises:
    AssertionError: If the input is not a string

    Examples:
    >>> count_characters('hello')
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    >>> count_characters('programming')
    {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
    >>> count_characters('aaa')
    {'a': 3}
    """
    # Input validation
    assert isinstance(input_string, str), "Input must be a string"

    # Create an empty dictionary to store character counts
    char_count = {}

    # Count each character
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
