#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The goal of this challenge is to count how many prime numbers are present in a given list of integers. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

  Created on: 09/01/25
@author: Zeinab Shadabshoar
"""


def is_prime(n: int) -> bool:
    """
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
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(numbers: list) -> int:
    """
    Counts the number of prime numbers in a list.

    Parameters:
        numbers (list): The list of numbers to check.

    Returns:
        int: The count of prime numbers in the list.

    Examples:
        >>> count_primes([2, 3, 4, 5])
        3
    """
    prime_count = 0
    for num in numbers:
        if is_prime(num):
            prime_count += 1
    return prime_count

# Example usage
numbers = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print("Number of prime numbers:", count_primes(numbers))
