#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to format an array of integers
into a phone number string.

Module contents:
    - format_phone_number: returns a string formatted as a phone number from a list of integers

Created on 2025-01-04
@author: KarimMakki
"""


def format_phone_number(phone_number: list) -> str:
    """Returns a string formatted as a phone number from a list of integers

    The function should:
    - Accept exactly 10 integers as input.
    - Ensure all integers are between 0 and 9.
    - Return a string in the format: "(XXX) XXX-XXXX", where X represents the digits from the input array.

    Parameter:
    phone_number: a list of integers

    Returns -> str: a string formatted as a phone number

    Raises:
    AssertionError: if the input type is not a list
    AssertionError: If the input contains non-integer elements.
    ValueError: if the input list does not contain exactly 10 integers
    ValueError: if any integer is not in the range 0 to 9


    Examples:
        >>> format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        '(123) 456-7890'

        >>> format_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        '(000) 000-0000'

        >>> format_phone_number([5, 6 ,7, 3, 2, 3, 1, 2, 0, 9])
        '(567) 323-1209'
    """

    # Validate input is a list
    assert isinstance(phone_number, list), "input must be a list"

    # Ensure correct phone number length
    if len(phone_number) != 10:
        raise ValueError("phone_number must have 10 digits")

    for phone_digit in phone_number:
        # Validate all elements are integers
        assert isinstance(phone_digit, int), "input must be an integer"

        # Validate each digit is within valid range
        if phone_digit < 0 or phone_digit > 9:
            raise ValueError("input must be between 0 and 9")

    # Combine all digits into a single string
    phone_digits = "".join(str(digit) for digit in phone_number)

    # Format the string into the required phone number pattern
    formatted_phone_number = (
        f"({phone_digits[:3]}) {phone_digits[3:6]}-{phone_digits[6:]}"
    )

    return formatted_phone_number
