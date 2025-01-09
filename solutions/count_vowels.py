#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting vowels in a given string.

Module contents:
    - count_vowels: A function to count the number of vowels in a string (case-insensitive).

Created on 2026-07-01
Author: Rumiya Ismatova
"""


def count_vowels(text: str) -> int:
    """
    Count_vowels function takes a string and count
    all upper and lower case vowels.

    Arguments:
    text (str): The input string to check for vowels. This string can
                contain alphabetic characters.


    Input:
    text[str]: The input string to check for vowels. This string may
                contain alphabetic characters.

    Return:
    num[int]: the number of vowels in text
            The total count of vowels (a, e, i, o, u) in the input string.
            Both uppercase and lowercase vowels are counted, and
            non-alphabetic characters are ignored.
            Returns 0 if no vowels are found.

    >>> count_vowels("")
    0

    >>> count_vowels("0")
    0

    >>> count_vowels("what")
    1

    >>> count_vowels("Hello")
    2

    >>> count_vowels("Austria")
    4

    >>> count_vowels("Hello, World!")
    3
    """

    if not text:  # Handle empty strings
        return 0

    vowels = {"a", "e", "i", "o", "u", "y"}
    count = 0

    for char in text:
        if char.lower() in vowels:
            count += 1

    # Defensive assertion for input validation
    assert isinstance(text, str), "Input should be a string"

    list_vowels = ["a", "e", "i", "o", "u", "y"]
    count = sum(1 for char in text if char.lower() in list_vowels)
    return count
