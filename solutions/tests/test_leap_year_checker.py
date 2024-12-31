"""
Unit tests for the is_leap_year function.

Tests the behavior of the is_leap_year function across a range of cases:
    - Valid leap years
    - Non-leap years
    - Invalid input types
    - Boundary cases
Created on 2024-12-31
Author: Hussaini Ahmed
"""

import unittest

from solutions.leap_year_checker import is_leap_year


class TestIsLeapYear(unittest.TestCase):
    """Test cases for the is_leap_year function."""

    def test_valid_leap_years(self):
        """Test known leap years."""
        self.assertTrue(is_leap_year(2020))
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(1600))

    def test_non_leap_years(self):
        """Test known non-leap years."""
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2021))
        self.assertFalse(is_leap_year(2019))

    def test_invalid_input(self):
        """Test invalid inputs for the function."""
        with self.assertRaises(TypeError):
            is_leap_year("2020")
        with self.assertRaises(TypeError):
            is_leap_year(2020.5)
        with self.assertRaises(ValueError):
            is_leap_year(-2020)
        with self.assertRaises(ValueError):
            is_leap_year(0)

    def test_boundary_cases(self):
        """Test edge cases for leap year logic."""
        self.assertFalse(is_leap_year(1))  # Minimum valid year
        self.assertTrue(is_leap_year(4))  # First leap year


if __name__ == "__main__":
    unittest.main()
