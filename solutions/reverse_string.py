#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for reversing a string passed to the function by the user.

Module contents:
    - reverse_string: reverses the string passed to it.

Created on 5/1/2024
@author: Mohamed Altayeb
Group: ET foundations group 16 (Matrix)
"""


def reverse_string(to_be_reversed: str):
    """
    Reverses the input string and returns the reversed result.

    Arguments:
        to_be_reversed (str): The string we want to reverse.

    Returns:
        str: The resulted reversed string.

    Raises:
        AssertionError: If the input is not a string.

    Examples:
    >>> reverse_string("Mohamed")
    'demahoM'

    >>> reverse_string("test")
    'tset'

    >>> reverse_string("12345")
    '54321'

    """

    # The input must be a string
    assert isinstance(to_be_reversed, str), "Input must be a string"

    # Create a new string with the reversed elements
    reversed_string = ""
    for char in to_be_reversed:
        reversed_string = char + reversed_string

    # Return the new reversed string
    return reversed_string
