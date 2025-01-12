"""
Module for filtering even numbers from a list of integers.

This module provides a function that takes a list of integers as input
and returns a list of all even numbers from the input list.

@author: Vahab
@created: 01/11/2025
"""

from typing import List


def get_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filters even numbers from a list of integers.

    Parameters:
    numbers (List[int]): A list of integers to filter.

    Returns:
    List[int]: A list containing all even numbers from the input list.

    Raises:
    TypeError: If the input is not a list or contains non-integer elements.

    Example:
    >>> get_even_numbers([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> get_even_numbers([1, 3, 5])
    []
    >>> get_even_numbers([])
    []
    """
    # Check the input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    # Check the list items are only integers
    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("All elements in the list must be integers.")

    # Filters the even number from input list and store them in a list
    return [n for n in numbers if n % 2 == 0]


if __name__ == "__main__":
    example_input = [1, 2, 3, 4, 5, 6]
    print(get_even_numbers(example_input))
