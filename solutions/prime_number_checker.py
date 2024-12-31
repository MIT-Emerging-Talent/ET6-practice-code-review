#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for checking if a number is prime.

Module contents: check if an input number is a prime number.
Created on 2024-12-30
Author: Hussaini Ahmed
"""


def prime_number_checker(number: int) -> bool:
    """
    Checks if a number is prime.

    Parameters:
        number (int): Input number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        TypeError: If the input is not an integer.

    Examples:
        >>> prime_number_checker(2)
        True
        >>> prime_number_checker(3)
        True
        >>> prime_number_checker(4)
        False
        >>> prime_number_checker(13)
        True
        >>> prime_number_checker(1)
        False
        >>> prime_number_checker(0)
        False
        >>> prime_number_checker(-5)
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
