#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting vowels in a string.
Module contents:
    - count_vowels: Counts the number of vowels in a string.

Created on 8 1 2025
    @author: Nour Elhuda Haidar
"""


def count_vowels(text: str) -> int:
    """Counts the number of vowels (a, e, i, o, u) in the input string.

    Parameters:
        text (str): The input string.

    Returns:
        int: The number of vowels in the string.

    Raises:
        AssertionError: If the input is not a string.

    >>> count_vowels("hello world")
    3
    >>> count_vowels("Python is awesome")
    6
    >>> count_vowels("")
    0
    >>> count_vowels("123456")
    0
    """
    assert isinstance(text, str), "Input must be a string."
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
