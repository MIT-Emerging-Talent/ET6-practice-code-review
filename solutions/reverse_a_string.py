#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for reversing a string
Module contents:
    - reverse_a_string: Creates a reversed copy of the string

Created on 25-12-2024
@author: Ahd AbdelRahim
"""


def reverse_a_string(text: str) -> str:
    """Returns a reversed copy of the string

    Parameters:
        text (str): The input string to be reversed

    Returns:
        str: The reversed string

    Examples:
    >>> reverse_a_string("")
    ''
    >>> reverse_a_string("Ahd")
    'dhA'
    >>> reverse_a_string("1,2,3")
    '3,2,1'
    >>> reverse_a_string("level")
    'level'

    Raises:
    TypeError: If input is not a string

    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    # Return the reversed string
    return text[::-1]


# Why I used TypeError instead of AssertionError?

# TypeError: tells exactly what went wrong.
# AssertionError can be turned off if Python is run in a special mode,
# so it's not reliable for checking user inputs.
