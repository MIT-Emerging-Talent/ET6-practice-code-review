#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the is_positive function.

@author: Luyando .E. Chitindi
"""

import unittest
from solutions.is_positive import is_positive


class TestIsPositive(unittest.TestCase):
    """Test the is_positive function"""

    def test_positive_number(self):
        """It should evaluate 4 to True"""
        actual = is_positive(4)
        expected = True
        self.assertEqual(actual, expected)

    def test_negative_number(self):
        """It should evaluate -3 to False"""
        actual = is_positive(-3)
        expected = False
        self.assertEqual(actual, expected)

    def test_zero(self):
        """It should evaluate 0 to False"""
        actual = is_positive(0)
        expected = False
        self.assertEqual(actual, expected)

    def test_non_integer_input(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            is_positive(3.5)

        with self.assertRaises(AssertionError):
            is_positive("string")


if __name__ == "__main__":
    unittest.main()
