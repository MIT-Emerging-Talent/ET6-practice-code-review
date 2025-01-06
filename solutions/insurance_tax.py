#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to calculate insurance tax

Module contents:
    - insurance_tax: returns the insurance tax calculated based on the weekly salary.

Created on 2025-01-04
@author: Nay Win Hlaing
"""


def insurance_tax(weekly_salary: float) -> float:
    """
    Returns the insurance tax based on weekly salary.
    Tax is 0% on the first 183 you earn;
    12% on earnings between 183 and 962(inclusive);
    2% on anything above 962.

    Parameters:
        weekly_salary: float, greater than or equal to zero
                    & up to 2 decimals

    Returns:
        float: greater than or equal to zero
            & up to 2 decimals

    Raises:
        ValueError: if the argument is not an int or float
        ValueError: if the argument is less than 0


    >>> insurance_tax(0):
    0
    >>> insurance_tax(183):
    0
    >>> insurance_tax(961.78):
    93.45
    """
    # Validate input is a number.
    if not isinstance(weekly_salary, (float, int)):
        raise ValueError("Input must be a number.")

    # Ensure weekly salary is not a negative number.
    if weekly_salary < 0:
        raise ValueError("Weekly Salary must not be negative.")

    # Tax is 0% if the salary is below or equal to 183
    if weekly_salary <= 183:
        tax = 0

    # Tax is 0.12% of the earnings that are between 183 and 962(inclusive)
    elif weekly_salary > 183 and weekly_salary <= 962:
        tax = round(0.12 * (weekly_salary - 183), 2)

    # If the salary is above 962, tax is
    # 12% of the earnings between 183 and 962(inclusive)
    # in addition to 2% of the earnings above 962
    elif weekly_salary > 962:
        tax = round(0.02 * (weekly_salary - 962) + 0.12 * (962 - 183), 2)

    return tax
