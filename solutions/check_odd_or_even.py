#!/usr/bin/env python3
"""
A module for determining if a number is even or odd.

Module contents:
    - check_odd_or_even: Returns "Even" if the number is even, "Odd" otherwise.

Author: Clement MUGISHA
Date: 7th January 2025
Group: ET6-foundations-group-16
"""


def check_odd_or_even(num: int) -> str:
    """
    Checks if the provided integer is even or odd.

    Parameters:
        num (int): The integer to check.

    Returns:
        str: "Even" if num is even, otherwise "Odd".

    Raises:
        AssertionError: If num is not an integer.

    Examples:
        >>> check_odd_or_even(4)
        'Even'
        >>> check_odd_or_even(7)
        'Odd'
        >>> check_odd_or_even(0)
        'Even'
        >>> check_odd_or_even(-3)
        'Odd'
        >>> check_odd_or_even(2.5)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError: num must be an integer
    """
    assert isinstance(num, int), "num must be an integer"
    return "Even" if num % 2 == 0 else "Odd"
