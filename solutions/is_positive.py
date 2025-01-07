"""
is_positive.py
This module provides a function to determine if a given number is positive.

Author: Faisal Minawi
Date: Mon Jan 6 2025
Group: ET6-foundations-group-16

Functions:
- is_positive(n): Determines if a given number is positive (greater than 0).
"""


def is_positive(n):
    """
    Checks if a given number is positive.

    Parameters:
    - n (int or float): A number to check.

    Returns:
    - bool: True if the number is greater than 0, False otherwise.

    Raises:
    - TypeError: If the input is not a real number (int or float)

    Examples:
        >>> is_positive(5)
        True
        >>> is_positive(-3)
        False
        >>> is_positive(0)
        False
        >>> is_positive(3.14)
        True
        >>> is_positive(-2.5)
        False
        >>> is_positive("5")
        Traceback (most recent call last):
            ...
        TypeError: Input must be a real number (int or float)
    """
    if not isinstance(n, (int, float)) or isinstance(n, bool):
        raise TypeError("Input must be a real number (int or float)")
    return n > 0
