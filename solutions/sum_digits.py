"""
This module contains a function sum_digits

It uses recursion to solve the sum of digits of n

"""


def sum_digits(num: int):
    """
    Calculate the sum of the digits of a given non-negative integer using recursion.

    Args:
    num (int): A non-negative integer whose digits will be summed.

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

    validate_input(num)

    if num == 0:
        return 0
    else:
        return num % 10 + sum_digits(num // 10)


def validate_input(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError("Input must be a non-negative integer.")
