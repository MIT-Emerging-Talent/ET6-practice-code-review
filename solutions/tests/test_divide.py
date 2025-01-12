#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 05.01.2025

@author: Zephaniah Okoye
"""

import unittest
import math

from ..divide import divide


class TestDivide(unittest.TestCase):
    """Test for testing our divide function"""

    def test_divide_integers(self):
        """It should produce the accurate results of a division operation for two integer inputs"""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(9, 3), 3.0)
        self.assertEqual(divide(0, 1), 0.0)

    def test_divide_floats(self):
        """It should produce the accurate results of a division operation for two float inputs"""
        self.assertAlmostEqual(divide(10.5, 2.5), 4.2)
        self.assertAlmostEqual(divide(-7.0, 2.0), -3.5)

    def test_divide_zero(self):
        """It should show a ZeroDivisionError whenever the denominator input is zero"""
        with self.assertRaises(ZeroDivisionError) as context:
            divide(7, 0)
        self.assertTrue("Cannot divide by zero" in str(context.exception))

    def test_divide_type_error(self):
        """It should show a TypeError when either argument is not a number"""
        with self.assertRaises(TypeError) as context:
            divide("10", 2)
        self.assertTrue("Both arguments must be numbers" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            divide(10, "2")
        self.assertTrue(
            "unsupported operand type(s) for /: 'int' and 'str'"
            in str(context.exception)
        )

        with self.assertRaises(TypeError) as context:
            divide("10", "2")
        self.assertTrue("Both arguments must be numbers" in str(context.exception))

    def test_divide_large_number(self):
        """It should correctly handle very large numbers"""
        self.assertAlmostEqual(divide(1e308, 1e308), 1.0)

    def test_divide_small_number(self):
        """It should correctly handle very small numbers"""
        self.assertAlmostEqual(divide(1e-308, 1e-308), 1.0)

    def test_divide_negative_numbers(self):
        """It should correctly handle negative numbers"""
        self.assertAlmostEqual(divide(-10, -2), 5.0)
        self.assertAlmostEqual(divide(-10, 2), -5.0)
        self.assertAlmostEqual(divide(10, -2), -5.0)

    def test_divide_infinity(self):
        """It should correctly handle division with infinity"""
        self.assertEqual(divide(float("inf"), 1), float("inf"))

    def test_divide_nan(self):
        """It should correctly handle division with NaN values"""
        self.assertTrue(math.isnan(divide(float("nan"), 1)))
