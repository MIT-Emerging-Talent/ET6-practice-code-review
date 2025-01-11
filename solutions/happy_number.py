#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to determine if a number is a happy number.

A happy number is defined by the process of replacing the number by the sum
of the squares of its digits. The process continues until the number equals
1 (indicating it is happy) or loops endlessly (indicating it is unhappy)
"""


def happy_number(number: int) -> bool:
    """
    Determine if a number is a happy number

    Args:
        number (int): A positive integer to check if happy

    Returns:
        bool: True if the number is happy, False otherwise

    Raises:
        ValueError: If number is not a positive integer

    Examples:
        >>> happy_number(19)
        True
        >>> happy_number(2)
        False
        >>> happy_number(1)
        True
    """
    # Ensure the input is a positive integer
    assert isinstance(number, int) and number > 0, "Input must be a positive integer"

    # Loop until the number becomes 1 or enters the 4 cycle
    while number != 1 and number != 4:
        sum = 0
        # Loop through the digits of the number
        while number > 0:
            digit = number % 10  # Get the rightmost digit
            sum += digit**2
            number //= 10  # Remove the rightmost digit from the number
        number = sum  # Update the number to the sum of squares

    # Return True if number is 1, otherwise False
    return number == 1
