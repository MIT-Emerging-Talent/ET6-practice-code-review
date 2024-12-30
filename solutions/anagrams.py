#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function that takes two strings as input and checks if they
are anagrams of each other. Anagrams are words or phrases made by
rearranging the letters of another, using all original letters
exactly once

True if the two strings are anagrams, False otherwise

"""


def is_anagrams(word1: str, word2: str) -> bool:
    """
    Returns true or false if the two strings given are anagrams
    of each other.

    Parameters:
        word1: The first string
        words2: The second string

    Returns -> bool: Either true or false of either the strings
    are anagrams of each other or not.

    Raises:
        AssertionError: if the parameters are not strings

    Examples:
        >>> is_anagrams("anagram", "nagaram")
        True
        >>> is_anagrams("rat", "car")
        False
    """
