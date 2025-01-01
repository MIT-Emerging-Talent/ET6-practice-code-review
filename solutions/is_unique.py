#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if all characters in a string are unique.

Module contents:
    - is_unique: Verifies if all characters in a given string are unique.

Created on 2025-01-01
Author: Ava Abdullah
"""


def is_unique(text: str) -> bool:
    """Checks if all characters in a string are unique.

    Parameters:
        text: str, the input string to check

    Returns -> bool: True if all characters are unique, False otherwise

    Raises:
        AssertionError: if the argument is not a string

    Examples:
        >>> is_unique("abcdefg")
        True
        >>> is_unique("aabbcc")
        False
        >>> is_unique(" ")
        True
    """
    assert isinstance(text, str), "Input must be a string"

    return len(set(text)) == len(text)
