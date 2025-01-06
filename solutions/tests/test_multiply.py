#! usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test for multiplication of two numbers

Created on 06.1.2025

@author:Simi-Solola


"""

import unittest

from solutions.multiply import multiply


class TestMultiply(unittest.TestCase):
    """
    Test case for the multiply function.
    """

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        result = multiply(2, 3)
        self.assertEqual(result, 6)

    def test_multiply_negative_number(self):
        """Test multiplying a positive and a negative number."""
        result = multiply(2, -3)
        self.assertEqual(result, -6)

    def test_multiply_non_numeric_input(self):
        """Test that non-numeric inputs raise an assertion error."""
        with self.assertRaises(AssertionError):
            multiply(2, "a")
