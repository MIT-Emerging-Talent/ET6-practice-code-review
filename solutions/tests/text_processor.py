"""
This module provides functions to process texts and convert them in different ways.

Created on: 04/01/2025
@author: Thilakan Jegatheeswaran
"""


def count_vowels(text: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in the given text.

    Args:
        text (str): The string to analyze.

    Returns:
        int: The number of vowels in the text.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def reverse_text(text: str) -> str:
    """
    Reverse the given text.

    Args:
        text (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return text[::-1]


def to_uppercase(text: str) -> str:
    """
    Convert the given text to uppercase.

    Args:
        text (str): The string to convert.

    Returns:
        str: The text in uppercase.
    """
    return text.upper()
