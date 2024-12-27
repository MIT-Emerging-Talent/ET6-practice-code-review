#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-12-27

@author: Yuri Spizhovyi
"""


def count_vowels(text: str) -> int:
    """
    Count_vowels function takes a string and count
    all upper and lower case vowels.

    Input: text[str]

    Return: num[int] the number of vowels in text

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

    # Check if input is a string
    assert isinstance(text, str), "Input should be a string"

    list_vowels = ["a", "e", "i", "o", "u", "y"]
    count = 0
    for char in text:
        if char.lower() in list_vowels:
            count += 1
    return count


count_vowels("Hello")
