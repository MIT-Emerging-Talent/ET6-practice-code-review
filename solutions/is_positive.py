#!/usr/bin/env python3

"""
A module for checking if a number is positive.

Module contents:
- is_positive: Determines if a given number is positive.

Author: Faisal Minawi
Created: 2025-01-08
"""


def is_positive(n: float) -> bool:
    """Determines if a given number is positive.

    A number is considered positive if it is greater than 0.

    Raises:
        TypeError: If the input is not a real number (int or float).

    Parameters:
        n: float or int, the number to check.

    Returns:
        bool: True if the number is greater than 0, False otherwise.

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
        >>> is_positive(True)
        Traceback (most recent call last):
            ...
        TypeError: Input must be a real number (int or float)
    """
    if isinstance(n, bool):
        raise TypeError("Input must be a real number (int or float)")
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a real number (int or float)")
    return n > 0
