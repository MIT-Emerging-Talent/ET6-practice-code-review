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

# To identify and exclude punctuation characters by checking their Unicode category
import unicodedata


def is_palindrome(text_to_check: str) -> bool:
    """

    The function takes in a string and returns True if the string is a palindrome
    (reads the same backward as forward ignoring spaces, punctuation,
    and case differences) and False otherwise.


    Arguments:
    text_to_check (str): The input string to be checked.
    - Must be a valid string (an assertion will raise an error for non-strings).


    Returns:
    bool:
        - True if the input string is a palindrome (reads the same backward
        as forward after ignoring spaces, punctuation, and case differences).
        - False otherwise.
        - An empty string or a string with only spaces/punctuation is not
        considered a palindrome.

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
    # Assert that the input is a string
    assert isinstance(text_to_check, str), "text_to_check must be a string"

    # Convert to lowercase to ensure case-insensitivity
    text_to_check = text_to_check.lower()

    # Remove all types of whitespace (spaces, tabs, line breaks) from the string
    # This ensures that whitespaces are ignored when checking for palindromes
    text_to_check = "".join(text_to_check.split())

    # To ensure an empty string or a string with space/spaces considered non-palindrome
    if text_to_check == "":
        return False

    # Remove punctuation
    cleaned_text = ""
    for text_char in text_to_check:
        if not unicodedata.category(text_char).startswith("P"):
            cleaned_text += text_char

    # Reverse_string
    reversed_text = cleaned_text[::-1]

    return (
        reversed_text == cleaned_text
    )  # Check if the string is the same forwards and backwards
