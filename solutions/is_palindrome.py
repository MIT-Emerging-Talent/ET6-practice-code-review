"""
is_palindrome.py
Module providing a function to check if a string is a palindrome.

Author: Faisal Minawi
Date: Jan 8 2025
Group: ET6-foundations-group-16
"""


def is_palindrome(s):
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric chars.

    Parameters:
        s (str): Input string

    Returns:
        bool: True if palindrome, False otherwise

    Raises:
        AssertionError: If input is not a string
    """
    assert isinstance(s, str), "Input must be a string"
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
