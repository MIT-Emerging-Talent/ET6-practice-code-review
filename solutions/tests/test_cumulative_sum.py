#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: test_cumulative_sum

Description:
    This module contains test cases for the `cumulative_sum` function defined
    in the `cumulative_sum.py` module. It tests the function's behavior with
    various input scenarios, ensuring that it handles different edge cases and
    returns the expected cumulative sums.

Test Categories:
    - Standard cases: List of positive integers, negative integers, and floating-point numbers.
    - Edge cases: Empty list, single-element list, list with zeros, large number list.
    - Defensive tests: None input, Non-list inputs, list with non-numeric elements.

Author: Falaq Youniss
Date: 29/12/2024
"""

import unittest
from ..cumulative_sum import cumulative_sum


class TestCumulativeSum(unittest.TestCase):
    """Test for cumulative_sum function that handles different cases"""

    # Standard test cases
    def test_positive_int(self):
        """It should return a cumulative list of positive integers."""
        self.assertEqual(cumulative_sum([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_negative_int(self):
        """It should return a cumulative list of negative integers."""
        self.assertEqual(cumulative_sum([-1, -2, -3, -4]), [-1, -3, -6, -10])

    def test_positive_float(self):
        """It should return a cumulative list of positive floats."""
        self.assertEqual(cumulative_sum([1.0, 2.0, 3.0, 4.0]), [1.0, 3.0, 6.0, 10.0])

    def test_negative_float(self):
        """It should return a cumulative list of negative floats."""
        self.assertEqual(
            cumulative_sum([-1.0, -2.0, -3.0, -4.0]), [-1.0, -3.0, -6.0, -10.0]
        )

    def test_positive_negative(self):
        """It should return a cumulative list of negative and positive integers."""
        self.assertEqual(cumulative_sum([-1, 2, -3, 4]), [-1, 1, -2, 2])

    def test_integer_float(self):
        """It should return a cumulative list of integers and floats."""
        self.assertEqual(cumulative_sum([1.0, 2, 3.0, 4]), [1, 3, 6.0, 10.0])

    def test_combination(self):
        """It should return a cumulative list of mixed positive and negative integers/floats."""
        self.assertEqual(cumulative_sum([1.0, -2, -3.0, 4]), [1, -1, -4, 0])

    def test_same(self):
        """It should return a cumulative list of same positive integers."""
        self.assertEqual(cumulative_sum([3, 3, 3]), [3, 6, 9])

    # Edge cases
    def test_zero(self):
        """It should return a list of zeros."""
        self.assertEqual(cumulative_sum([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_empty(self):
        """It should return an empty list."""
        self.assertEqual(cumulative_sum([]), [])

    def test_one(self):
        """It should return the same single-item list."""
        self.assertEqual(cumulative_sum([1]), [1])

    def test_large_numbers(self):
        """It should correctly handle large numbers."""
        self.assertEqual(cumulative_sum([1e6, 2e6, 3e6]), [1e6, 3e6, 6e6])

    # Defensive tests
    def test_none(self):
        """It should raise AssertionError for None input."""
        with self.assertRaises(AssertionError):
            cumulative_sum(None)

    def test_not_list(self):
        """It should raise AssertionError for non-list input."""
        with self.assertRaises(AssertionError):
            cumulative_sum("hello")

    def test_not_num(self):
        """It should raise AssertionError for non-numeric list elements."""
        with self.assertRaises(AssertionError):
            cumulative_sum([1, "cat", 3])
