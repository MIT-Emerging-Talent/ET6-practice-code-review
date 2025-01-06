#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test module for largest_perfect_square_less_than function.

Contains tests for checking the functionality of finding

the largest perfect square less than a given number.

Test categories:

    - Functionality tests: checking if the function correctly identifies
    the largest perfect square less than a number.

    - Edge tests:
        - Small positive numbers (the input is less than or equal to 1)
        - Perfect squares
        - Very large numbers
        - Zero

    - Defensive tests: ensuring the function handles invalid inputs such as:
        - Negative numbers
        - Non-numeric inputs


Created on 2025-01-06
@author: Huda Alamassi
"""

import unittest

from solutions.largest_perfect_square_less_than_number import (
    largest_perfect_square_less_than_number,
)


class TestLargestPerfectSquareLessThanNumber(unittest.TestCase):
    """Test the largest_perfect_square_less_than_number function."""

    # Test functionality
    def test_integer_input(self):
        """Test that the function returns the largest perfect square less than the input integer."""
        actual = largest_perfect_square_less_than_number(50)
        self.assertEqual(actual, 49)

    def test_float_input(self):
        """Test that the function returns the largest perfect square less than the input float."""
        actual = largest_perfect_square_less_than_number(2.6)
        self.assertEqual(actual, 1)

    def test_perfect_square_condition(self):
        """Test the condition when the input number is close to a perfect square."""
        actual = largest_perfect_square_less_than_number(16.5)
        self.assertEqual(actual, 9)

    # Test edge cases
    def test_small_positive_number(self):
        """It should return 0 if you pass small positive numbers (less than or equal to 1)."""
        actual = largest_perfect_square_less_than_number(0.5)
        self.assertEqual(actual, 0)

    def test_perfect_square(self):
        """Test when the input is a perfect square."""
        actual = largest_perfect_square_less_than_number(16)
        self.assertEqual(actual, 9)

    def test_very_large_number(self):
        """Test with a very large number."""
        actual = largest_perfect_square_less_than_number(10**6)
        self.assertEqual(actual, 998001)

    def test_zero(self):
        """It should return 0 if you pass 0"""
        actual = largest_perfect_square_less_than_number(0)
        self.assertEqual(actual, 0)

    # Test defensive assertions
    def test_defensive_assertion_for_negative_input(self):
        """Test that an assertion is raised if the input is a negative number."""
        with self.assertRaises(AssertionError):
            largest_perfect_square_less_than_number(-10)

    def test_defensive_assertion_for_non_numeric_input(self):
        """Test that an assertion is raised if the input is not a number."""
        with self.assertRaises(AssertionError):
            largest_perfect_square_less_than_number("abc")
