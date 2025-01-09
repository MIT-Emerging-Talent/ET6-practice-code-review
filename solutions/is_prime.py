#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for determining whether a number is prime.

Module contents:
    - is_prime: checks if a given number is prime.

Created on Jan 06, 2025
@author: Ibrahim Elmisbah
"""


def is_prime(n: int) -> bool:
    """Determine if a number is prime.

    Parameters:
        n: int, the number to check if prime

    Returns:
        bool: True if the number is prime, False otherwise

    Raises:
        AssertionError: if the argument is not an integer

    >>> is_prime(23)
    True
    >>> is_prime(10)
    False
    >>> is_prime(17)
    True
    >>> is_prime(1)
    False
    >>> is_prime(-5)
    False
    """
    # Ensure the input is an integer
    assert isinstance(n, int), "input must be an integer"

    # If n is less than or equal to 1, return False (not prime)
    if n <= 1:
        return False

    # Check divisibility from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by any number between 2 and sqrt(n), it's not prime
        if n % i == 0:
            return False

    # If no divisors were found, n is prime
    return True
