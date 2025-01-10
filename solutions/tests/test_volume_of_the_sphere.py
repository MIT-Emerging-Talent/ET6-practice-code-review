#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for volume_of_the_sphere function.
Contains tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: Valid positive float and integer radii.
    - Edge cases: Very small and very large positive radii.
    - Defensive cases: Invalid input types (string, list), and invalid values (zero, negative).

Created on 2025-01-07
Author: Cyne Jarvis J. Zarceno
"""

import os
import sys
import unittest
from math import pi

# Add parent directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from solutions.volume_of_the_sphere import volume_of_the_sphere


class TestVolumeOfTheSphere(unittest.TestCase):
    """Test cases for volume_of_the_sphere function."""

    def test_volume_with_radius_five(self):
        """Test volume calculation with radius 5.0."""
        self.assertAlmostEqual(volume_of_the_sphere(5.0), 523.60, places=2)

    def test_volume_with_radius_two_point_five(self):
        """Test volume calculation with radius 2.5."""
        self.assertAlmostEqual(volume_of_the_sphere(2.5), 65.45, places=2)

    def test_volume_with_radius_one(self):
        """Test volume calculation with radius 1.0."""
        self.assertAlmostEqual(volume_of_the_sphere(1.0), 4.19, places=2)

    def test_volume_with_integer_radius(self):
        """Test volume calculation with integer input."""
        expected = round((4 / 3) * pi * 27, 2)
        self.assertAlmostEqual(volume_of_the_sphere(3), expected, places=2)

    def test_raises_type_error_with_string_input(self):
        """Test TypeError raised when input is a string."""
        with self.assertRaises(TypeError):
            volume_of_the_sphere("5")

    def test_raises_type_error_with_list_input(self):
        """Test TypeError raised when input is a list."""
        with self.assertRaises(TypeError):
            volume_of_the_sphere([5])

    def test_raises_value_error_with_zero_radius(self):
        """Test ValueError raised when radius is zero."""
        with self.assertRaises(ValueError):
            volume_of_the_sphere(0)

    def test_raises_value_error_with_negative_radius(self):
        """Test ValueError raised when radius is negative."""
        with self.assertRaises(ValueError):
            volume_of_the_sphere(-1)

    def test_volume_with_small_radius(self):
        """Test volume calculation with very small radius."""
        expected = round((4 / 3) * pi * 0.001, 2)
        self.assertAlmostEqual(volume_of_the_sphere(0.1), expected, places=2)

    def test_volume_with_large_radius(self):
        """Test volume calculation with large radius."""
        expected = round((4 / 3) * pi * 1000**3, 2)
        self.assertAlmostEqual(volume_of_the_sphere(1000), expected, places=2)


if __name__ == "__main__":
    unittest.main()
