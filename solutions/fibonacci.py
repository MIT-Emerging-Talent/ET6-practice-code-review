#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for generating Fibonacci sequences.

Module contents:
- generate_fibonacci: Generates Fibonacci sequence up to n terms.

The Fibonacci sequence is a series of numbers where each number is the sum of the two
preceding ones, starting with 0 and 1.

Author: Fahed Daibes
Created: 12-Jan-2025
"""


def generate_fibonacci(n: int) -> list:
    """
    Generates the first n terms of the Fibonacci sequence.

    Parameters:
    - n (int): The number of terms to generate.

    Returns:
    - list: A list containing the first n terms of the Fibonacci sequence.

    Raises:
    - AssertionError: If the input is not a positive integer.

    Examples:
        >>> generate_fibonacci(0)
        []

        >>> generate_fibonacci(1)
        [0]

        >>> generate_fibonacci(5)
        [0, 1, 1, 2, 3]

        >>> generate_fibonacci("five")
        Traceback (most recent call last):
            ...
        AssertionError: Input must be a non-negative integer.
    """
    # Defensive check
    assert isinstance(n, int) and n >= 0, "Input must be a non-negative integer."

    if n == 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence
