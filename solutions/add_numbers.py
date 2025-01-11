"""
A module for adding two numbers

Created on 11 1 2025
@author: momtaz-yaqubi
"""


def add_numbers(a, b):
    """
    Adds two numbers together.

    Parameters:
        a (int, float): The first number to add.
        b (int, float): The second number to add.

    Returns:
        int, float: The result of adding `a` and `b`.

    Raises:
        TypeError: If either `a` or `b` is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b
