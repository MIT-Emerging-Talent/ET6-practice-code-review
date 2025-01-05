#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on January 4, 2025

@author: Norbert Ndayisenga
"""


def count_even_numbers(numbers):
    """
    Count the even numbers in a list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The count of even numbers in the list.

    Raises:
        AssertionError: If any element in the list is not an integer.

    Examples:
        >>> count_even_numbers([2, 4, 6, 8])
        4
        >>> count_even_numbers([1, 3, 5, 7])
        0
        >>> count_even_numbers([1, 2, 3, 4, 5, 6])
        3
        >>> count_even_numbers([-2, -4, -6, -8])
        4
        >>> count_even_numbers([])  # An empty list should return 0
        0
        >>> count_even_numbers([1, 2, 'three', 4.5])  # Non-integer values raise an error
        Traceback (most recent call last):
            ...
        AssertionError: All elements in the list must be integers.
    """
    assert all(isinstance(num, int) for num in numbers), "All elements in the list must be integers."
    return sum(1 for num in numbers if num % 2 == 0)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
