#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A module containing function for the leap_year function.
Module contents:
leap_year: Determines if a given year is a leap year.

Created on 2025-01-03
Author: Solara Hamza
"""


def leap_year(year: int) -> bool:
    """Determines if a given year is a leap year.
    This function takes a year as input and returns True if it is a leap year,
    and False otherwise.
    Parameters:
        year: int, the year to check for leap year
    Returns -> bool: True if the year is a leap year, False otherwise
    Examples:
        >>> leap_year(2000)
        True
        >>> leap_year(1900)
        False
        >>> leap_year(2024)
        True
        >>> leap_year(2025)
        False
    """
    if year < 0:
        raise ValueError("Year must be a positive integer")
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0 and year % 100 == 0:
        return True
    else:
        return False
