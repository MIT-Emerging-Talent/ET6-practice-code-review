"""
Module to determine whether a number is odd or even.

This module provides a single function, `is_odd_or_even`, that takes an integer
and returns whether the number is "Odd" or "Even". Defensive checks ensure that
the input is a valid integer.

Author: Tamara Saqer
Date: 2025-01-10
"""

def is_odd_or_even(number: int) -> str:
    """
    Determine whether a number is odd or even.

    Args:
        number (int): The number to check. Must be an integer.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.

    Raises:
        ValueError: If the input is not an integer.

    Examples:
        >>> is_odd_or_even(4)
        'Even'
        >>> is_odd_or_even(7)
        'Odd'
        >>> is_odd_or_even(0)
        'Even'
        >>> is_odd_or_even(-3)
        'Odd'
        >>> is_odd_or_even(-2)
        'Even'
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    return "Even" if number % 2 == 0 else "Odd"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
