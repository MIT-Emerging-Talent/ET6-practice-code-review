#!/usr/bin/env python3
"""
Tests for the calculate_bmi function.

Created on 2025-01-04
Author: Cynthia Wairimu
"""

import unittest
from ..calculate_bmi import calculate_bmi


class TestCalculateBMI(unittest.TestCase):
    """Tests for the calculate_bmi function."""

    def test_metric_normal_weight(self):
        """It should return 'Normal weight' for a BMI between 18.5 and 24.9 using metric."""
        result = calculate_bmi(weight=70, height=1.75, system="metric")
        self.assertEqual(result, "Normal weight")

    def test_metric_underweight(self):
        """It should return 'Underweight' for a BMI below 18.5 using metric."""
        result = calculate_bmi(weight=45, height=1.75, system="metric")
        self.assertEqual(result, "Underweight")

    def test_metric_obese(self):
        """It should return 'Obese' for a BMI of 30 or above using metric."""
        result = calculate_bmi(weight=100, height=1.75, system="metric")
        self.assertEqual(result, "Obese")

    def test_imperial_overweight(self):
        """It should return 'Overweight' for a BMI between 25 and 29.9 using imperial."""
        result = calculate_bmi(weight=160, height=65, system="imperial")
        self.assertEqual(result, "Overweight")

    def test_invalid_system(self):
        """It should raise a ValueError for an invalid system."""
        with self.assertRaises(ValueError):
            calculate_bmi(weight=70, height=1.75, system="unknown")

    def test_invalid_inputs(self):
        """It should raise a ValueError for invalid inputs."""
        with self.assertRaises(ValueError):
            calculate_bmi(weight=-70, height=1.75, system="metric")
        with self.assertRaises(ValueError):
            calculate_bmi(weight=70, height=0, system="metric")
        with self.assertRaises(ValueError):
            calculate_bmi(weight="seventy", height=1.75, system="metric")


if __name__ == "__main__":
    unittest.main()
