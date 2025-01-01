#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module to count the number of digits in a given number.

Module contents:
    - count_digits: Counts the number of digits in a given number.

Created on Wednesday, 1st January, 2025.
@author: Gai Samuel
"""


def count_digits(number):
    """
    The count_digits function counts the number of integers in a given number.

    Parameters:
        number: an integer or float number whose digits are to be counted.

    Returns:
        An integer representing the number of digits in the input number.
        Note that the negative sign is not counted as a digit.

    Raises:
        AssertionError if the input is empty.
        AssertionError if the input is not an integer, float, or numeric string.
        AssertionError if the input is an invalid string.

    Example:
    >>> count_digits(34)
    2
    >>> count_digits(-17)
    2
    >>> count_digits(0)
    1
    >>> count_digits(19.5)
    2
    >>> count_digits("24")
    2
    """
    # Raises an assertion error if the input is empty or invalid.
    if number == "":
        raise AssertionError("The input cannot be empty.")

    # converts a float to an integer.
    if isinstance(number, float):
        number = int(number)

    # Handles a string input.
    if isinstance(number, str):
        try:
            number = int(number)
        except ValueError as exc:
            raise AssertionError("Input must be a valid number.") from exc

    # Check for empty or invalid inputs
    if not isinstance(number, (int, float, str)):
        raise AssertionError("Input must be an integer, float, or numeric string.")

    # Converts the number to its absolute value and then to a string. The absolute value is used to remove the negative sign.
    number_str = str(abs(int(number)))

    return len(number_str)
