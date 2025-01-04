#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2025-12-25
@author: Alemayehu_Desta
"""

from datetime import datetime


def time_into_2025(current_date: datetime) -> tuple:
    """Calculates the elapsed months, weeks, and days into the year 2025.

    Args:
        current_date (datetime): The current date.

    Returns:
        tuple: A tuple containing the number of months, weeks, and days elapsed in 2025.

    Raises:
        ValueError: If the provided date is not in the year 2025.
    """
    # Ensure the date is in 2025
    if current_date.year != 2025:
        raise ValueError("Date must be in the year 2025.")

    # Reference start date
    start_of_year = datetime(2025, 1, 1)

    # Calculate elapsed days
    delta_days = (current_date - start_of_year).days

    # Calculate months, weeks, and days
    elapsed_months = delta_days // 30
    remaining_days = delta_days % 30
    elapsed_weeks = remaining_days // 7
    remaining_days = remaining_days % 7

    return elapsed_months, elapsed_weeks, delta_days + 1
