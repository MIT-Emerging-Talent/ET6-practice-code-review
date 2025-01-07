#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_positive function.

Test categories:
    - Standard cases: positive numbers, negative numbers, zero
    - Edge cases: very large numbers, very small numbers, floating points
    - Defensive tests: wrong input types
"""

import unittest

from ..is_positive import is_positive


class TestIsPositive(unittest.TestCase):
    """Test suite for the is_positive function."""

    # Standard test cases
    def test_positive_integers(self):
        """It should return True for positive integers."""
        self.assertTrue(is_positive(5))
        self.assertTrue(is_positive(1))
        self.assertTrue(is_positive(100))

    def test_negative_integers(self):
        """It should return False for negative integers."""
        self.assertFalse(is_positive(-5))
        self.assertFalse(is_positive(-1))
        self.assertFalse(is_positive(-100))

    def test_zero(self):
        """It should return False for zero."""
        self.assertFalse(is_positive(0))

    # Edge cases
    def test_large_numbers(self):
        """It should handle very large numbers correctly."""
        self.assertTrue(is_positive(1e308))
        self.assertFalse(is_positive(-1e308))

    def test_small_numbers(self):
        """It should handle very small positive and negative numbers correctly."""
        self.assertTrue(is_positive(1e-308))
        self.assertFalse(is_positive(-1e-308))

    def test_floating_points(self):
        """It should handle floating point numbers correctly."""
        self.assertTrue(is_positive(0.1))
        self.assertTrue(is_positive(3.14))
        self.assertFalse(is_positive(-0.1))
        self.assertFalse(is_positive(-3.14))

    # Defensive tests
    def test_invalid_input_type_string(self):
        """It should raise TypeError for string inputs."""
        with self.assertRaises(TypeError):
            is_positive("5")

    def test_invalid_input_type_none(self):
        """It should raise TypeError for None input."""
        with self.assertRaises(TypeError):
            is_positive(None)

    def test_invalid_input_type_bool(self):
        """It should raise TypeError for boolean inputs."""
        with self.assertRaises(TypeError):
            is_positive(True)
        with self.assertRaises(TypeError):
            is_positive(False)

    def test_complex_numbers(self):
        """It should raise TypeError for complex numbers."""
        with self.assertRaises(TypeError):
            is_positive(1 + 2j)


if __name__ == "__main__":
    unittest.main()
