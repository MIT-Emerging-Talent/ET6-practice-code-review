#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for encrypting using caesar's cypher.

Module contents:
    - caesar_encryption: generates an encrypted string.

Created on 28/12/2024
@author: Caesar Ghazi
"""


def caesar_encryption(text: str, shift: int) -> str:
    """
    Encrypts a text using the Caesar Cipher.

    Parameters:
        text (str): The input text to encrypt.
        shift (int): The number of positions to shift each letter.

    Returns:
        str: The encrypted text.

    >>> caesar_encryption("Hello, World!", 3)
    'Khoor, Zruog!'

    >>> caesar_encryption("ABC", -1)
    'ZAB'

    >>> caesar_encryption("abc", 0)
    'abc'
    """
    assert isinstance(text, str), "Text must be a string."
    assert isinstance(shift, int), "Shift must be an integer."

    result = ""
    for character in text:
        if character.isalpha():
            start = ord("A") if character.isupper() else ord("a")
            shifted = (ord(character) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += character

    return result
