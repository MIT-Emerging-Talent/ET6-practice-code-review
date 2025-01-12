#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test for multiplying of 2 numbers

Created on 06.01.2025

@author:Simi-Solola


"""

import unittest

from solutions.multiply import multiply


class TestMultiply(unittest.TestCase):
    """
    Test case for the multiply function.
    Tests include:
    - Positive numbers
    - Negative numbers
    - Error case for non-numeric input
    """

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        result = multiply(2, 3)
        self.assertEqual(result, 6.0)

    def test_multiply_negative_number(self):
        """Test multiplying a positive number by a negative number."""
        result = multiply(-2, 3)
        self.assertEqual(result, -6.0)

    def test_multiply_non_numeric_input(self):
        """Test that non-numeric inputs raise an assertion error."""
        with self.assertRaises(AssertionError):
            multiply(2, "a")

    def test_multiply_float_input(self):
        """Test multiplying two floating-point numbers."""
        result = multiply(2.5, 4.0)
        self.assertEqual(result, 10.0)


if __name__ == "__main__":
    unittest.main()
