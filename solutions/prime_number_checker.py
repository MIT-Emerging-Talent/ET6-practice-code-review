#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for checking if a number is prime.

Module contents: check if an input number is a prime number.
Created on 2024-12-30
Author: Hussaini Ahmed
"""


def is_prime(number: int) -> bool:
    """
    Checks if a number is prime.

    Parameters:
        number (int): Input number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        TypeError: If the input is not an integer.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(13)
        True
        >>> is_prime(1)
        False
        >>> is_prime(0)
        False
        >>> is_prime(-5)
        False
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")

    if number <= 1:
        return False  # 0, 1, and negative numbers are not prime

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Found a divisor, not prime

    return True  # No divisors found, the number is prime
