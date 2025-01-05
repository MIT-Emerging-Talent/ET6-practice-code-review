#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the celsius_to_fahrenheit function.
Contains comprehensive tests to verify temperature conversion functionality.

Test categories:
    - Standard cases: typical temperatures in Celsius
    - Edge cases: extreme values, floating-point precision, zero and negative zero
    - Defensive tests: invalid inputs (non-numeric types)

Created: 04/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Shaima Mohamed
"""

import unittest
from ..celsius_to_fahrenheit import celsius_to_fahrenheit


class TestCelsiusToFahrenheit(unittest.TestCase):
    """Test the celsius_to_fahrenheit function"""

    # Test Standard Cases
    def test_zero_celsius(self):
        """It should convert 0°C to 32°F"""
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_100_celsius(self):
        """It should convert 100°C to 212°F"""
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_negative_40_celsius(self):
        """It should convert -40°C to -40°F (same value)"""
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_float_input(self):
        """It should convert 25.5°C to 77.9°F"""
        self.assertEqual(celsius_to_fahrenheit(25.5), 77.9)

    # Test Edge Cases
    def test_large_temperature(self):
        """It should handle large temperatures correctly"""
        self.assertEqual(celsius_to_fahrenheit(1000), 1832.0)

    def test_very_small_fraction(self):
        """It should correctly convert very small fractional Celsius values"""
        self.assertAlmostEqual(celsius_to_fahrenheit(0.0001), 32.00018)

    def test_absolute_zero(self):
        """Test the conversion at absolute zero."""
        self.assertEqual(celsius_to_fahrenheit(-273.15), -459.67)

    def test_edge_case_around_freezing(self):
        """It should handle temperatures just below freezing"""
        self.assertAlmostEqual(celsius_to_fahrenheit(-0.1), 31.82)

    def test_negative_zero(self):
        """It should correctly convert -0.0°C to 32.0°F"""
        self.assertEqual(celsius_to_fahrenheit(-0.0), 32.0)

    # Test Defensive Assertions
    def test_non_numeric_input(self):
        """It should raise an assertion error if input is a string"""
        with self.assertRaises(AssertionError):
            celsius_to_fahrenheit("100")

    def test_invalid_type_list(self):
        """It should raise AssertionError for list input"""
        with self.assertRaises(AssertionError):
            celsius_to_fahrenheit([30])

    def test_invalid_type_none(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            celsius_to_fahrenheit(None)

    def test_below_absolute_zero(self):
        """It should raise AssertionError for temperatures below absolute zero"""
        with self.assertRaises(AssertionError):
            celsius_to_fahrenheit(-274)


if __name__ == "__main__":
    unittest.main()
