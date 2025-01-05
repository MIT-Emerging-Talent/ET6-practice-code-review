#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for finding the most frequent character in a string.

Module contents:
    - most_frequent_character: takes a string as an argument and returns the most frequent character.

Created on 04 01 25
@author: Mohamad Ziadah
"""


def most_frequent_character(s: str) -> str:
    """
    Finds the most frequent character in a string.

    Parameters:
        s (str): The input string to find the most frequent character from.

    Returns:
        str: The most frequent character in the string.

    Raises:
        AssertionError: If the input is not a string.

    >>> most_frequent_character("abracadabra")
    'a'
    >>> most_frequent_character("aabbcc")
    'a'
    >>> most_frequent_character("Hello, World!")
    'l'

    """
    assert isinstance(s, str), "Input must be a string"

    # If the string is empty, return None
    if not s:
        return None

    # Remove spaces and convert to lowercase for accurate comparison
    s = s.replace(" ", "").lower()

    # Create a dictionary to store character counts
    char_count = {}

    # Count the frequency of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the character with the maximum frequency
    most_frequent = max(char_count, key=char_count.get)

    return most_frequent
