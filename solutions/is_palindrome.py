"""
A module for checking if a string is a palindrome.

Module contents:
    - is_palindrome: checks whether a string is a palindrome.

Created on 27 12 2024
@author: muqaddas96
"""


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome.

    Parameters:
        text: str, the input string to check

    Returns -> bool: True if the text is a palindrome, False otherwise

    Raises:
        AssertionError: if the argument is not a string

    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("A man a plan a canal Panama")
    True
    """
    assert isinstance(text, str), "input must be a string"

    # Remove spaces and convert to lowercase
    normalized_text = "".join(text.split()).lower()

    # Check if it reads the same forward and backward
    return normalized_text == normalized_text[::-1]
