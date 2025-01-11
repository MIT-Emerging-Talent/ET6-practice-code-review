"""
This module contains a function sum_digits

It uses recursion to solve the sum of digits of n

"""


def sum_digits(n):
    """
    Calculate the sum of the digits of a given non-negative integer using recursion.

    Args:
    n (int): A non-negative integer whose digits will be summed.

    Returns:
    int: The sum of the digits of the given integer.

    Examples:
    >>> sum_digits(123)
    6
    >>> sum_digits(0)
    0
    >>> sum_digits(9876)
    30
    >>> sum_digits(456)
    15
    """

    validate_input(n)

    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)


def validate_input(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
