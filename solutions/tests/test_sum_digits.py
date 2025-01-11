"""
Unit tests for the sum_digits function.

This test suite validates the functionality of the sum_digits function, ensuring
it correctly computes the sum of the digits for various types of inputs and handles
invalid inputs appropriately.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from solutions.sum_digits import sum_digits


class TestSumDigits(unittest.TestCase):
    def test_single_digit(self):
        """Test sum_digits with a single-digit input."""
        self.assertEqual(sum_digits(9), 9)

    def test_multiple_digits(self):
        """Test sum_digits with a multi-digit input."""
        self.assertEqual(sum_digits(456), 15)

    def test_large_number(self):
        """Test sum_digits with a large number input."""
        self.assertEqual(sum_digits(123456789), 45)

    def test_edge_case(self):
        """Test sum_digits with an edge case where digits are mixed (e.g., 101)."""
        self.assertEqual(sum_digits(101), 2)

    def test_negative_input(self):
        """Test sum_digits raises ValueError for negative input."""
        with self.assertRaises(ValueError):
            sum_digits(-1)

    def test_string_input(self):
        """Test sum_digits raises ValueError when input is a string."""
        with self.assertRaises(ValueError):
            sum_digits("123")

    def test_none_input(self):
        """Test sum_digits raises ValueError when input is None."""
        with self.assertRaises(ValueError):
            sum_digits(None)

    def test_float_input(self):
        """Test sum_digits raises ValueError when input is a float."""
        with self.assertRaises(ValueError):
            sum_digits(12.34)


if __name__ == "__main__":
    unittest.main()
