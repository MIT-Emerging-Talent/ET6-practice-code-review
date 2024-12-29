#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prime Number Checker
=============================
This script provides a function to check if a number is a prime number and prints the result.

Author: Banu Ozyilmaz
Created on: 12-29-2024
"""


def is_prime(n):
    """
    Check if a number is a prime number.

    Arguments:
        n (int): The number to check.

    Returns:
        bool: True if n is a prime number, False otherwise.

    Raises:
        AssertionError: If n is not an integer.
        AssertionError: If n is a negative number.

    Examples:
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
        >>> is_prime(18)
        False
        >>> is_prime(-6)
        Traceback (most recent call last):
            ...
        AssertionError: The argument must be a non-negative integer.
        >>> is_prime(5.5)
        Traceback (most recent call last):
            ...
        AssertionError: The argument should be an integer.
    """
    # Input validation
    assert isinstance(n, int), "The argument should be an integer."
    assert n >= 0, "The argument must be a non-negative integer."

    # Prime numbers are greater than 1
    if n <= 1:
        print(f"{n} is NOT a prime number")
        return False

    # Check for factors from 2 up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by any number in this range, it is not prime
        if n % i == 0:
            print(f"{n} is NOT a prime number")
            return False

    # If no factors are found, n is prime
    print(f"{n} is a prime number")
    return True
