#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test module for leap_year function.
Test categories:
    - Standard cases: typical leap years, non-leap years
    - Edge cases: boundary years, negative years
    - Defensive tests: wrong input types, assertions
Created on 2025-01-03
Author: Solara Hamza
"""

import unittest
from ..leap_year import leap_year


class TestLeapYear(unittest.TestCase):
    """Test suite for the leap_year function."""

    # Standard test cases
    def test_true_leap_year(self):
        """It should return True for leap years."""
        self.assertTrue(leap_year(2000))
        self.assertTrue(leap_year(2024))

    def test_false_leap_year(self):
        """It should return False for non-leap years."""
        self.assertFalse(leap_year(2025))
        self.assertFalse(leap_year(2003))

    def test_century_non_leap_year(self):
        """It should return False for non-leap century years."""
        self.assertFalse(leap_year(1900))
        self.assertFalse(leap_year(2100))

    def test_century_leap_year(self):
        """It should return True for leap century years."""
        self.assertTrue(leap_year(2000))
        self.assertTrue(leap_year(2400))

    # Defensive tests
    def test_wrong_input(self):
        """It should raise TypeError for empty input."""
        with self.assertRaises(TypeError):
            leap_year("string")

    def test_negative_year(self):
        """It should raise ValueError for negative years."""
        with self.assertRaises(ValueError):
            leap_year(-2000)

    # Edge cases
    def test_empty_input(self):
        """It should raise TypeError for empty input."""
        with self.assertRaises(ValueError):
            leap_year("")


if __name__ == "__main__":
    unittest.main()
