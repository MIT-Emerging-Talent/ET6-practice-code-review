#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module providing FizzBuzz implementation.

This module implements the classic FizzBuzz programming task where numbers
are replaced with 'Fizz' for multiples of 3, 'Buzz' for multiples of 5,
and 'FizzBuzz' for multiples of both.

Created: 25/12/2024
Team Number: 28
Team Name: MIT Alpha
Author: Ghyath Ibrahim
"""


def fizz_buzz(n: int) -> list[str]:
    """
    Generate FizzBuzz sequence up to number n.

    Args:
        n (int): Upper bound of sequence (inclusive).
            Must be a positive integer.

    Returns:
        list[str]: List of strings where:
            - Multiples of 3 are replaced with 'Fizz'
            - Multiples of 5 are replaced with 'Buzz'
            - Multiples of both are replaced with 'FizzBuzz'
            - Other numbers are converted to strings

    Raises:
        AssertionError: If n is not a positive integer.

    Examples:
        >>> fizz_buzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']

        >>> fizz_buzz(15)[-3:]
        ['13', '14', 'FizzBuzz']

        >>> fizz_buzz(1)
        ['1']
    """
    # defensive assertions from unwanted data types and values
    assert isinstance(n, int), f"Expected integer, got {type(n).__name__}"
    assert n > 0, f"Expected positive integer, got {n}"

    result = []
    for i in range(1, n + 1):
        # Multiples of both are replaced with 'FizzBuzz'
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        # Multiples of 3 are replaced with 'Fizz'
        elif i % 3 == 0:
            result.append("Fizz")
        # Multiples of 5 are replaced with 'Buzz'
        elif i % 5 == 0:
            result.append("Buzz")
        # Other numbers are converted to strings
        else:
            result.append(str(i))

    return result
