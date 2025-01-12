#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module to find the length of the longest substring in a given string without repeating characters.

Module Contents:

    - longest_substring_length(s: str) -> int:
    Finds the length of the longest substring without repeating characters.

Created on: 2025-01-03
Author: Jola-Moses
"""


def longest_substring_length(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.

    Parameters:
        s (str): The input string for which to find the longest substring.
                An empty string is valid input.

    Returns:
        int: A non-negative integer representing the length of the longest substring
            without repeating characters.

    Raises:
        AssertionError: If `s` is not a string.

    Examples:
        >>> longest_substring_length("abcabcbb")
        3
        >>> longest_substring_length("abcdef")
        6
        >>> longest_substring_length("aaaaaa")
        1
        >>> longest_substring_length("")
        0
    """

    assert isinstance(s, str), "Input should be a string"

    max_length = 0
    current_substring = ""

    for char in s:
        if char in current_substring:
            # Remove repeating characters
            while char in current_substring:
                current_substring = current_substring[1:]

        # Add the current character to the substring
        current_substring += char

        # Update max_length
        max_length = max(max_length, len(current_substring))

    return max_length
