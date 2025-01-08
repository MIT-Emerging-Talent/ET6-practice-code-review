#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides unit tests for the prime_finder function.

Test Categories:
Regular Passing Cases - Tests with typical inputs
Rare or Edge Cases - Tests with empty lists, single elements, and duplicates
Defensive Cases - Tests that verify error handling for invalid inputs

Created on: 2025/1/6
Author: ZaidMazen1
"""

import unittest

from ..prime_finder import prime_finder


class TestPrimeFinder(unittest.TestCase):
    """
    Unit tests for the prime_finder function.
    """

    # Regular Passing Cases

    def test_primes_in_range(self):
        """
        Tests with a range of integers that contain primes.
        """
        self.assertEqual(prime_finder(1, 6), [2, 3, 5])

    def test_beginning_with_prime(self):
        """
        Tests with a range of integers that begins with a prime.
        """
        self.assertEqual(prime_finder(2, 10), [2, 3, 5, 7])

    def test_ending_with_prime(self):
        """
        Tests with a range of integers that start with a prime.
        """
        self.assertEqual(prime_finder(1, 11), [2, 3, 5, 7, 11])

    def test_beginning_and_ending_with_prime(self):
        """
        Tests with a range of integers that start and end with a prime.
        """
        self.assertEqual(prime_finder(2, 11), [2, 3, 5, 7, 11])

    # Rare or Edge Cases

    def test_large_range(self):
        """
        Tests with a large range of integers that contain primes.
        """
        self.assertEqual(
            prime_finder(0, 100),
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
            ],
        )

    def test_empty_range(self):
        """
        Tests with an empty range.
        """
        self.assertEqual(prime_finder(0, 0), [])

    # Defensive Cases That Raise Errors

    def test_non_integer_elements(self):
        """
        Tests with non-integer elements.
        """
        with self.assertRaises(AssertionError):
            prime_finder("cat", "dog")

    def test_invalid_range(self):
        """
        Tests with an invalid range.
        """
        with self.assertRaises(ValueError):
            prime_finder(7, 2)

    def test_negative_elements(self):
        """
        Tests with negative elements.
        """
        with self.assertRaises(ValueError):
            prime_finder(-5, -2)
