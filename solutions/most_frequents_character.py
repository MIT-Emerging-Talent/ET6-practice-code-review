#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the most frequent character in a string.

Module contents:
    - most_frequent_character: Returns the character that appears most frequently in a string.

Created on 2025-01-03
Author: Ava Abdullah
"""


def most_frequent_character(text: str) -> str:
    """Finds the character that appears most frequently in a string.

    Accepts a string and returns the most frequent character,
    If multiple characters have the same highest frequency, returns the first one.
    Spaces and special characters are considered valid, and the check is case-sensitive.

    Parameters:
      text: str, the input string to check

    Returns -> max_char: str, the character with the highest frequency.

    Raises:
      AssertionError: if the argument is not a string or is empty

    Examples:
      >>> most_frequent_character("aabbccc")
      'c'
      >>> most_frequent_character("bbbccaaa")
      'b'
      >>> most_frequent_character("a b c") #Should return space
      ' '
      >>> most_frequent_character("xx!!!")
      '!'
    """
    assert isinstance(text, str), "Input must be a string"
    assert len(text) > 0, "Input string must not be empty"

    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    max_char = max(char_count, key=lambda char: (char_count[char], -text.index(char)))
    return max_char
