#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the length of the longest substring without repeating characters.

Module contents:
    - longest_substring(s): Function to determine the length of the longest substring without repeating characters.

Created on 2025-01-07
@author: Gennadii Ershov
"""


def longest_substring(s: str) -> int:
    """
    Determines the length of the longest substring without repeating characters.

    Args:
        s (str): The input string to be evaluated. Must have a length between 0 and 5 * 10^4.
                 The string consists of English letters, digits, symbols, and spaces.

    Returns:
        int: The length of the longest substring without repeating characters. Returns 0 if the input string is empty.

    Examples:
        >>> longest_substring("abcabcbb")
        3

        >>> longest_substring("bbbbb")
        1

        >>> longest_substring("pwwkew")
        3

        >>> longest_substring("")
        0
    """
    seen = set()

    for start in range(len(s)):
        for end in range(start, len(s)):
            substring = s[start : end + 1]

            # Check if the substring has unique characters
            if substring not in seen and len(substring) == len(set(substring)):
                seen.add(substring)

    # Return the length of the longest non-repeating substring
    return max((len(i) for i in seen), default=0)
