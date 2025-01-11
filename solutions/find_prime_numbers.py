#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
This module defines the function `find_primes_up_to_n` to identify all prime numbers
up to a given integer \( N \). A prime number is greater than 1 and divisible only by 1 and itself.

"""


def is_prime(n: int) -> bool:
    r"""
    Checks if a given number is prime.

    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    """
    # Ensure n is an integer
    if not isinstance(n, int):
        raise AssertionError("Input must be an integer")

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_up_to_n(n: int) -> list:
    r"""
    Finds all prime numbers up to the given number \( N \).

    Parameters:
        n (int): The upper limit to find primes up to.

    Returns:
        list: A list of all prime numbers up to \( N \).

    Examples:
        >>> find_primes_up_to_n(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """
    # Ensure n is an integer and non-negative
    if not isinstance(n, int):
        raise AssertionError("Input must be an integer")
    if n < 0:
        raise AssertionError("Input must be a non-negative integer")

    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes
