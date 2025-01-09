#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for multiply_numbers function.

Test categories:
    - Standard cases: typical numbers
    - Edge cases: zero, negative numbers
    - Defensive tests: wrong input types, assertions

"""

import unittest

from solutions.multiplication import multiply_numbers


class TestMultiplyNumbers(unittest.TestCase):
    """Test suite for the multiply_numbers function."""

    # Standard test cases
    def test_positive_integers(self):
        """It should return the product of two positive integers"""
        self.assertEqual(multiply_numbers(5, 3), 15)

    def test_floats(self):
        """It should return the product of two floats"""
        self.assertEqual(multiply_numbers(4.5, 2.0), 9.0)

    def test_mixed_signs(self):
        """It should return the product of one negative integer and one positive integer"""
        self.assertEqual(multiply_numbers(-7, 6), -42)

    # Edge cases
    def test_zero(self):
        """It should return the product when multiplying by zero"""
        self.assertEqual(multiply_numbers(0, 12), 0)

    def test_negative_integers(self):
        """It should return the product of two negative integers"""
        self.assertEqual(multiply_numbers(-3, -4), 12)

    def test_float_and_integer(self):
        """It should return the product of a float and an integer"""
        self.assertEqual(multiply_numbers(2.5, 4), 10.0)


if __name__ == "__main__":  # noqa: F821
    unittest.main()
