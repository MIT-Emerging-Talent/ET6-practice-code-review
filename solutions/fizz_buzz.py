#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for processing a list of numbers with specific rules:
- For multiples of 3, return "Fizz".
- For multiples of 5, return "Buzz".
- For multiples of both 3 and 5, return "FizzBuzz".
- Otherwise, return the number itself as a string.
@Author Sahar Omer
5/jan/2025
"""


def fizz_buzz(numbers: list[int]) -> list[str]:
    """
    Process a list of numbers according to the FizzBuzz rules.

    Parameters:
        numbers: list[int]
            A list of integers to process.

    Returns:
        list[str]: A list containing "Fizz", "Buzz", "FizzBuzz", or the number itself as a string.

    Raises:
        TypeError: If the input is not a list of integers.
        ValueError: If the list contains negative integers.

    Examples:
        >>> fizz_buzz([1, 3, 5, 15])
        ['1', 'Fizz', 'Buzz', 'FizzBuzz']
        >>> fizz_buzz([4, 6, 10, 30])
        ['4', 'Fizz', 'Buzz', 'FizzBuzz']
        >>> fizz_buzz([])
        []
    """
    # Defensive assertions
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers.")
    if not all(num >= 0 for num in numbers):
        raise ValueError("All integers in the list must be non-negative.")

    # Processing the FizzBuzz rules
    result = []
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))

    return result
