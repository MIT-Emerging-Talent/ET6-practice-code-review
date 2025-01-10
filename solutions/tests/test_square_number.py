#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Test module for square_number function.
Test categories:
    - Standard cases: typical numbers
    - Edge cases: zero, negative numbers, floating-point values
    - Defensive tests: wrong input types, assertions
"""

import unittest

from solutions.square_number import square_number


class TestSquareNumber(unittest.TestCase):
    """Test suite for the square_number function."""

    # Standard test cases
    def test_integers(self):
        """It should return the square of an integer"""
        self.assertEqual(square_number(5), 25)

    def test_floats(self):
        """It should return the square of a float"""
        self.assertEqual(square_number(3.5), 12.25)

    # Edge cases
    def test_zero(self):
        """It should return 0 when input is 0"""
        self.assertEqual(square_number(0), 0)

    def test_negative(self):
        """It should return the square of a negative number"""
        self.assertEqual(square_number(-4), 16)

    # Defensive tests
    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            square_number(None)

    def test_string_input(self):
        """It should raise AssertionError for string input"""
        with self.assertRaises(AssertionError):
            square_number("string")


if __name__ == "_main_":
    unittest.main()
