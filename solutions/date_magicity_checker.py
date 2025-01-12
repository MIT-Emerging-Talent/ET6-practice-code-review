#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 05 01 2025

@author: Alona Niechvieieva
"""


def date_magicity_checker(date: str) -> bool:
    """
    Takes a date string and returns True if it's magic, False otherwise

    Check if a date is 'magic' (day * month == last two digits of year)

    Parameters:
        date: string, expected to be in the format: DD.MM.YYYY

    Returns :
        bool: True if the date is magic, False otherwise

    Raises:
        AssertionError: If `date` is not a string
        AssertionError: If `date` does not have a proper length of 10 characters
        AssertionError: If `date` does not have dots at positions 2 and 5
        AssertionError: If any part of the date is not a valid integer
        AssertionError: If day or month is out of valid range

    Examples:
        >>> date_magicity_checker("06.10.1860")
        True

        >>> date_magicity_checker("03.12.1936")
        True

        >>> date_magicity_checker("01.12.2004"):
        False
    """

    # Assertions for input format
    assert isinstance(date, str), "date is not a string"
    assert len(date) == 10, "date does not have a proper length"
    assert date[2] == "." and date[5] == ".", (
        "The dots are not placed at positions 2 and 5"
    )

    # String type input consists checked for the right format
    list_string_day_month_year = date.split(".")
    list_int_day_month_year = []

    # Convert parts of the date to integers, ensuring each part is a valid integer
    list_int_day_month_year = []
    for part in list_string_day_month_year:
        assert part.isdigit(), f"'{part}' is not a valid integer"
        list_int_day_month_year.append(int(part))

    # Extract day, month, and the last two digits of the year from the list
    day = list_int_day_month_year[0]
    month = list_int_day_month_year[1]
    year = list_int_day_month_year[2] % 100

    # Validate day and month ranges using assertions
    assert 1 <= day <= 31, f"Day {day} is out of valid range (1-31)"
    assert 1 <= month <= 12, f"Month {month} is out of valid range (1-12)"

    # Ensure the result fits within two digits
    day_month_multiplication = day * month
    if day_month_multiplication > 99:
        day_month_multiplication = day_month_multiplication % 100

    return day_month_multiplication == year
