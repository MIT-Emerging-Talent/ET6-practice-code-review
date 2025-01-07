#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the is_prime function.

This module contains unit tests for the is_prime function.
"""

import unittest
from ..is_prime import is_prime


class TestIsPrime(unittest.TestCase):
    """
    Test cases for the is_prime function.

    This class contains tests to verify the correctness of the is_prime function,
    including boundary cases, defensive assertions, and expected behavior for
    prime and non-prime numbers.
    """

    def test_negative_number(self):
        """
        Test that negative numbers are not considered prime.
        """
        actual = is_prime(-5)
        expected = False
        self.assertEqual(actual, expected)

    def test_zero(self):
        """
        Test that zero is not considered prime.
        """
        actual = is_prime(0)
        expected = False
        self.assertEqual(actual, expected)

    def test_one(self):
        """
        Test that one is not considered prime.
        """
        actual = is_prime(1)
        expected = False
        self.assertEqual(actual, expected)

    def test_small_prime(self):
        """
        Test that a small prime number returns True.
        """
        actual = is_prime(7)
        expected = True
        self.assertEqual(actual, expected)

    def test_small_non_prime(self):
        """
        Test that a small non-prime number returns False.
        """
        actual = is_prime(4)
        expected = False
        self.assertEqual(actual, expected)

    def test_large_prime(self):
        """
        Test that a large prime number returns True.
        """
        actual = is_prime(7919)
        expected = True
        self.assertEqual(actual, expected)

    def test_large_non_prime(self):
        """
        Test that a large non-prime number returns False.
        """
        actual = is_prime(8000)
        expected = False
        self.assertEqual(actual, expected)

    def test_defensive_assertion_non_integer(self):
        """
        Test that a non-integer input raises an AssertionError.
        """
        with self.assertRaises(AssertionError):
            is_prime("not a number")

    def test_boundary_case_two(self):
        """
        Test that two is correctly identified as prime.
        """
        actual = is_prime(2)
        expected = True
        self.assertEqual(actual, expected)

    def test_boundary_case_three(self):
        """
        Test that three is correctly identified as prime.
        """
        actual = is_prime(3)
        expected = True
        self.assertEqual(actual, expected)
