#!/usr/bin/env python3

"""
A module for calculating the average of a list of numbers.

Module contents:
    - calculate_average: Calculates and returns the average of a list of numbers.
"""


def calculate_average(numbers):
    """Returns the average of a list of numeric values (integers or floats).

    Takes a list of integers or floats and returns their average as a float.
    If the list is empty, this function returns None. If any element in the
    list is not an integer or float, an AssertionError is raised.

    Parameters:
        numbers: list of int or float, the values to average.

    Returns -> float or None: the average of all numbers. If the list is empty,
    returns None.

    Raises:
        AssertionError: if any element in the list is not an int or float

    Examples:
        >>> calculate_average([10, 20, 30, 40, 50])
        30.0
        >>> calculate_average([1.5, 2.5, 3.5])
        2.5
        >>> print(calculate_average([]))
        None
        >>> calculate_average([100])
        100.0
        >>> calculate_average([1, "two", 3])  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError: All elements must be int or float
    """

    if not numbers:
        return None

    for num in numbers:
        assert isinstance(num, (int, float)), "All elements must be int or float"
    return sum(numbers) / len(numbers)
