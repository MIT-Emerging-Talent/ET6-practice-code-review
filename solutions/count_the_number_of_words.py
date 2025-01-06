#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for counting the number of words in a string.

Module contents:
    - word_count_function: takes a string as an argument and returns the number of words.

Created on 06/01/2025
@author: Mohamad Ziadah
"""


def word_count_function(s: str) -> int:
    """
    Counts the number of words in a string.

    Parameters:
        s (str): The input string to count words from.

    Returns:
        int: The number of words in the string.

    Raises:
        AssertionError: If the input is not a string.

    >>> word_count_function("The quick brown fox jumps over the lazy dog")
    9
    >>> word_count_function("")
    0
    >>> word_count_function("   leading and trailing spaces   ")
    4
    >>> word_count_function("word1\tword2\nword3  word4")
    4

    """
    assert isinstance(s, str), "Input must be a string"

    # Filter out non-alphanumeric characters and split the string by whitespace
    words = [word for word in s.split() if word.isalnum()]

    # Return the count of words
    return len(words)
