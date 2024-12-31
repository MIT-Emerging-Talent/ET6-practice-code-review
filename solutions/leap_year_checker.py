#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a given year is a leap year.

Module contents:
    - is_leap_year: A function that checks if a given year is a leap year.

Created on 2024-12-31
Author: Hussaini Ahmed
"""


def is_leap_year(year: int) -> bool:
    """
    Checks if a given year is a leap year.

    A leap year:
    - Is divisible by 4, but not divisible by 100, unless it is also divisible by 400.

    Parameters:
        year (int): The year to check. Must be a positive integer.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the year is not a positive integer.

    Examples:
        >>> is_leap_year(2020)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(2023)
        False
        >>> is_leap_year(0)
        False
    """
    if not isinstance(year, int):
        raise TypeError("The year must be an integer.")
    if year <= 0:
        raise ValueError("The year must be a positive integer.")

    # A year is a leap year if it is divisible by 4, not divisible by 100, or divisible by 400.
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
