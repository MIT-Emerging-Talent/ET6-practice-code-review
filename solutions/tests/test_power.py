#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for power function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
- Standard cases: Different valid inputs.
- Edge cases: Boundary & Extreme conditions
- Defensive cases: Invalid inputs (types, values)

Created on 2025-01-04
Author: Nay Win Hlaing
"""

import unittest
from ..power import power


class TestPower(unittest.TestCase):
    """Test the power function."""

    # Standard Cases
    def test_exponent_zero(self):
        """Exponent 0 of any base value; results in 1."""
        actual = power(1000, 0)
        expected = 1
        self.assertEqual(actual, expected)

    def test_exponent_one(self):
        """Exponent 1 of any base should result in the base itself."""
        actual = power(2003, 1)
        expected = 2003
        self.assertEqual(actual, expected)

    def test_odd_exponent(self):
        """The function should work correctly with an odd exponent."""
        actual = power(10, 3)
        expected = 1000
        self.assertEqual(actual, expected)

    def test_even_exponent(self):
        """The function should work correctly with an even exponent."""
        actual = power(10, 8)
        expected = 100000000
        self.assertEqual(actual, expected)

    def test_negative_base_even_exponent(self):
        """The function should work correctly with a negative base and an even exponent."""
        actual = power(-3, 4)
        expected = 81
        self.assertEqual(actual, expected)

    def test_negative_base_odd_exponent(self):
        """The function should work correctly with a negative base and an odd exponent."""
        actual = power(-3, 3)
        expected = -27
        self.assertEqual(actual, expected)

    def test_negative_even_exponent(self):
        """The function should correctly with a negative even exponent."""
        actual = power(3, -4)
        expected = 1 / 81
        self.assertAlmostEqual(actual, expected)

    def test_negative_odd_exponent(self):
        """The function should correctly with a negative odd exponent."""
        actual = power(2, -3)
        expected = 1 / 8
        self.assertAlmostEqual(actual, expected)

    # Edge cases
    def test_negative_base_exponent_zero(self):
        """Exponent of 0 should always evaluate to 1."""
        actual = power(-5000, 0)
        expected = 1
        self.assertEqual(actual, expected)

    def test_base_one_any_exponent(self):
        """Raising base 1 to any exponent should evaluate to 1."""
        actual = power(1, 1000)
        expected = 1
        self.assertEqual(actual, expected)

    def test_base_negative_one_even_exponent(self):
        """Raising base -1 to an even exponent should evaluate to 1."""
        actual = power(-1, 1000)
        expected = 1
        self.assertEqual(actual, expected)

    def test_base_negative_one_odd_exponent(self):
        """Raising base -1 to an odd exponent should evaluate to 1."""
        actual = power(-1, 1111)
        expected = -1
        self.assertEqual(actual, expected)

    # Defensive cases
    def test_string_base(self):
        """A string base input should raise a type error."""
        with self.assertRaises(TypeError):
            power("5", 2)

    def test_string_exponent(self):
        """A string exponent input should raise a type error."""
        with self.assertRaises(TypeError):
            power(3, "3")

    def test_decimal_input(self):
        """A decimal input should raise a type error."""
        with self.assertRaises(TypeError):
            power(2.2, 2.2)

    def test_fractional_input(self):
        """A fractional input should raise a type error."""
        with self.assertRaises(TypeError):
            power(8 / 2, 1 / 2)

    def test_base_0_exponent_0(self):
        """0 raised to the power of 0 is mathematically ambiguous."""
        with self.assertRaises(ValueError):
            power(0, 0)

    def test_base_0_exponent_negative(self):
        """0 raised to a negative exponent is undefined."""
        with self.assertRaises(ValueError):
            power(0, -5)
