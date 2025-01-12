#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
A module for Returns the longest word in the given sentence.

Module contents:
   This module contains a function `longest_word`
   that takes a sentence and returns the longest word in it.
   It handles edge cases such as empty strings, non-string inputs, and punctuation.

Author: Özgür Özbek
Date: 11th January 2025
Group: ET6-foundations-group-16
"""

import string


def longest_word(sentence: str) -> str:
    """
    Returns the longest word in the given sentence, ignoring punctuation.

    Args:
        sentence (str): A sentence from which to find the longest word.

    Returns:
        str: The longest word in the sentence. If there are multiple longest words,
             the first one encountered is returned.

    Raises:
        AssertionError: If the input is not a string or if the string is empty.

    Example:
        >>> longest_word("I love programming with Python")
        'programming'

        >>> longest_word("apple banana cherry!")
        'banana'

        >>> longest_word("Hello, world!")
        'Hello'

    """
    # Defensive assertion to check if the sentence is a non-empty string
    assert isinstance(sentence, str), "Input must be a string."
    assert sentence, "Input string must not be empty."

    # Split the sentence into words based on spaces
    words = sentence.split()

    # Initialize the variable to store the longest word
    longest = ""

    # Iterate through each word in the list
    for word in words:
        # Remove punctuation from the start and end of the word
        word = word.strip(string.punctuation)

        # Check if the current word is longer than the longest found so far
        if len(word) > len(longest):
            longest = word

    return longest
