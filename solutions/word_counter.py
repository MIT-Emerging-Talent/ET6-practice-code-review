#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting the number of words in a given text.

Module contents:
    - count_words: counts the number of words in a given text.
    - main: the main function of the module.

Created on 7 1 2025
@author: Collins Ochieng
"""


def word_counter(text: str) -> int:
    """
    Count the number of words in a given text.

    Parameters:
        text: str, the entered text.

    Returns -> int: The number of words in the text.

    Raises:
        AssertionError: if the argument is not a string.

    >>> count_words("Hello, World!")
    2
    >>> count_words("Python is awesome!")
    3
    >>> count_words("I love programming in Python.")
    5
    """
    assert isinstance(text, str), "Input must be a string."

    words = text.split()
    return len(words)
