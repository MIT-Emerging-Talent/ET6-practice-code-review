#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a given string is a palindrome (reads the same backward as forward)

Module contents:
    - palindrome: input string is palindrome if it reads the same backward as forward

Created on XX XX XX
@author: Saad M. Ashour
"""


def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters
    that reads the same forward and backward, ignoring spaces, punctuation,
    and case sensitivity.

    Parameters:
        s (str): The input string to be checked.

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
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = "".join(char.lower() for char in s if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]
