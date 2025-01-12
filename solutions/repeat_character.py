#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Repeat Character

A function that takes in a string, a single character, and a number.
The function returns a string with each occurrence of the character repeated n times.

Created on 2/1/2025
Author: Aziz Azizi

"""


def repeat_character(text: str = "", repeat_char: str = "", n: int = 1) -> str:
    """Repeat a character n times in a string.

    Parameters:
    text (str): The input string.
    repeat_char (str): The character to repeat.
    n (int): The number of times to repeat the character.

    Returns:
    str: The modified string with each occurrence of the character repeated n times.

    Raises:
    TypeError: If text is not a string, repeat_char is not a string,
    or n is not an integer.

    AssertionError: If repeat_char is not a single character or n is negative.

    doctest:
    >>> repeat_character("Aziz", "z", 3)
    'Azzzizzz'
    >>> repeat_character("Gray", "r", 5)
    'Grrrrray'
    >>> repeat_character("Hand", "h", 5)
    'HHHHHand'
    >>> repeat_character("Hand", "D", 3)
    'Handdd'
    >>> repeat_character("", "a", 2)
    ''
    >>> repeat_character()
    ''
    >>> repeat_character("bat", "a")
    'bat'
    >>> repeat_character("Azxxizxx", "x", 0)
    'Aziz'
    >>> repeat_character("Aziz", "z", -1)
    Traceback (most recent call last):
    ...
    AssertionError: n must be a positive integer
    >>> repeat_character(123, "a", 3)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string
    >>> repeat_character("Earth", "t", "g")
    Traceback (most recent call last):
    ...
    TypeError: n must be an integer
    >>> repeat_character("word", 4, 6)
    Traceback (most recent call last):
    ...
    TypeError: repeat_char must be a string
    >>> repeat_character("text", "long", 3)
    Traceback (most recent call last):
    ...
    AssertionError: repeat_char must be a single character
    """
    # checks if the type and value of the input parameters are correct
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(repeat_char, str):
        raise TypeError("repeat_char must be a string")
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if len(repeat_char) > 1:
        raise AssertionError("repeat_char must be a single character")
    if n < 0:
        raise AssertionError("n must be a positive integer")

    # Repeat the repeat_char 'n' times in the text
    result = ""
    for char in text:
        if char.lower() == repeat_char.lower() and n > 0:
            result += char * n  # Repeat the character 'n' times if condition is met
        elif char.lower() == repeat_char.lower() and n == 0:
            continue  # Remove the character if n is 0
        else:
            result += char

    return result
