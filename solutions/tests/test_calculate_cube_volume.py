#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the calculate_cube_volume function.

Test categories:
    - Standard cases: small positive numbers
    - Edge cases: 0, 1, large positive numbers
    - Defensive tests: assertions, wrong input types

Created on 11-Jan-2025

@author: Mahmoud Alnouri
"""

import unittest
from ..calculate_cube_volume import calculate_cube_volume


class TestCalculateCubeVolume(unittest.TestCase):
    """Test the calculate_cube_volume function."""

    def test_zero_side_length(self):
        """Test the volume of a cube with side length 0 is 0."""
        self.assertAlmostEqual(calculate_cube_volume(0), 0.0)

    def test_one_side_length(self):
        """Test the volume of a cube with side length 1."""
        self.assertAlmostEqual(calculate_cube_volume(1), 1.0)

    def test_small_positive_side_length(self):
        """Test the volume of a cube with a small positive side length."""
        self.assertAlmostEqual(calculate_cube_volume(2.5), 15.625)

    def test_large_positive_side_length(self):
        """Test the volume of a cube with a large positive side length."""
        self.assertAlmostEqual(calculate_cube_volume(1000), 1_000_000.0)

    def test_none_input(self):
        """Test that None input raises AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_cube_volume(None)

    def test_negative_side_length(self):
        """Test that a negative side length raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_cube_volume(-5)

    def test_non_numeric_input(self):
        """Test that a non-numeric input raises AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_cube_volume("side_length")

    def test_list_input(self):
        """Test that a list input raises AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_cube_volume([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
