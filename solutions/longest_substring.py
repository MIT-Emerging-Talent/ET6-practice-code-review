#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating the longest substring

Module contents:
    longest_substring: generates the longest substring without
    repetition for a given string.

Created on 2025-01-05
@author: Hiba Daffallah
"""


def longest_substring(input_string: str) -> str:
    """
     Generates a string containing the longest substring without repitition
     from the input_string.

    Parameters:
        input_string: str

    Returns :
      substring: the longest substring

    Raises:
        AssertionError: if the argument is not a string

    >>> longest_substring('')
    ''
    >>> longest_substring('bbbbbb')
    'b'
    >>> longest_substring('abcdef')
    'abcdef'
    >>> longest_substring('pwwkew')
    'wke'
    >>> longest_substring('celelocceli')
    'eloc'
    """
    # Ensure the input is a string
    assert isinstance(input_string, str)

    n = len(input_string)
    # If the string is empty, return an empty string as the result
    if n == 0:
        return ""
    # Initialize a set to keep track of unique characters in the current substring
    sub = set()
    # Initialize the longest substring variable
    longest_sub = ""
    # Initialize the left pointer of the sliding window
    left = 0
    for right in range(n):
        # If the character at the right pointer is already in the set,
        # slide the left pointer to remove characters until the duplicate is removed
        while input_string[right] in sub:
            sub.remove(input_string[left])
            left += 1

        # Add the current character at the right pointer to the set
        sub.add(input_string[right])
        current_len = right - left + 1

        # If the current substring is longer than the previously recorded longest substring,
        # update the longest substring
        if current_len > len(longest_sub):
            longest_sub = input_string[left : right + 1]

    # Return the longest substring found
    return longest_sub
