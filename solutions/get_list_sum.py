#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the sum of numbers provided by the user.

Module contents:
    - get_list_sum: calculates the sum of numbers provided by the user.

Created on 2025-01-03
@author: Muqadsa Tahir
"""


def get_list_sum(sequence_length: int) -> int:
    """
    Calculates the sum of a list of numbers provided by the user.

    Parameters:
        sequence_length (int, greater than or equal to zero):
        The number of elements to be entered by the user.

    Returns -> int: The sum of the numbers entered by the user.

    Raises:
        AssertionError: If argument is not an integer.
        AssertionError: If argument is less than 0.

    >>> get_list_sum(3)  # Example usage (assuming user inputs: 2, -5, 10)
    7
    >>> get_list_sum(4)  # Example usage (assuming user inputs: 1, 2, 3, 4)
    10
    """

    # the sequence length should be an integer greater than 0
    assert isinstance(sequence_length, int), "sequence_length must be an integer"
    assert sequence_length >= 0, "sequence_length must be greater than or equal to zero"

    # This function first iteratively prompts the user to enter each number in the sequence.
    # Finally, it calculates and returns the sum of the entered numbers.
    numbers = []
    for i in range(sequence_length):
        number = int(input(f"Enter element {i+1}: "))
        numbers.append(number)

    return sum(numbers)
