#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for find_two_sum_indices function.

Created on 2025-01-05

Author: Emmanuel
"""

import unittest

from ..find_max_number import find_max_number


class TestFindMaximum(unittest.TestCase):
    """
    Unit tests for the   find_max_number function.
    """

    def test_first_number_greater(self):
        # Test when the first number is greater
        self.assertEqual(find_max_number(5, 3), 5)

    def test_second_number_greater(self):
        # Test when the second number is greater
        self.assertEqual(find_max_number(2, 8), 8)

    def test_numbers_equal(self):
        # Test when both numbers are equal
        self.assertEqual(find_max_number(7, 7), 7)

    def test_negative_numbers(self):
        # Test with negative numbers
        self.assertEqual(find_max_number(-5, -10), -5)
        self.assertEqual(find_max_number(-20, -3), -3)

    def test_mix_positive_and_negative_numbers(self):
        # Test with a mix of positive and negative numbers
        self.assertEqual(find_max_number(-5, 10), 10)
        self.assertEqual(find_max_number(15, -8), 15)

    def test_floats(self):
        # Test with floating-point numbers
        with self.assertRaises(AssertionError):
            find_max_number(-2.5, -1.5)

    def test_large_numbers(self):
        # Test with very large numbers
        self.assertEqual(find_max_number(1_000_000_000, 2_000_000_000), 2_000_000_000)
        self.assertEqual(find_max_number(-1_000_000_000, 0), 0)

    def test_zero(self):
        # Test when one or both numbers are zero
        self.assertEqual(find_max_number(0, 5), 5)
        self.assertEqual(find_max_number(0, -5), 0)

    def test_same_number_repeated(self):
        # Test multiple calls with the same numbers
        for _ in range(5):  # Repeat the test 5 times
            self.assertEqual(find_max_number(42, 42), 42)

    def test_non_numeric_values(self):
        # Test with invalid input types
        with self.assertRaises(AssertionError):
            find_max_number("10", 20)  # First argument is a string
        with self.assertRaises(AssertionError):
            find_max_number(10, "20")  # Second argument is a string
        with self.assertRaises(AssertionError):
            find_max_number("10", "20")  # Both arguments are strings
        with self.assertRaises(AssertionError):
            find_max_number(None, 10)  # First argument is None
        with self.assertRaises(AssertionError):
            find_max_number(10, None)  # Second argument is None


if __name__ == "__main__":
    # Run all unit tests
    unittest.main()
