#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the add_numbers function.

This module tests various scenarios for the `add_numbers` function
from the `solutions.sum` module to ensure its correctness.

Tests include:
    - Addition of integers
    - Addition of floats
    - Mixed types (integer and float)
    - Large numbers
    - Edge cases like zero and negatives
"""

import unittest
from solutions.sum import add_numbers


class TestAddNumbers(unittest.TestCase):
    """Unit tests for the add_numbers function."""

    def test_integers(self):
        """Test addition of two integers."""
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-3, 7), 4)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_floats(self):
        """Test addition of two floats."""
        self.assertEqual(add_numbers(3.5, 2.5), 6.0)
        self.assertEqual(add_numbers(-1.1, -2.9), -4.0)

    def test_integer_and_float(self):
        """Test addition of an integer and a float."""
        self.assertEqual(add_numbers(3, 2.5), 5.5)
        self.assertEqual(add_numbers(-3, 2.5), -0.5)

    def test_large_numbers(self):
        """Test addition of large numbers."""
        self.assertEqual(add_numbers(1_000_000, 2_000_000), 3_000_000)
        self.assertEqual(add_numbers(1e15, 1e15), 2e15)

    def test_edge_cases(self):
        """Test edge cases like zero and negatives."""
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(-5, 5), 0)
        self.assertEqual(add_numbers(-5, -5), -10)
