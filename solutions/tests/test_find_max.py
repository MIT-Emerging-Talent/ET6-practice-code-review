#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the find_max function.
Contains comprehensive tests to verify the functionality of finding the maximum value.

Test categories:
    - Standard cases: typical numerical comparisons
    - Edge cases: identical values, floating-point precision, large values
    - Defensive tests: invalid inputs (non-numeric types)

Created: 04/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Shaima Mohamed
"""

import unittest
from ..find_max import find_max


class TestFindMax(unittest.TestCase):
    """Test the find_max function"""

    # Test Standard Cases
    def test_positive_numbers(self):
        """It should return the largest of three positive numbers"""
        self.assertEqual(find_max(3, 5, 2), 5)

    def test_negative_numbers(self):
        """It should return the largest of three negative numbers"""
        self.assertEqual(find_max(-1, -3, -2), -1)

    def test_mixed_numbers(self):
        """It should return the largest of mixed positive and negative numbers"""
        self.assertEqual(find_max(-1, 3, 2), 3)

    # Test Edge Cases
    def test_identical_values(self):
        """It should return the same value if all inputs are identical"""
        self.assertEqual(find_max(4, 4, 4), 4)

    def test_floating_point_precision(self):
        """It should correctly handle floating-point precision"""
        self.assertAlmostEqual(find_max(2.5, 2.51, 2.49), 2.51)

    def test_large_numbers(self):
        """It should handle very large numbers correctly"""
        self.assertEqual(find_max(1e10, 1e12, 1e11), 1e12)

    # Test Defensive Assertions
    def test_non_numeric_num1(self):
        """It should raise an assertion error if num1 is a string"""
        with self.assertRaises(AssertionError):
            find_max("1", 2, 3)

    def test_non_numeric_num2(self):
        """It should raise an assertion error if num2 is a string"""
        with self.assertRaises(AssertionError):
            find_max(1, "2", 3)

    def test_non_numeric_num3(self):
        """It should raise an assertion error if num3 is a string"""
        with self.assertRaises(AssertionError):
            find_max(1, 2, "3")


if __name__ == "__main__":
    unittest.main()
