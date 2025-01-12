#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Unit tests for the is_leap_year function.

This test suite validates the behavior of the is_leap_year function,
including typical cases, boundary cases, and defensive assertions.
"""

import unittest

from solutions.leap_year_checker import is_leap_year


class TestIsLeapYear(unittest.TestCase):
    """
    Test cases for the is_leap_year function.
    """

    def test_common_leap_year(self):
        """Test a common leap year divisible by 4 but not 100."""
        self.assertTrue(is_leap_year(2024))

    def test_century_non_leap_year(self):
        """Test a century year that is not a leap year."""
        self.assertFalse(is_leap_year(1900))

    def test_century_leap_year(self):
        """Test a century year that is a leap year."""
        self.assertTrue(is_leap_year(2000))

    def test_non_leap_year(self):
        """Test a common year that is not a leap year."""
        self.assertFalse(is_leap_year(2023))

    def test_year_zero(self):
        """Test a year less than or equal to zero."""
        with self.assertRaises(ValueError):
            is_leap_year(0)

    def test_negative_year(self):
        """Test a negative year."""
        with self.assertRaises(ValueError):
            is_leap_year(-2024)

    def test_invalid_input(self):
        """Test invalid input that is not an integer."""
        with self.assertRaises(TypeError):
            is_leap_year("2024")

    def test_large_number(self):
        """Test a large number boundary case."""
        self.assertTrue(is_leap_year(4000000))
