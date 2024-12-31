#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def longest_substring(s: str) -> str:
    """
    Function to find the longest substring without repeating characters.

    Parameters:
    s (str): The input string.

    Returns:
    str: The longest substring without repeating characters.

    Raises:
        assertionError: If the input is not a string
        ValueError: If the input string is empty.

    Examples:

    >>> longest_substring("abcabcbb")
    'abc'
    >>> longest_substring("bbbbb")
    'b'
    >>> longest_substring("pwwekew")
    'wek'
    """
    assert isinstance(s, str), "Input must be a string"
    if not s:
        raise ValueError("Input string cannot be empty")

    longest = ""
    for i in range(len(s)):
        substring = ""
        for j in range(i, len(s)):
            if s[j] == " ":
                continue
            if s[j] in substring:
                break
            substring += s[j]
        if len(substring) > len(longest):
            longest = substring
    return longest
