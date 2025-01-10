#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the quadratic_roots function.

Test categories:
    - Standard cases: Verifies normal function behavior
    - Edge cases: Tests boundary values
    - Defensive tests: Handles invalid inputs

Created on 06 Jan 2025
Team Number: 28
Team Name: MIT Alpha
Author: Salih Adam
"""

import unittest

from ..quadratic_roots import quadratic_roots


class TestQuadraticRoots(unittest.TestCase):
    """Test suite for the quadratic_roots function"""

    # Standard test cases

    def test_two_real_roots_int(self):
        """It should return two real roots"""
        actual = quadratic_roots(1, -5, 6)
        expected = "Two real roots: 3.0, 2.0"
        self.assertEqual(actual, expected)

    def test_two_real_roots_float(self):
        """It should return two real roots"""
        actual = quadratic_roots(2.88, -14.09, -31.60)
        expected = "Two real roots: 6.564, -1.672"
        self.assertEqual(actual, expected)

    def test_two_complex_roots_int(self):
        """It should return two complex roots"""
        actual = quadratic_roots(1, -6, 18)
        expected = "Two complex roots: (3+3j), (3-3j)"
        self.assertEqual(actual, expected)

    def test_two_complex_roots_float(self):
        """It should return two complex roots"""
        actual = quadratic_roots(1.68, -5.76, 11.75)
        expected = "Two complex roots: (1.714+2.014j), (1.714-2.014j)"
        self.assertEqual(actual, expected)

    # Edge cases

    def test_one_real_root(self):
        """It should return the one real repeated root"""
        actual = quadratic_roots(1, -10, 25)
        expected = "One real root: 5.0"
        self.assertEqual(actual, expected)

    def test_b_is_zero_a_and_b_different_signs(self):
        """It should return same real roots twice with different signs"""
        actual = quadratic_roots(4, 0, -36)
        expected = "Two real roots: 3.0, -3.0"
        self.assertEqual(actual, expected)

    def test_b_is_zero_a_and_b_same_signs(self):
        """It should return same imaginary roots twice with different signs"""
        actual = quadratic_roots(4, 0, 36)
        expected = "Two imaginary roots: 3j, -3j"
        self.assertEqual(actual, expected)

    def test_c_is_zero(self):
        """It should return 2 real roots one is zero and one is non-zero"""
        actual = quadratic_roots(4, 4, 0)
        expected = "Two real roots: 0.0, -1.0"
        self.assertEqual(actual, expected)

    def test_b_and_c_are_zero(self):
        """It should return 0 as one real root"""
        actual = quadratic_roots(4, 0, 0)
        expected = "One real root: 0.0"
        self.assertEqual(actual, expected)

    # Defensive tests

    def test_invalid_type_for_a(self):
        """It should raise AssertionError if input is not an integer or float"""
        with self.assertRaises(AssertionError):
            quadratic_roots("a", 5, 7)

    def test_a_is_zero(self):
        """It should raise AssertionError if 'a' is zero"""
        with self.assertRaises(AssertionError):
            quadratic_roots(0, -34.4, 12)

    def test_invalid_type_for_b(self):
        """It should raise AssertionError if input is not an integer or float"""
        with self.assertRaises(AssertionError):
            quadratic_roots(19, "b", 13.8)

    def test_invalid_type_for_c(self):
        """It should raise AssertionError if input is not an integer or float"""
        with self.assertRaises(AssertionError):
            quadratic_roots(49, -68, "c")
