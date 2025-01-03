#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime


def time_into_2025(current_datetime: datetime) -> tuple[int, int, int]:
    """Calculates how many months, weeks, and days have passed in 2025.

    Args:
        current_datetime (datetime): The current datetime to calculate elapsed time.

    Returns:
        tuple[int, int, int]: A tuple containing:
            - Months passed
            - Weeks passed
            - Days passed

    Raises:
        ValueError: If the provided date is not in the year 2025.
    """
    if current_datetime.year != 2025:
        raise ValueError("This function is designed for the year 2025 only.")

    # Start of the year
    start_of_year = datetime(2025, 1, 1, 0, 0, 0)
    elapsed = current_datetime - start_of_year

    # Days passed
    days = elapsed.days
    if current_datetime > start_of_year:
        days += 1

    # Months passed (January = 0 months elapsed)
    months = current_datetime.month - 1

    # Weeks passed
    weeks = days // 7

    return months, weeks, days
