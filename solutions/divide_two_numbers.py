"""
A module to divide two numbers and return the result.

Created 2025-01-04

@author: Henry Ogoe
"""


def divide_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns quotient.

    Parameters:
    a(int): The first integer
    b(int): The second integer

    Returns:
    int: Result of division of numerator (a) by denominator (b).

    Raises:
        TypeError: If the input contains non-integer elements.
        ValueError: If denominator is 0.

    Examples:
    >>> divide_numbers(4, 2)
    2
    >>> divide_numbers(64, 4)
    16

    >>> divide_numbers("4", 2)
    Traceback (most recent call last):
    TypeError: Inputs must be integers.

    >>> divide_numbers(8,0)
    Traceback (most recent call last):
    ValueError: Please dont divide by zero.
    """

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers.")
    if b == 0:
        raise ValueError("Please dont divide by zero.")
    return a // b
