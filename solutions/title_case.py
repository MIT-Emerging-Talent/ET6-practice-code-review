#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting Sentence to title.

Module contents:
    - title_case: converts a Sentence to title.

Created on 5 1 2025
    @author: Nour Elhuda Haidar
"""

def title_case(sentence: str) -> str:
    """Converts a string to title case
    (capitalize the first letter of each word).

    Parameters:
        sentence (str): The input string.

    Returns:
        str: The string converted to title case.

    Raises:
        AssertionError: If the input is not a string.
        
    >>> title_case("hello world")
    'Hello World'
    >>> title_case("PYTHON is awesome")
    'Python Is Awesome'
    >>> title_case("")
    ''
    >>> title_case("123abc")
    '123Abc'
    """
    assert isinstance(sentence, str), "Input must be a string."
    return sentence.title()