#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the calculate_mean function.

Date created: Dec 30, 2024
Author: @Abel Teka
"""

import unittest

from solutions.calculate_mean import calculate_mean


class TestCalculateMean(unittest.TestCase):
    """Unit tests for the calculate_mean function."""

    def test_positive_numbers(self):
        self.assertEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)

    def test_negative_numbers(self):
        self.assertEqual(calculate_mean([-1, -2, -3, -4, -5]), -3.0)

    def test_mixed_numbers(self):
        self.assertEqual(calculate_mean([-10, 0, 10]), 0.0)

    def test_single_number(self):
        self.assertEqual(calculate_mean([42]), 42.0)

    def test_floating_point_numbers(self):
        self.assertAlmostEqual(calculate_mean([1.5, 2.5, 3.5]), 2.5)

    def test_empty_list(self):
        self.assertIsNone(calculate_mean([]))

    def test_invalid_input_not_a_list(self):
        with self.assertRaises(TypeError):
            calculate_mean("not a list")

    def test_invalid_input_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            calculate_mean([1, 2, "three", 4])

    def test_allow_infinity(self):
        """Allow infinity as a valid mean result."""
        self.assertEqual(calculate_mean([float("inf"), 2, 3]), float("inf"))

    def test_allow_negative_infinity(self):
        """Allow negative infinity as a valid mean result."""
        self.assertEqual(calculate_mean([float("-inf"), 2, 3]), float("-inf"))

    def test_large_numbers(self):
        self.assertAlmostEqual(calculate_mean([1e9, 2e9, 3e9]), 2e9)

    def test_small_numbers(self):
        self.assertAlmostEqual(calculate_mean([1e-9, 2e-9, 3e-9]), 2e-9)

    def test_zeros(self):
        self.assertEqual(calculate_mean([0, 0, 0, 0]), 0.0)


if __name__ == "__main__":
    unittest.main()
