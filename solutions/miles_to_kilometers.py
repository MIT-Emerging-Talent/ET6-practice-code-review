"""
miles_to_kilometers.py

This module provides a function to convert miles to kilometers.

Author: Obay Salih
Date: Fri 10/1/2025
Group: ET6-foundations-group-16 (Matrix)

Functions:
- miles_to_kilometers(miles): Converts miles to kilometers and returns the result.
"""


def miles_to_kilometers(miles: float) -> float:
    """
    Convert miles to kilometers.

    Parameters:
    - miles (int or float): The distance in miles to be converted.

    Returns:
    - float: The converted distance in kilometers.

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


if __name__ == "__main__":
    # Example usage
    print("Example: miles_to_kilometers(5) =", miles_to_kilometers(5))
