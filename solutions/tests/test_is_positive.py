#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_positive function.

Module contents:
- TestIsPositive: Unit test for the is_positive function.

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
    def test_basic_positive_integer(self):
        """It should return True for basic positive integer."""
        self.assertTrue(is_positive(5))

    def test_basic_negative_integer(self):
        """It should return False for basic negative integer."""
        self.assertFalse(is_positive(-5))

    def test_positive_large_integer(self):
        """It should return True for large positive integer."""
        self.assertTrue(is_positive(1000000))

    def test_negative_large_integer(self):
        """It should return False for large negative integer."""
        self.assertFalse(is_positive(-1000000))

    def test_zero(self):
        """It should return False for zero."""
        self.assertFalse(is_positive(0))

    # Edge cases
    def test_very_large_positive_number(self):
        """It should handle very large positive numbers correctly."""
        self.assertTrue(is_positive(1e308))

    def test_very_large_negative_number(self):
        """It should handle very large negative numbers correctly."""
        self.assertFalse(is_positive(-1e308))

    def test_very_small_positive_number(self):
        """It should handle very small positive numbers correctly."""
        self.assertTrue(is_positive(1e-308))

    def test_very_small_negative_number(self):
        """It should handle very small negative numbers correctly."""
        self.assertFalse(is_positive(-1e-308))

    # Floating point tests
    def test_positive_float(self):
        """It should return True for positive float."""
        self.assertTrue(is_positive(0.1))
        self.assertTrue(is_positive(3.14))

    def test_negative_float(self):
        """It should return False for negative float."""
        self.assertFalse(is_positive(-0.1))
        self.assertFalse(is_positive(-3.14))

    # Defensive tests
    def test_string_input(self):
        """It should raise TypeError for string input."""
        with self.assertRaises(TypeError):
            is_positive("5")

    def test_none_input(self):
        """It should raise TypeError for None input."""
        with self.assertRaises(TypeError):
            is_positive(None)

    def test_boolean_true_input(self):
        """It should raise TypeError for boolean True input."""
        with self.assertRaises(TypeError):
            is_positive(True)

    def test_boolean_false_input(self):
        """It should raise TypeError for boolean False input."""
        with self.assertRaises(TypeError):
            is_positive(False)

    def test_complex_number_input(self):
        """It should raise TypeError for complex number input."""
        with self.assertRaises(TypeError):
            is_positive(1 + 2j)


if __name__ == "__main__":
    unittest.main()
