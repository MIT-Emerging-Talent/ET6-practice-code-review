#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for converting a value in hours to minutes.

Module contents:
    > hours_to_minutes: converts a value in hours to minutes.

Created on the 04 Jan 2025
@author: Tosan Okome
"""


def hours_to_minutes(hours: float) -> int:
    """
        Converts a given value in hours to its equivalent in minutes.

    Parameters:
        hours : float
            The number of hours to convert to minutes. Must be a numerical value (int or float).

        Returns:
        int
            The equivalent number of minutes.

        Raises:
        TypeError:
            If the input is not a number (int or float).

        ValueError:
            If the input is negative.

        Examples:
            >>> hours_to_minutes(4)
            (240)
            >>> hours_to_minutes(0.5)
            (30)
            >>> hours_to_minutes(24)
            (1440)
            >>> hours_to_minutes(12)
            (720)
    """
    if not isinstance(hours, (int, float)):
        raise TypeError(f"Invalid input type: {type(hours)}. Must be int or float.")

    if hours < 0:
        raise ValueError("Invalid input: hours cannot be negative.")

    return int(hours * 60)
