#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module to find the length of the longest substring in a given string without repeating characters.

Module Contents:

    - length_longest_substring(s: str) -> int:
    Finds the length of the longest substring without repeating characters.

Created on: 2025-01-03
Author: Jola-Moses
"""
def length_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.

    Parameters:
        s: str, the input string for which to find the longest substring

    Returns -> int, the length of the longest substring without repeating characters

    Raises:
        AssertionError: if s is not a string

    >>> length_longest_substring("abcabcbb")
    3
    
    >>> length_longest_substring("abcdef")
    6
    
    >>> length_longest_substring("aaaaaa")
    1
    """

    # Track the length of the longest substring without repeating characters
    longest = 0

    # Store the substring being evaluated
    current = ""

    # Iterate through each character to find substrings
    for char in s:
        if char in current:
            # Remove characters until the repeating one is eliminated
            while char in current:
                current = current[1:]

    current += char  # Expand the substring with the current character
