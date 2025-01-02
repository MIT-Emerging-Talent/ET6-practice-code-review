"""
A module for counting words in a string.

Module contents:
    - count_words: counts the number of words in a string.

Created on 01 01 2025
@author: Raghad
"""


def count_words(text: str) -> int:
    """Count the number of words in a given string.

    Parameters:
        text: str, the input string to analyze

    Returns -> int: number of words in the text

    Raises:
        AssertionError: if the argument is not a string

    >>> count_words("Hello World")
    2
    >>> count_words("Python programming is fun")
    4
    >>> count_words("")
    0
    """
    # Validate input
    assert isinstance(text, str), "Input must be a string"

    # Split the text by whitespace and count the resulting parts
    words = text.split()
    return len(words)
