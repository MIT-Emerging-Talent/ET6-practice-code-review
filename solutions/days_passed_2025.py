#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for calculating elapsed days in 2025.

Module contents:
    - Calculates the total number of days elapsed in 2025, including the current day.
"""

from datetime import datetime

__author__ = "Alemayehu_Desta"
__created__ = "2025-12-25"


def days_passed_2025(current_date: datetime) -> int:
    """
    Calculates the total number of days elapsed in 2025.

    Parameters:
        current_date (datetime): The current date.

    Returns:
        int: The number of days elapsed in 2025, including the current day.

    Raises:
        ValueError: If the provided date is not in the year 2025.
    """
    if current_date.year != 2025:
        raise ValueError("Date must be in the year 2025.")

    # Reference start date
    start_of_year = datetime(2025, 1, 1)

    # Calculate elapsed days
    delta_days = (current_date - start_of_year).days + 1

    return delta_days
