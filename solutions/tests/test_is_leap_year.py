#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the is_leap_year function.

Test cases include:
    - Valid leap years (e.g., divisible by 4 but not 100, or divisible by 400).
    - Non-leap years (e.g., not divisible by 4, or divisible by 100 but not 400).
    - Years outside the Gregorian calendar (e.g., before 1583).
    - Invalid inputs (e.g., non-integer values).

Created on 2025-01-01
@author: Alexander Andom
"""

import unittest

from ..is_leap_year import is_leap_year


class TestIsLeapYear(unittest.TestCase):
    """Test the is_leap_year function"""

    def test_leap_year_2000(self):
        """Test for a leap year: 2000"""
        self.assertTrue(is_leap_year(2000))

    def test_non_leap_year_1900(self):
        """Test for a non-leap year: 1900"""
        self.assertFalse(is_leap_year(1900))

    def test_leap_year_2024(self):
        """Test for a leap year: 2024"""
        self.assertTrue(is_leap_year(2024))

    def test_non_leap_year_2023(self):
        """Test for a non-leap year: 2023"""
        self.assertFalse(is_leap_year(2023))

    def test_leap_year_2400(self):
        """Test for a leap year: 2400"""
        self.assertTrue(is_leap_year(2400))

    def test_non_leap_year_2100(self):
        """Test for a non-leap year: 2100"""
        self.assertFalse(is_leap_year(2100))

    def test_invalid_input_string(self):
        """Test for invalid input: string"""
        with self.assertRaises(AssertionError):
            is_leap_year("two thousand")

    def test_invalid_input_float(self):
        """Test for invalid input: float"""
        with self.assertRaises(AssertionError):
            is_leap_year(2000.5)

    def test_year_below_1583(self):
        """Test for a year below 1583 to raise AssertionError"""
        with self.assertRaises(AssertionError):
            is_leap_year(1500)


if __name__ == "__main__":
    unittest.main()
