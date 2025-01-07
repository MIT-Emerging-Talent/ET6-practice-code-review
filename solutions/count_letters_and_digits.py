#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to count the number of letters and digits in a sentence.

This module includes a function `count_letters_and_digits` that accepts a sentence
and calculates the number of letters and digits.

Created: 05/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Shaima Mohamed
"""


def count_letters_and_digits(sentence: str) -> dict[str, int]:
    """
    Count the number of letters and digits in a sentence.

    Parameters:
        sentence: str. The input sentence to be analyzed.

    Returns:
        dict: A dictionary containing the count of letters and digits.

    Raises:
        AssertionError: If the input is not a string.

    >>> count_letters_and_digits("hello world! 123")
    {'LETTERS': 10, 'DIGITS': 3}
    >>> count_letters_and_digits("abc 123 xyz")
    {'LETTERS': 6, 'DIGITS': 3}
    >>> count_letters_and_digits("!@#")
    {'LETTERS': 0, 'DIGITS': 0}
    >>> count_letters_and_digits("123")
    {'LETTERS': 0, 'DIGITS': 3}
    """
    # Defensive check to ensure the input is a string
    assert isinstance(sentence, str), "Input must be a string"

    #   The strategy processes each character in the input sentence, classifying it as
    #   a digit or letter, updating counts accordingly, and ignoring non-alphanumeric
    #   characters. The final counts are stored in a dictionary and returned.

    # Initialize counts for letters and digits.
    counts = {"LETTERS": 0, "DIGITS": 0}

    # Process each character, classify it as digit or letter.
    for char in sentence:
        if char.isdigit():
            counts["DIGITS"] += 1  # Increment digit count if character is a digit.
        elif char.isalpha():
            counts["LETTERS"] += 1  # Increment letter count if character is a letter.

    # Return the final counts after processing the sentence.
    return counts
