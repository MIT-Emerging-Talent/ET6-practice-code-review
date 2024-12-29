#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Banu Ozyilmaz
Created on: 12-29-2024

This script contains unit tests for the prime number checker function using the unittest module.
"""

import unittest
from solutions.prime_number_checker import is_prime


class TestPrimeFunction(unittest.TestCase):
    """Unit tests for the prime number checker function"""

    # Standard tests for known prime and non-prime numbers
    def test_standard_cases(self):
        """Standard tests for known prime and non-prime numbers"""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))

    # Edge cases, including smallest primes and non-primes, and large primes
    def test_edge_cases(self):
        """Edge cases for smallest primes, non-primes, and large primes"""
        self.assertFalse(is_prime(0))  # Not a prime
        self.assertFalse(is_prime(1))  # Not a prime
        self.assertTrue(is_prime(2))  # Smallest prime number
        self.assertTrue(is_prime(7919))  # A large prime number
        self.assertTrue(is_prime(104729))  # Another large prime number

    # Defensive tests to ensure the function behaves correctly with non-integer values
    def test_non_integer_input(self):
        """Defensive tests for non-integer values"""
        with self.assertRaises(AssertionError):  # Expecting an AssertionError for float
            is_prime(2.5)
        with self.assertRaises(
            AssertionError
        ):  # Expecting an AssertionError for string
            is_prime("string")
        with self.assertRaises(
            AssertionError
        ):  # Expecting an AssertionError for negative integer
            is_prime(-10)

    # Additional tests for negative numbers and corner cases
    def test_negative_numbers(self):
        """Tests for negative numbers"""
        with self.assertRaises(AssertionError):
            is_prime(-5)
        with self.assertRaises(AssertionError):
            is_prime(-7)


if __name__ == "__main__":
    unittest.main()
