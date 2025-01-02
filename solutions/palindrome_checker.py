#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a string is a palindrome.

Module contents:
    - is_palindrome: Checks whether a given string is a palindrome.
        - text: The input string to check.
        How it works:
            - The string is sanitized by removing non-alphanumeric characters.
            - Case is normalized to lowercase.
            - The string is compared to its reverse to check for palindrome status.

Created on 28/12/2024
@author: Caesar Ghazi
"""


def palindrome_checker(text: str) -> bool:
    """
    Checks whether a given string is a palindrome.

    Parameters:
        text (str): The input string to check.

    Returns:
        bool: True if the text is a palindrome, False otherwise.

    Raises:
        AssertionError: If text is not a string.

    Examples:
    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("hello")
    False

    >>> is_palindrome("No lemon, no melon")
    True
    """

    assert isinstance(text, str), "Text must be a string."

    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())

    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]
