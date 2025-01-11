#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit Test for is_prime Function

This script contains a unit test for the `is_prime` function, which checks whether a given number
is prime or not.
A prime number is a number greater than 1 that has no divisors other than 1 and itself.

The test class `TestIsPrime` includes various test cases to verify that the function works correctly
for different types of inputs:
- Prime numbers
- Non-prime numbers
- Edge cases (such as 0, 1, and negative numbers)
- Larger prime numbers

Test cases include:
- Testing prime numbers like 2, 3, 5, and 7.
- Testing non-prime numbers like 1, 4, 6, 8, 9, etc.
- Checking edge cases such as 0 and negative numbers.

To run the tests, use the Python `unittest` framework.
The tests will provide feedback on the correctness
of the `is_prime` function.


"""

import unittest


def is_prime(number):
    """
    Check if a number is prime.

    Parameters:
    - number (int): The number to check.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False  # Numbers 1 and smaller are not prime
    for i in range(2, number):
        if number % i == 0:  # If a divisor is found, it is not prime
            return False
    return True  # If it has no divisors, it is a prime number


class TestIsPrime(unittest.TestCase):
    """Test case for the is_prime function."""

    def test_prime(self):
        """Test prime numbers."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(13))

    def test_non_prime(self):
        """Test non-prime numbers."""
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(14))

    def test_edge_case(self):
        """Test edge cases."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))
        self.assertTrue(is_prime(97))


if __name__ == "__main__":
    unittest.main()
