#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a given string is a palindrome (reads the same backward as forward)

Module contents:
    - palindrome: input string is palindrome if it reads the same backward as forward

Created on 30.12.2024
@author: Saad M. Ashour
"""


def is_palindrome(input_string: str) -> bool:
    """
    Check if a given string is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters
    that reads the same forward and backward, ignoring spaces, punctuation,
    and case sensitivity.

    Parameters:
        input_string (str): The input string to be checked.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("A man, a plan, a canal, Panama")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("Madam")
        True
    """
    # AssertionError: Input must be a string
    assert isinstance(input_string, str), "Input must be a string"

    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = "".join(char.lower() for char in input_string if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]
