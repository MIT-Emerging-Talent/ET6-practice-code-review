#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for encrypting using caesar's cypher.

Module contents:
    - caesar_encryption: Encrypts the input text using the Caesar Cipher.
        - text: The input string to be encrypted.
        - shift: The number of positions each alphabetic character is shifted.
        How it works:
            - Each character in the input text is shifted by a specified number (shift).
            - The alphabet wraps around when shifting beyond 'Z'.
Created on 28/12/2024
@author: Caesar Ghazi
"""


def caesar_encryption(text: str, shift: int) -> str:
    """
    Encrypts a text using the Caesar Cipher.

    Parameters:
        text (str): The input text to encrypt.
        shift (int): The number of positions to shift each letter.
                    The shift value will be normalized using '% 26' to ensure
                    it stays within the range [0-25].

    Returns:
        str: The encrypted text.

    Raises:
        AssertionError: if Text is not a string.
        AssertionError: if Shift is not an integer.

    >>> caesar_encryption("Hello, World!", 3)
    'Khoor, Zruog!'

    >>> caesar_encryption("ABC", -1)
    'ZAB'

    >>> caesar_encryption("abc", 0)
    'abc'
    """
    assert isinstance(text, str), "Text must be a string."
    assert isinstance(shift, int), "Shift must be an integer."

    result = ""  # Initialize an empty string to store the encrypted result
    # Iterate through each character in the input text
    for character in text:
        # Process only alphabetic characters
        if character.isalpha():
            # Determine the starting ASCII code ('A' for uppercase, 'a' for lowercase)
            start = ord("A") if character.isupper() else ord("a")
            # Calculate the shifted position and wrap it using mod 26
            shifted = (ord(character) - start + shift) % 26 + start
            # Append the encrypted character to the result
            result += chr(shifted)
        else:
            # Non-alphabetic characters remain as they are
            result += character
    # Return the final result
    return result
