#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting any given string to uppercase.
Module contents:
    - convert_string_to_uppercase: A function that converts any given string to uppercase.
Created on 29 Dec 2024
@author: Noorelsalam Almakki
"""


def convert_string_to_uppercase(text: str) -> str:
    """The convert_string_to_uppercase function takes a string and returns the uppercase version of it.

    Parameters:
        - text (str): any string text.
    Returns:
        - upper_string (str): the uppercase version of the input text.
    Raises:
        - AssertionError: if the input text is not a string.
    Example:
    >>> convert_string_to_uppercase("hello")
    'HELLO'
    >>> sum_of_digits("HELLo")
    'HELLO'
    >>> sum_of_digits("")
    ''
    """
    assert isinstance(text, str), "The input text must be a string."

    upper_string = text.upper()

    return upper_string
