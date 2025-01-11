#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for generating the reversing strings

Module contents: Takes a string as input and returns its reversed version

Created on 2025-01-01

@author: Jeffery Offei Darko
"""


def reverse_string(input_string: str):
    """This function takes a string and returns the reverse form of the string

    Parameters:
    string (str): The input to be reversed

    Returns:
    str: The reversed version of the input string

    Raises:
    AssertionError: If the input is not a string

    Examples:
    >>> reverse_string('hello')
    'olleh'

    >>> reverse_string('Python programming')
    'gnimmargorp nohtyP'

    >>> reverse_string('12345')
    '54321'

    >>> reverse_string('Madam')
    'madaM'

    >>> reverse_string('racecar')
    'racecar'

    >>> reverse_string('!@#$%^&*()')
    ')(*&^%$#@!'
    """
    # Check if input is a string
    assert isinstance(input_string, str), "Input must be a string"

    return input_string[::-1]


print(reverse_string("Evan Cole"))
