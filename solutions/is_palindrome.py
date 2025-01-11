#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a string is a palindrome.

Created on 8 1 2025
@author: Dadi Ishimwe
"""


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome.

    Parameters:
        text: str, The string to check.

    Returns -> bool, True if the string is a palindrome, False otherwise.

    Raises:
        AssertionError: if the argument is not a string.

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("hello")
    False

    >>> is_palindrome("A man, a plan, a canal, Panama")
    True

    >>> is_palindrome("")
    True
    """
    # Validate the input data type
    assert isinstance(text, str)

    # Normalize the string by removing non-alphanumeric characters and converting to lowercase
    normalized_text = "".join(char.lower() for char in text if char.isalnum())

    # Check if the normalized string is a palindrome
    return normalized_text == normalized_text[::-1]
