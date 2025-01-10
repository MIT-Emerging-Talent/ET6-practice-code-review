#!/usr/bin/env python3
"""
Module to convert feet to meters.

The conversion factor from feet to meters is:
    1 foot = 0.3048 meters

Author: Obay Salih
Date: 8th January 2025
Group: ET6-foundations-group-16

"""


def feet_to_meters(feet: float) -> float:
    """
    Converts a length from feet to meters.

    Parameters:
        feet (float): The length in feet. It must be a numeric value (int or float).

    Returns:
        float: The equivalent length in meters.

    Raises:
        AssertionError: If feet is not a numeric value (int or float).

    Examples:
        >>> feet_to_meters(1)
        0.3048
        >>> feet_to_meters(10)
        3.048
        >>> feet_to_meters(0)
        0.0
        >>> feet_to_meters(-5)
        -1.524
        >>> feet_to_meters("10")  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError: feet must be a numeric value (int or float)
    """
    # Ensure that the input is a numeric value (either int or float)
    assert isinstance(feet, (int, float)), "feet must be a numeric value (int or float)"

    # Conversion from feet to meters
    return feet * 0.3048
