#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4 1 2025

@author: Ammar Ibrahim
"""

import unittest

from ..factorial_calc import factorial_calc


class TestFactorialCalc(unittest.TestCase):
    """Test the factorial_calc function"""

    def test_0(self):
        """it should returne 1 (the factorial   of 0 = 1)"""
        actual = factorial_calc(0)
        expected = 1
        self.assertEqual(actual, expected)

    def test_5(self):
        """it should returne 120 (the factorial   of 5 = 120)"""
        actual = factorial_calc(5)
        expected = 5 * 4 * 3 * 2 * 1
        self.assertEqual(actual, expected)

    def test_negative(self):
        """It should raise AssertionError for negative numbers"""
        with self.assertRaises(AssertionError):
            factorial_calc(-5)

    def test_float(self):
        """It should raise AssertionError for non integer inputs"""
        with self.assertRaises(AssertionError):
            factorial_calc(5.5)
