#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit test for calculate_bmi function.

Module contents:
    - TestCalculateBMI: Unit test class for the calculate_bmi function.

Test categories:
    - Standards cases: double weights, double heights
    - Edge cases: negative numbers, 0
    - Defensive tests: wrong input types, assertions

Created on 7 1 2025
@author: Collins Ochieng
"""

import unittest

from ..calculate_bmi import calculate_bmi


class TestCalculateBMI(unittest.TestCase):
    """Unit test class for the calculate_bmi function."""

    def test_underweight(self):
        """Test underweight case with a BMI of 16.82."""
        self.assertEqual(calculate_bmi(52.1, 1.76), 16.82)

    def test_healthy(self):
        """Test healthy case with a BMI of 21.72."""
        self.assertEqual(calculate_bmi(65.0, 1.73), 21.72)

    def test_overweight(self):
        """Test overweight case with a BMI of 26.12."""
        self.assertEqual(calculate_bmi(80.0, 1.75), 26.12)

    def test_zero_values(self):
        """Test zero values which raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.48)

    def test_negative_values(self):
        """Test negative values which raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_bmi(-65.11, 1.48)

    def test_string_input(self):
        """Test string input which raises AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_bmi("65.11", 1.48)


if __name__ == "__main__":
    unittest.main()
