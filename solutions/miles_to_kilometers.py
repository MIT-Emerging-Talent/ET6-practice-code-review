"""
Convert miles to kilometers.

This module provides a function to convert distances from miles to kilometers using
the conversion factor: 1 mile = 1.609344 kilometers. It also validates that the input
is a valid, non-negative number.

Example usage:
    >>> miles_to_kilometers(0)
    0.000

    >>> miles_to_kilometers(1)
    1.609344

    >>> miles_to_kilometers(10)
    16.09344

"""


def miles_to_kilometers(miles: float) -> float:
    """Convert miles to kilometers.

    Parameters:
    miles (float): The distance in miles to be converted.

    Returns:
    float: The converted distance in kilometers.

    Example:
    >>> miles_to_kilometers(1)
    1.609344
    >>> miles_to_kilometers(10)
    16.09344
    """
    if not isinstance(miles, (int, float)):
        raise ValueError("Input must be a number.")
    if miles < 0:
        raise ValueError("Distance cannot be negative.")

    # Conversion factor from miles to kilometers
    return miles * 1.609344
