#!/usr/bin/env python3
# -- coding: utf-8 --
# File: tests/test_multiply_function.py
"""
This module contains unit tests for the `multiply` function in `multiply_function.py`.
The tests cover various scenarios including valid inputs, defensive assertions, and boundary cases.
"""

import unittest
from ..multiply import multiply

class TestMultiplyFunction(unittest.TestCase):
    """Unit tests for the `multiply` function."""

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        self.assertEqual(multiply(-2, -5), 10)

    def test_multiply_positive_and_negative(self):
        """Test multiplying a positive and a negative number."""
        self.assertEqual(multiply(-1.5, 2), -3.0)

    def test_multiply_with_zero(self):
        """Test multiplying any number by zero."""
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(7, 0), 0)

    def test_multiply_float_numbers(self):
        """Test multiplying two floating-point numbers."""
        self.assertAlmostEqual(multiply(2.5, 4.2), 10.5)

    def test_multiply_invalid_first_argument(self):
        """Test error when the first argument is not a number."""
        with self.assertRaises(TypeError):
            multiply("a", 5)

    def test_multiply_invalid_second_argument(self):
        """Test error when the second argument is not a number."""
        with self.assertRaises(TypeError):
            multiply(3, None)

if __name__ == "__main__":
    unittest.main()
