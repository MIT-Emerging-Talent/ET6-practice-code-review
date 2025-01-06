#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit test for fahrenheit_to_kelvin function.

Module contents:
    - TestFahrenheitToKelvin: Unit test class for the fahrenheit_to_kelvin function.

Created on 5 1 2025
@author: Ammar Ibrahim
"""

import unittest

from ..fahrenheit_to_kelvin import fahrenheit_to_kelvin


class TestFahrenheitToKelvin(unittest.TestCase):
    """Unit tests for the fahrenheit_to_kelvin function."""

    def test_freezing_point(self):
        """Test for the freezing point of water."""
        actual = fahrenheit_to_kelvin(32)
        expected = 273.15
        self.assertEqual(actual, 273.15, expected)

    def test_boiling_point(self):
        """Test for the boiling point of water."""
        actual = fahrenheit_to_kelvin(212)
        expeted = 373.15
        self.assertEqual(actual, expeted)

    def test_negative_temperature(self):
        """Test for a negative Fahrenheit temperature."""
        actual = fahrenheit_to_kelvin(-40)
        expected = 233.15
        self.assertEqual(actual, expected)

    def test_zero_temperature(self):
        """Test for zero Fahrenheit."""
        actual = fahrenheit_to_kelvin(0)
        expected = 255.37
        self.assertEqual(actual, expected)

    def test_float_input(self):
        """Test for a float tempruture input."""
        actual = fahrenheit_to_kelvin(50.5)
        expected = 283.43
        self.assertEqual(actual, expected)

    def test_invalid_input_string(self):
        """Test for invalid input (string)."""
        with self.assertRaises(AssertionError):
            fahrenheit_to_kelvin("100")
