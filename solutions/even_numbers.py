#!/usr/bin/env python3
# -- coding: utf-8 --

"""
This module checks if a given number is even and returns True for even numbers or False otherwise.
Created on 2025-01-11

@author: Martha Yelademe Nyekanga
"""


def is_even(number: int) -> bool:
    """This function checks if a given number is even.

    Parameters:
    number (int): The number to check

    Returns:
    bool: True if the number is even, False otherwise

    Raises:
    AssertionError: If the input is not an integer

    Examples:
    >>> is_even(2)
    True

    >>> is_even(3)
    False

    >>> is_even(0)
    True

    >>> is_even(-4)
    True
    """
    assert isinstance(number, int) and not isinstance(number, bool), (
        "the input number must be an integer and not a boolean"
    )
    # Return True if the number is even, False otherwise
    return number % 2 == 0


# Example:
if __name__ == "__main__":
    print(is_even(0))
