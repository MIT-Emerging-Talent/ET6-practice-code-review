#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains unit tests for the sum_of_evens function.

Test Categories:
  - Regular Passing Cases: Valid ranges of inputs.
  - Boundary Cases: Edge scenarios like zero or single values.
  - Defensive Cases: Invalid or negative inputs.
"""

import unittest

from sum_of_even import sum_of_evens


class TestSumOfEvens(unittest.TestCase):
    """
    Unit tests for the sum_of_evens function.
    """

    # Normal Cases
    def test_regular_range(self):
        """Test the sum of evens within a regular range."""
        self.assertEqual(sum_of_evens(10), 30)

    def test_small_range(self):
        """Test the sum of evens within a small range."""
        self.assertEqual(sum_of_evens(5), 6)

    def test_single_even(self):
        """Test when the range contains a single even number."""
        self.assertEqual(sum_of_evens(2), 2)

    # Boundary Cases
    def test_zero(self):
        """Test when the input is zero."""
        self.assertEqual(sum_of_evens(0), 0)

    def test_single_odd(self):
        """Test when the range contains a single odd number."""
        self.assertEqual(sum_of_evens(1), 0)

    # Defensive Cases
    def test_negative_input(self):
        """Test when the input is negative."""
        with self.assertRaises(ValueError):
            sum_of_evens(-5)

    def test_non_integer_input(self):
        """Test when the input is not an integer."""
        with self.assertRaises(AssertionError):
            sum_of_evens(5.5)
