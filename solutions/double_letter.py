#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a word contains consecutive duplicate letters using recursion.

Module contents:
    - double_letter: checks if a word contains two identical consecutive letters.

Created on XX XX XX

@author: WUOR BHANG GATWECH

Challenge description:
In this challenge, you will create a recursive function that determines whether
a word contains at least one occurrence of two identical consecutive letters
(e.g., "hello" contains "ll"). The function returns `True` if such a sequence
is found and `False` otherwise.

"""


# --- function implementation ---
def double_letter(word):
    """
    Checks if a word contains two identical consecutive letters using recursion.

    Parameters:
        word (str): The word to check.

    Returns:
        bool: True if the word contains consecutive duplicate letters, False otherwise.

    Example:
        >>> double_letter("hello")
        True
        >>> double_letter("world")
        False
        >>> double_letter("bookkeeper")
        True
    """
    word = word.lower()  # Convert the string to lowercase

    # Checking if the word has less than two letters
    if len(word) < 2:
        return False

    # Checking if the word has two letters that are the same
    if word[0] == word[1]:
        return True
    # call the word
    return double_letter(word[1:])
