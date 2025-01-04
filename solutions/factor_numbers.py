"""
This module provides a function to calculate the factorial of a number recursively.

The factorial function is defined only for non-negative integers.
"""

from typing import Union


def factorial(n: int) -> Union[int, None]:
    """
    Calculate the factorial of a given non-negative integer.

    Args:
        n (int): The number whose factorial is to be calculated. Must be >= 0.

    Returns:
        Union[int, None]: The factorial of the input number, or None if the input is invalid.

    Raises:
        ValueError: If `n` is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
