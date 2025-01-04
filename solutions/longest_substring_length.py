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
        s: str, the input string for which to find the longest substring

    Returns -> int, the length of the longest substring without repeating characters

    Raises:
        AssertionError: if s is not a string

    >>> longest_substring_length("abcabcbb")
    3

    >>> longest_substring_length("abcdef")
    6

    >>> longest_substring_length("aaaaaa")
    1
    """

    assert isinstance(s, str), "s input should be a string"

    longest = 0
    current = ""

    for char in s:
        if char in current:
            # Remove repeating characters from the substring
            while char in current:
                current = current[1:]

        current += char
        longest = max(longest, len(current))

    return longest
