"""
A module for checking whether a given year is a leap year.

This module provides a single function:
- `is_leap_year(year)`: Returns True if the year is a leap year, False otherwise.

@Author Sahar Omer
5/Jan/2025
"""


def is_leap_year(year: int) -> bool:
    """
    Determines if a given year is a leap year.

    Parameters:
        year (int): The year to check. Must be a positive integer.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the year is not a positive integer.

    Examples:
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2024)
        True
        >>> is_leap_year(2023)
        False
    """
    if not isinstance(year, int):
        raise TypeError("Year must be an integer.")
    if year <= 0:
        raise ValueError("Year must be a positive integer.")

    # Leap year logic
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
