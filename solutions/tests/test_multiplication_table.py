#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the multiplication_table function.

Test categories:
    - Standard cases: Verifies normal function behavior
    - Edge cases: Tests boundaries and extreme values
    - Defensive tests: Handles invalid or malicious inputs

Created on 03 Jan 2025
Team Number: 28
Team Name: MIT Alpha
Author: Salih Adam
"""

import unittest

from ..multiplication_table import multiplication_table


class TestMultiplicationTable(unittest.TestCase):
    """Test suite for the multiplication_table function"""

    # Standard test cases

    def test_standard_range(self):
        """It should return the standard multiplication table"""
        actual = multiplication_table(4, 1, 10)
        expected = """Table:
        4 x  1 = 4
        4 x  2 = 8
        4 x  3 = 12
        4 x  4 = 16
        4 x  5 = 20
        4 x  6 = 24
        4 x  7 = 28
        4 x  8 = 32
        4 x  9 = 36
        4 x 10 = 40
        End"""
        self.assertEqual(actual, expected)

    def test_negative_n_values(self):
        """It should return a table with negative results"""
        actual = multiplication_table(-9, 9, 11)
        expected = """Table:
        -9 x  9 = -81
        -9 x 10 = -90
        -9 x 11 = -99
        End"""
        self.assertEqual(actual, expected)

    def test_n_is_float(self):
        """It should return a table with rounded results"""
        actual = multiplication_table(9.07895, 22, 25)
        expected = """Table:
        9.07895 x 22 = 199.74
        9.07895 x 23 = 208.82
        9.07895 x 24 = 217.89
        9.07895 x 25 = 226.97
        End"""
        self.assertEqual(actual, expected)

    def test_high_multiplication_range(self):
        """It should return a table with large multipliers"""
        actual = multiplication_table(5, 5000, 5001)
        expected = """Table:
        5 x 5000 = 25000
        5 x 5001 = 25005
        End"""
        self.assertEqual(actual, expected)

    # Edge test cases

    def test_n_is_zero(self):
        """It should return a zero table"""
        actual = multiplication_table(0, 1, 3)
        expected = """Table:
        0 x 1 = 0
        0 x 2 = 0
        0 x 3 = 0
        End"""
        self.assertEqual(actual, expected)

    def test_very_small_n_in_a_short_low_multiplication_range(self):
        """It should round the results down to zero"""
        actual = multiplication_table(0.0001, 15, 17)
        expected = """Table:
        0.0001 x 15 = 0.0
        0.0001 x 16 = 0.0
        0.0001 x 17 = 0.0
        End"""
        self.assertEqual(actual, expected)

    def test_very_small_n_in_a_short_high_multiplication_range(self):
        """It should round up to the same result"""
        actual = multiplication_table(0.0001, 1000, 1002)
        expected = """Table:
        0.0001 x 1000 = 0.1
        0.0001 x 1001 = 0.1
        0.0001 x 1002 = 0.1
        End"""
        self.assertEqual(actual, expected)

    def test_n_equals_one(self):
        """It should return the multipliers as results"""
        actual = multiplication_table(1, 56, 60)
        expected = """Table:
        1 x 56 = 56
        1 x 57 = 57
        1 x 58 = 58
        1 x 59 = 59
        1 x 60 = 60
        End"""
        self.assertEqual(actual, expected)

    def test_a_repeating_fraction(self):
        """It should round up results"""
        actual = multiplication_table(2 / 3, 8, 10)
        expected = """Table:
        0.6666666666666666 x  8 = 5.33
        0.6666666666666666 x  9 = 6.0
        0.6666666666666666 x 10 = 6.67
        End"""
        self.assertEqual(actual, expected)

    def test_first_and_last_multipliers_are_equal(self):
        """It should return a one line table"""
        actual = multiplication_table(7, 11, 11)
        expected = """Table:
        7 x 11 = 77
        End"""
        self.assertEqual(actual, expected)

    # Defensive test cases

    def test_n_is_not_int_or_float(self):
        """It should raise an AssertionError for wrong input type"""
        with self.assertRaises(AssertionError):
            multiplication_table("2", 1, 4)

    def test_first_multiplier_is_not_int(self):
        """It should raise an AssertionError for wrong input type"""
        with self.assertRaises(AssertionError):
            multiplication_table(6.6, 3.5, 6)

    def test_last_multiplier_is_not_int(self):
        """It should raise an AssertionError for wrong input type"""
        with self.assertRaises(AssertionError):
            multiplication_table(22, 5, "10")

    def test_last_multiplier_is_less_than_one(self):
        """It should raise an AssertionError for wrong input range"""
        with self.assertRaises(AssertionError):
            multiplication_table(14, 1, -3)

    def test_first_multiplier_is_greater_than_last_multiplier(self):
        """It should raise an AssertionError for wrong input range"""
        with self.assertRaises(AssertionError):
            multiplication_table(12, 12, 5)


if __name__ == "__main__":
    unittest.main()
