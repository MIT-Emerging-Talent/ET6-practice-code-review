#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
This module defines the functions `is_prime` and `count_primes` for checking primality
and counting prime numbers in a list.

@uthor: Zeinab Shadabshoar
Date: 09 01 2025

"""


def is_prime(n: int) -> bool:
    r"""
    Checks if a given number is prime.

    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative integer.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(numbers: list) -> int:
    r"""
    Counts the number of prime numbers in a list.

    Parameters:
        numbers (list): The list of numbers to check.

    Returns:
        int: The count of prime numbers in the list.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.

    Examples:
        >>> count_primes([2, 3, 4, 5])
        3
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    prime_count = 0
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements in the list must be integers")
        if is_prime(num):
            prime_count += 1
    return prime_count


# Example usage
numbers = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print("Number of prime numbers:", count_primes(numbers))
