#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The goal of this challenge is to count how many prime numbers are present in a given list of integers.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Created on: 09/01/25
@author: Zeinab shadabshoar
"""

def is_prime(n: int) -> bool:
    r"""
    Checks if a given number is prime.

    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        AssertionError: If the input is not an integer.
        AssertionError: If the input is a negative number.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    """
    # validate input type
    assert isinstance(n, int), "Input must be an integer"

    # ensure that the number is positive
    assert n >= 0, "Input must be a non-negative integer"

    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
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
        AssertionError: If the input is not a list.
        AssertionError: If the list contains non-integer elements.

    Examples:
        >>> count_primes([2, 3, 4, 5])
        3
    """
    # validate input type
    assert isinstance(numbers, list), "Input must be a list"

    prime_count = 0

    for num in numbers:
        # ensure that each element in the list is an integer
        assert isinstance(num, int), "All elements in the list must be integers"

        if is_prime(num):
            prime_count += 1

    return prime_count

# Example usage
numbers = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print("Number of prime numbers:", count_primes(numbers))
