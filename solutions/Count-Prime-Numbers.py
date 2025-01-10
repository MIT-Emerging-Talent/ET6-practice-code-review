#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides functions for checking primality and counting prime numbers in a list.

Date: 09 01 2025
Author: Zeinab Shadabshoar
"""

def is_prime(n: int) -> bool:
    """
    Checks if a given number is prime.

    Args:
        n: The number to check.

    Returns:
        True if the number is prime, False otherwise.

    Raises:
        AssertionError: If n is not an integer or n is negative.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    """
    assert isinstance(n, int), "Input must be an integer"
    assert n >= 0, "Input must be a non-negative integer"

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(numbers: list) -> int:
    """
    Counts the number of prime numbers in a list.

    Args:
        numbers: The list of numbers to check.

    Returns:
        The count of prime numbers in the list.

    Raises:
        AssertionError: If the input is not a list.
        AssertionError: If the list contains non-integer elements.

    Examples:
        >>> count_primes([2, 3, 4, 5])
        3
    """
    assert isinstance(numbers, list), "Input must be a list"

    prime_count = 0
    for num in numbers:
        assert isinstance(num, int), "All elements in the list must be integers"
        if is_prime(num):
            prime_count += 1

    return prime_count

# Example usage
numbers = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print("Number of prime numbers:", count_primes(numbers))
