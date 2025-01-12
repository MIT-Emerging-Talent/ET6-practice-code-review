"""
Unit tests for the `is_odd_or_even` function.

These tests verify the behavior of the `is_odd_or_even` function, including
defensive checks for invalid inputs and boundary cases.

Author: Tamara Saqer
Date: 2025-01-10
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from solutions.is_odd_or_even import is_odd_or_even


class TestIsOddOrEven(unittest.TestCase):
    """
    Test cases for the `is_odd_or_even` function.
    """

    def test_even_number(self):
        """
        Test that an even number returns 'Even'.
        """
        result = is_odd_or_even(4)
        self.assertEqual(result, "Even")

    def test_odd_number(self):
        """
        Test that an odd number returns 'Odd'.
        """
        result = is_odd_or_even(7)
        self.assertEqual(result, "Odd")

    def test_zero(self):
        """
        Test that zero returns 'Even'.
        """
        result = is_odd_or_even(0)
        self.assertEqual(result, "Even")

    def test_negative_odd(self):
        """
        Test that a negative odd number returns 'Odd'.
        """
        result = is_odd_or_even(-3)
        self.assertEqual(result, "Odd")

    def test_negative_even(self):
        """
        Test that a negative even number returns 'Even'.
        """
        result = is_odd_or_even(-2)
        self.assertEqual(result, "Even")

    def test_non_integer_input_string(self):
        """
        Test that a non-integer input (string) raises an AssertionError.
        """
        with self.assertRaises(AssertionError):
            is_odd_or_even("a")

    def test_non_integer_input_float(self):
        """
        Test that a non-integer input (float) raises an AssertionError.
        """
        with self.assertRaises(AssertionError):
            is_odd_or_even(3.14)


if __name__ == "__main__":
    unittest.main()
