#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module to check if two strings are anagrams of each other.

Module contents:
    - anagram_checker: Function to check if two strings are anagrams of each other.

Created on 01/01/2025
@author: Mohamed Saeed

"""


def anagram_checker(s1: str, s2: str) -> bool:
    """
    Function to check if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of a different
    word or phrase, typically using all the original letters exactly once.

    Parameters:
    s1 (str): The first input string.
    s2 (str): The second input string.

    Returns:
    bool: True if the strings are anagrams, False otherwise.

    Raises:
        assertionError: If the inputs are not strings.


    Examples:
    >>> anagram_checker("listen", "silent")
    True
    >>> anagram_checker("hello", "world")
    False
    >>> anagram_checker("rail safety", "fairy tales")
    True
    """
    assert isinstance(s1, str), "Input must be a string"
    assert isinstance(s2, str), "Input must be a string"
    assert len(s1) == len(s2), "Strings must have the same length."

    is_anagram = sorted(s1.replace(" ", "").lower()) == sorted(
        s2.replace(" ", "").lower()
    )
    return is_anagram
