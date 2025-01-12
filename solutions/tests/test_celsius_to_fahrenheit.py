#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for conversion from celsius to fahrenheit.

This module contains unittest test cases for the celsius_to_fahrenheit

Created on 30 12 2024
@author: Terry Aziaba
"""

import unittest

from ..celsius_to_fahrenheit import celsius_to_fahrenheit


class TestCelsiusToFahrenheit(unittest.TestCase):
    """Unit tests for the celsius_to_fahrenheit function."""

    def test_freezing_point(self):
        """Test the freezing point of water."""
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)

    def test_boiling_point(self):
        """Test the boiling point of water."""
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0)

    def test_negative_temperature(self):
        """Test a negative temperature."""
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_fractional_input(self):
        """Test a fractional Celsius value."""
        self.assertAlmostEqual(celsius_to_fahrenheit(37.5), 99.5)

    def test_large_positive_value(self):
        """Test a very large positive Celsius value."""
        self.assertAlmostEqual(celsius_to_fahrenheit(1000), 1832.0)

    def test_large_negative_value(self):
        """Test a very large negative Celsius value"""
        self.assertAlmostEqual(celsius_to_fahrenheit(-273.15), -459.67)

    def test_infinity_positive(self):
        """Test positive infinity."""
        result = celsius_to_fahrenheit(float("inf"))
        self.assertEqual(result, float("inf"))

    def test_infinity_negative(self):
        """Test negative infinity."""
        result = celsius_to_fahrenheit(float("-inf"))
        self.assertEqual(result, float("-inf"))

    def test_nan_value(self):
        """Test if NaN is handled correctly."""
        with self.assertRaises(AssertionError):
            celsius_to_fahrenheit(float("nan"))

    def test_zero_input(self):
        """Test zero as input."""
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)

    def test_small_fractional_input(self):
        """Test a small fractional input."""
        self.assertAlmostEqual(celsius_to_fahrenheit(0.5), 32.9)

    def test_assertion_error_non_numeric(self):
        """Test if an assertion error is raised for non-numeric input."""
        with self.assertRaises(AssertionError):
            celsius_to_fahrenheit("not a number")

    def test_assertion_error_none(self):
        """Test if an assertion error is raised for None input."""
        with self.assertRaises(AssertionError):
            celsius_to_fahrenheit(None)
