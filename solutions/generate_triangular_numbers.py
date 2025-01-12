"""
This module provides functions to generate triangular numbers.

A triangular number is the sum of consecutive natural numbers starting from 1.
The nth triangular number can be calculated using the formula: n * (n + 1) / 2.

This module offers the following functionality:

- `generate_triangular_numbers(n)`: Generates a list of the first n triangular numbers.
"""


def generate_triangular_numbers(n):
    """
    Generates a list of the first n triangular numbers.

    Args:
        n (int): The number of triangular numbers to generate (positive integer).

    Returns:
        list: A list containing the first n triangular numbers.

    Raises:
        ValueError: If n is not a positive integer.

    Examples:
        >>> generate_triangular_numbers(5)
        [1, 3, 6, 10, 15]

        >>> generate_triangular_numbers(1)
        [1]

        >>> generate_triangular_numbers(10)
        [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

        >>> generate_triangular_numbers(0)
        Traceback (most recent call last):
        ...
        ValueError: n must be a positive integer

        >>> generate_triangular_numbers(-3)
        Traceback (most recent call last):
        ...
        ValueError: n must be a positive integer

        >>> generate_triangular_numbers("five")
        Traceback (most recent call last):
        ...
        ValueError: n must be a positive integer
    """
    if not isinstance(n, int):
        raise ValueError("n must be a positive integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    triangular_numbers = []
    for i in range(1, n + 1):
        triangular_numbers.append(i * (i + 1) // 2)
    return triangular_numbers
