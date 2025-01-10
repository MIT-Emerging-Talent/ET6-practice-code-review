#!/usr/bin/env python3
"""
A module for squaring a number.
Module contents:
    - square_number: Returns the square of a given number.
"""


def square_number(number):
    """Returns the square of a number.
    Takes a number (int or float) and returns its square. If the input is not a valid number (either integer or float), an AssertionError is raised.
    Parameters:
        number: int or float, the number to square
    Returns -> int or float: the square of the number
    Raises:
        AssertionError: if the input is not an int or float
    Examples:
        >>> square_number(5)
        25
        >>> square_number(3.5)
        12.25
        >>> square_number(-4)
        16
    """
    assert isinstance(number, (int, float)), "Input must be an int or float"
    return number**2
