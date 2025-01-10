# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_is_prime.py

This module contains unit tests for the `is_prime` function, which determines
whether a given number is a prime number.

Author: Fahed Daibes
Date: Fri Jan 10 2025
Group: ET6-foundations-group-16

Tests:
- Valid inputs for prime and non-prime numbers.
- Edge cases, such as small numbers and negative numbers.
- Invalid inputs, such as non-integer types.
"""

import unittest
from solutions.is_prime import is_prime


def assert_prime(expected, number):
    """
    Custom assertion function to compare the result of is_prime with the expected value.

    Parameters:
    - expected (bool): The expected result (True if prime, False otherwise).
    - number (int): The input number to test.

    Raises:
    - AssertionError: If the result of is_prime does not match the expected value.
    """
    result = is_prime(number)
    assert result == expected, f"Expected {expected} for {number}, but got {result}."


class TestIsPrime(unittest.TestCase):
    """
    This test class contains unit tests for the `is_prime` function.

    Each test uses only one assertion with the custom `assert_prime` function.
    """

    def test_prime_two(self):
        """Test case for the smallest prime number."""
        assert_prime(True, 2)

    def test_prime_small(self):
        """Test case for a small prime number."""
        assert_prime(True, 17)

    def test_non_prime_small(self):
        """Test case for a small non-prime number."""
        assert_prime(False, 4)

    def test_non_prime_large(self):
        """Test case for a large non-prime number."""
        assert_prime(False, 100)

    def test_negative_number(self):
        """Test case for a negative number."""
        assert_prime(False, -5)

    def test_edge_case_zero(self):
        """Test case for zero."""
        assert_prime(False, 0)

    def test_edge_case_one(self):
        """Test case for one."""
        assert_prime(False, 1)

    def test_invalid_string(self):
        """Test case for an invalid string input."""
        with self.assertRaises(AssertionError):
            is_prime("eleven")

    def test_invalid_float(self):
        """Test case for an invalid float input."""
        with self.assertRaises(AssertionError):
            is_prime(6.8)


if __name__ == "__main__":
    unittest.main()
