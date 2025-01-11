#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for calculate_average function.

Test categories:
    - Standard cases: multiple numbers
    - Edge cases: empty list, single element, negative numbers, zeros
    - Defensive tests: wrong input types, assertions
"""

import unittest

from ..calculate_average import calculate_average


class TestCalculateAverage(unittest.TestCase):
    """Test suite for the calculate_average function."""

    # Standard test cases
    def test_integers(self):
        """It should return the average of multiple integers."""
        self.assertEqual(calculate_average([10, 20, 30, 40, 50]), 30.0)

    def test_floats(self):
        """It should return the average of multiple floats."""
        self.assertAlmostEqual(calculate_average([1.1, 2.2, 3.3]), 2.2, places=1)

    # Edge cases
    def test_empty_list(self):
        """It should return None if the list is empty."""
        self.assertIsNone(calculate_average([]))

    def test_single_element(self):
        """It should return the element itself if the list has one value."""
        self.assertEqual(calculate_average([100]), 100.0)

    def test_negative_numbers(self):
        """It should handle negative values correctly."""
        self.assertEqual(calculate_average([-10, -20, -30]), -20.0)

    def test_zeros(self):
        """It should return 0 if all values in the list are zero."""
        self.assertEqual(calculate_average([0, 0, 0, 0]), 0)

    # Defensive tests
    def test_invalid_input_raises_assertion_error(self):
        """It should raise AssertionError for non-float or non-integer inputs."""
        with self.assertRaises(AssertionError):
            calculate_average([10, "twenty", 30])

    def test_mixed_numbers(self):
        """It should correctly average a mixture of positive, negative, and zero values."""
        self.assertEqual(calculate_average([10, -10, 0, 20, -20]), 0)


if __name__ == "__main__":
    unittest.main()
