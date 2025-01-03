"""
Module: word_comparator

Description: This module provides a function to compare two words
by checking if their sorted characters are the same.

Created on: 03 01 25
@author: MD Jubayer Khan
"""


def are_words_same(word1: str, word2: str) -> bool:
    """
    Compares two words by sorting their characters and checking for equality.

    Parameters:
        word1 (str): The first word to compare.
        word2 (str): The second word to compare.

    Returns:
        bool: True if the sorted characters of both words are the same, False otherwise.

    Examples:
        >>> are_words_same("listen", "silent")
        True

        >>> are_words_same("word", "wrdo")
        True

        >>> are_words_same("hello", "world")
        False

        >>> are_words_same("", "")
        True
    """
    return sorted(word1) == sorted(word2)
