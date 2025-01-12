#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking for palindromic positive integers.

Module contents:
    - Checks for positive whole numbers that are palindromic.

Created on 08 01 2025
@author: Osei Agyemang Sarfo
"""


def palindrome_checker(number: int) -> bool:
    """Generates a boolean true if digit is palindromic otherwise false

    Parameters:
        number (int): The digits needed

    Returns:
        bool: True if the digit is palindromic otherwise false.

    >>> palindrome_checker(121)
    True

    >>> palindrome_checker(4354643)
    False

    >>> palindrome_checker(987353789)
    True
    """

    # Request for only a positive integer
    assert isinstance(number, int), "And number is needed"
    assert number > 0, "A positive integer is needed"

    # Negative numbers are not palindromes
    if number < 0:
        return False

        # Convert the integer to a string and check if it reads the same forward and backward
    str_number = str(number)
    return str_number == str_number[::-1]
