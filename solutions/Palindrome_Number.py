#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/01/2025
@author: Dorcas Wanja Njeri
"""


def is_Palindrome_Number(x: int) -> bool:
    """
    Determines if a given integer is a palindrome number.

    A palindrome number is one that remains the same when its digits are reversed.

    Parameters:
        x (int): The integer to check for palindrome.

    Returns:
        bool: True if the number is a palindrome, False otherwise.

    Raises:
        ValueError: If the input is not an integer.

    Examples:
    >>> is_palindrome_number(121)
    True
    >>> is_palindrome_number(-121)
    False
    >>> is_palindrome_number(123)
    False
    >>> is_palindrome_number(5)
    True
    >>> is_palindrome_number(12321)
    True
    >>> is_palindrome_number(0)
    True
    """
    if not isinstance(x, int):
        raise ValueError("The input must be an integer.")

    # Negative numbers and numbers that end with a 0 (except 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10
