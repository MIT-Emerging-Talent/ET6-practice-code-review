#!/usr/bin/env python3
"""
Module to swap two numbers.

Author: Majd Abualsoud
Date: 11st January 2025
Group: ET6-foundations-group-16
"""


def swap_numbers(a: float, b: float) -> tuple:
    """
    Swaps the values of two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        tuple: A tuple containing the swapped values (b, a).

    Examples:
        >>> swap_numbers(1, 2)
        (2, 1)
        >>> swap_numbers(10, 20)
        (20, 10)
        >>> swap_numbers(0, 5)
        (5, 0)
        >>> swap_numbers("10", 20)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError: Both a and b must be numeric values (int or float)
    """
    # Ensure that both a and b are numeric values (either int or float)
    assert isinstance(
        a, (int, float)
    ), "Both a and b must be numeric values (int or float)"
    assert isinstance(
        b, (int, float)
    ), "Both a and b must be numeric values (int or float)"

    # Swap the values and return as a tuple
    return b, a
