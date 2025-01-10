"""
Unit tests for the leap_year_checker function.

Tests the behavior of the leap_year_checker function across a range of cases:
    - Valid leap years
    - Non-leap years
    - Invalid input types
    - Boundary cases
Created on 2024-12-31
Author: Hussaini Ahmed
"""

import unittest

from solutions.leap_year_checker import leap_year_checker


class TestIsLeapYear(unittest.TestCase):
    """Test cases for the leap_year_checker function."""

    def test_valid_leap_year(self):
        """Ensure the function correctly identifies leap years."""
        self.assertTrue(
            leap_year_checker(2020), "2020 should be identified as a leap year."
        )

    def test_non_leap_year(self):
        """Ensure the function correctly identifies non-leap years."""
        self.assertFalse(
            leap_year_checker(2021), "2021 should not be identified as a leap year."
        )

    def test_century_year_not_leap(self):
        """Ensure century years that are not divisible by 400 are non-leap years."""
        self.assertFalse(
            leap_year_checker(1900), "1900 should not be identified as a leap year."
        )

    def test_century_year_leap(self):
        """Ensure century years divisible by 400 are leap years."""
        self.assertTrue(
            leap_year_checker(2000), "2000 should be identified as a leap year."
        )

    def test_invalid_input_type_string(self):
        """Ensure the function raises a TypeError for string input."""
        with self.assertRaises(TypeError):
            leap_year_checker("2020")

    def test_invalid_input_type_float(self):
        """Ensure the function raises a TypeError for float input."""
        with self.assertRaises(TypeError):
            leap_year_checker(2020.5)

    def test_negative_year(self):
        """Ensure the function raises a ValueError for negative year input."""
        with self.assertRaises(ValueError):
            leap_year_checker(-2020)

    def test_zero_year(self):
        """Ensure the function raises a ValueError for year 0."""
        with self.assertRaises(ValueError):
            leap_year_checker(0)

    def test_boundary_case_minimum_year(self):
        """Ensure the function handles the smallest valid year correctly."""
        self.assertFalse(leap_year_checker(1), "Year 1 should not be a leap year.")

    def test_boundary_case_first_leap_year(self):
        """Ensure the function correctly identifies the first leap year."""
        self.assertTrue(
            leap_year_checker(4), "Year 4 should be identified as a leap year."
        )


if __name__ == "__main__":
    unittest.main()
