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

import unittest
from math import pi
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solutions.volume_of_the_sphere import volume_of_the_sphere


class TestVolumeOfTheSphere(unittest.TestCase):
    """Test cases for volume_of_the_sphere function."""

    def test_volume_with_radius_five(self):
        """Test volume calculation with radius 5.0."""
        self.assertAlmostEqual(volume_of_the_sphere(5.0), 523.5987755982989)

    def test_volume_with_radius_two_point_five(self):
        """Test volume calculation with radius 2.5."""
        self.assertAlmostEqual(volume_of_the_sphere(2.5), 65.44984694978736)

    def test_volume_with_radius_one(self):
        """Test volume calculation with radius 1.0."""
        self.assertAlmostEqual(volume_of_the_sphere(1.0), 4.1887902047863905)

    def test_volume_with_integer_radius(self):
        """Test volume calculation with integer input."""
        self.assertAlmostEqual(volume_of_the_sphere(3), (4 / 3) * pi * 27)

    def test_raises_type_error_with_string_input(self):
        """Test TypeError raised when input is a string."""
        with self.assertRaises(AssertionError):
            volume_of_the_sphere("5")

    def test_raises_type_error_with_list_input(self):
        """Test TypeError raised when input is a list."""
        with self.assertRaises(AssertionError):
            volume_of_the_sphere([5])

    def test_raises_value_error_with_zero_radius(self):
        """Test ValueError raised when radius is zero."""
        with self.assertRaises(AssertionError):
            volume_of_the_sphere(0)

    def test_raises_value_error_with_negative_radius(self):
        """Test ValueError raised when radius is negative."""
        with self.assertRaises(AssertionError):
            volume_of_the_sphere(-1)

    def test_volume_with_small_radius(self):
        """Test volume calculation with very small radius."""
        self.assertAlmostEqual(volume_of_the_sphere(0.1), (4 / 3) * pi * 0.001)

    def test_volume_with_large_radius(self):
        """Test volume calculation with large radius."""
        self.assertAlmostEqual(volume_of_the_sphere(1000), (4 / 3) * pi * 1000**3)


if __name__ == "__main__":
    unittest.main()
