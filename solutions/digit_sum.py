#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 06 01 25

@author: Alona Niechvieieva
"""


def digit_sum(number):
    """
    Takes a single natural number and returns the sum of its digits

    Parameters:
        number: int, greater than or equal to zero

    Returns:
        int: The sum of the digits of the number

    Raises:
        TypeError: If number is not an integer
        ValueError: If number is less than 0

    Examples:
        >>> print_digit_sum(5)
        5
        >>> print_digit_sum(37)
        10
        >>> print_digit_sum(188)
        17

    """

    # Defensive assertions
    assert isinstance(number, int), "number is not an integer"
    assert number >= 0, "number is less than 0"

    # Calculate the sum of the digits of the number
    sum_of_the_digits = 0
    while number > 0:
        sum_of_the_digits += number % 10
        number //= 10

    return sum_of_the_digits
