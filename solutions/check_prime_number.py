#!/usr/bin/env python3
"""
This function check number for prime or not.

Author: Özgür ÖZBEK
Date: 11th January 2025
Group: ET6-foundations-group-16
"""


def check_prime_number(number: int) -> bool:
    """Checks if a number is prime.

    A prime number is a number greater than 1 that has no divisors other than 1 and itself.
    This function checks if the given number is prime by testing divisibility for all numbers
    from 2 to the square root of the number.

    Parameters:
        number: int, the number to check for prime. Must be greater than 1.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        AssertionError: If the number is less than or equal to 1.

    Examples:
        >>> check_prime_number(2)
        True
        >>> check_prime_number(3)
        True
        >>> check_prime_number(4)
        False
        >>> check_prime_number(13)
        True
        >>> check_prime_number(1)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError: Number must be greater than 1
    """
    assert number > 1, "Number must be greater than 1"
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
