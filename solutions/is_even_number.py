"""is_even_number.py
Module for checking if a number is even.
This module provides a simple utility function to determine if a number
is even, along with defensive checks for input validity.
"""


def is_even_number(number: int) -> bool:
    """
    Determines if a number is even.

    Args:
    number (int): The number to check. Must be an integer.

    Returns:
    bool: True if the number is even, False otherwise.

    Raises:
    AssertionError: If the input is not an integer.

    Examples:
    >>> is_even_number(2)
    True
    >>> is_even_number(3)
    False
    >>> is_even_number(0)
    True
    """
    assert isinstance(number, int), "Input must be an integer."
    return number % 2 == 0
