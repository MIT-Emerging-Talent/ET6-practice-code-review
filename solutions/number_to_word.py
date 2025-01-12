#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting single-digit number into its word representation.

Module contents:
    - number_to_word: converts a number ranging from (0-9) to it's word equivalent.

Created on 04 01 2024
@author: Terry Aziaba
"""


def number_to_word(number: int) -> str:
    """
    Converts a single-digit number into its word representation.

    Parameters:
        number (int): A single-digit number (0–9).

    Returns:
        str: The word representation of the number.

    Raises:
        ValueError: If the number is not a single digit.

    Examples:
        >>> number_to_word(0)
        'zero'

        >>> number_to_word(7)
        'seven'

        >>> number_to_word(10)
        Traceback (most recent call last):
            ...
        ValueError: Number must be a single digit (0–9).
    """
    # A dictionary mapping digits to their word representation
    digit_to_word = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    # Checks if the input is a valid single-digit number
    if number not in digit_to_word:
        raise ValueError("Number must be a single digit (0–9).")

    # Returns the word representation
    return digit_to_word[number]
