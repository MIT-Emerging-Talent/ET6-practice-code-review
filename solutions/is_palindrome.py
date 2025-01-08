#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for checking if a string is a palindrome.

Module contents:
    - is_palindrome: checks whether a given string is a palindrome,
    ignoring spaces, punctuation, and case differences.

Created on 2024-12-30
@author: Huda Alamassi
"""

import unicodedata


def is_palindrome(text_to_check: str) -> bool:
    """

    The function takes in a string and returns True if the string is a palindrome
    (reads the same backward as forward ignoring spaces, punctuation,
    and case differences) and False otherwise.


    Arguments:
    text_to_check (str): The input string to be checked.

    Returns:
    bool:
        - True if the string is a palindrome after removing spaces, punctuation,
        and case differences.
        - False if the string is not a palindrome or contains only spaces/punctuation.

    Raises:
    AssertionError: If the input is not a string.

    Examples:
        >>> is_palindrome("radar")
        True

        >>> is_palindrome("hello")
        False

        >>> is_palindrome("A man, a plan, a canal, Panama!")
        True

        >>> is_palindrome("No 'x' in Nixon")
        True

    """
    # validate input type
    assert isinstance(text_to_check, str), "text_to_check must be a string"

    # ensure case-insensitivity
    text_to_check = text_to_check.lower()

    # whitespace should not impact the palindrome check
    text_to_check = "".join(text_to_check.split())

    # punctuation should not impact the palindrome check
    cleaned_text = ""
    for text_char in text_to_check:
        if not unicodedata.category(text_char).startswith("P"):
            cleaned_text += text_char

    # exclude empty or non-informative strings
    if cleaned_text == "":
        return False

    reversed_text = cleaned_text[::-1]

    return reversed_text == cleaned_text
