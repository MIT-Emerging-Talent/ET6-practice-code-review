#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the calculate_mean function.

Date created: Dec 30, 2024
Author: @Abel Teka

This test suite validates the calculate_mean function's behavior, ensuring it:
- Correctly calculates the mean for positive, negative, and mixed numbers.
- Handles edge cases such as empty lists, single elements, and zeros.
- Raises appropriate errors for invalid inputs, such as non-numeric elements or NaN values.
- Performs reliably with large and small numeric values.

Each test case is designed to ensure a single assertion, with clear documentation for behavior and expectations.
"""

import unittest

from solutions.calculate_mean import calculate_mean


class TestCalculateMean(unittest.TestCase):
    """
    Unit tests for the calculate_mean function, ensuring correctness
    and handling of edge cases and invalid inputs.
    """

    def test_positive_numbers(self):
        """Test mean calculation with a list of positive numbers."""
        self.assertEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)

    def test_negative_numbers(self):
        """Test mean calculation with a list of negative numbers."""
        self.assertEqual(calculate_mean([-1, -2, -3, -4, -5]), -3.0)

    def test_mixed_numbers(self):
        """Test mean calculation with a mix of positive and negative numbers."""
        self.assertEqual(calculate_mean([-10, 0, 10]), 0.0)

    def test_single_number(self):
        """Test mean calculation with a single number."""
        self.assertEqual(calculate_mean([42]), 42.0)

    def test_floating_point_numbers(self):
        """Test mean calculation with a list of floating-point numbers."""
        self.assertAlmostEqual(calculate_mean([1.5, 2.5, 3.5]), 2.5)

    def test_empty_list(self):
        """Test mean calculation with an empty list."""
        self.assertIsNone(calculate_mean([]))

    def test_invalid_input_not_a_list(self):
        """Test for TypeError when the input is not a list."""
        with self.assertRaises(TypeError):
            calculate_mean("not a list")

    def test_invalid_input_non_numeric_elements(self):
        """Test for TypeError when the list contains non-numeric elements."""
        with self.assertRaises(TypeError):
            calculate_mean([1, 2, "three", 4])

    def test_invalid_input_nan(self):
        """Test for Exception when the list contains NaN."""
        with self.assertRaises(Exception):
            calculate_mean([1, 2, float("nan"), 4])

    def test_invalid_input_infinity(self):
        """Test for Exception when the list contains infinity."""
        with self.assertRaises(Exception):
            calculate_mean([1, 2, float("inf"), 4])

    def test_large_numbers(self):
        """Test mean calculation with very large numbers."""
        self.assertAlmostEqual(calculate_mean([1e9, 2e9, 3e9]), 2e9)

    def test_small_numbers(self):
        """Test mean calculation with very small numbers."""
        self.assertAlmostEqual(calculate_mean([1e-9, 2e-9, 3e-9]), 2e-9)

    def test_defensive_assertion_empty_list(self):
        """Test that an empty list returns None."""
        self.assertIsNone(calculate_mean([]))

    def test_boundary_case_zero_values(self):
        """Test mean calculation with a list of zeros."""
        self.assertEqual(calculate_mean([0, 0, 0, 0]), 0.0)


if __name__ == "__main__":
    unittest.main()
