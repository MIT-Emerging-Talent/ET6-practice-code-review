#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test cases for the `trap` function, which calculates the amount of rainwater
that can be trapped given an elevation map.

The `trap` function is tested with various scenarios, including edge cases,
to ensure accuracy and robustness.

Created on 12.01.2025
@author: Mushtary Alam
"""

import unittest
from ..trapping_rain_water import trap  # Ensure the correct import path here


class TestTrappingRainWater(unittest.TestCase):
    """
    Test the trapping_rain_water function
    """

    def test_trap(self):
        """
        Tests the `trap` function with various input cases.
        Validates the correctness of the implementation for:
            - Empty elevation map
            - Single bar or two bars (no trapping possible)
            - Basic cases with small maps
            - Complex cases with valleys and multiple trapping regions
        """
        # Test case 1: Empty list
        self.assertEqual(trap([]), 0, "Failed on empty list")

        # Test case 2: Single bar
        self.assertEqual(trap([1]), 0, "Failed on single element")

        # Test case 3: Two bars
        self.assertEqual(trap([1, 2]), 0, "Failed on two bars")

        # Test case 4: Small trapping
        self.assertEqual(trap([0, 1, 0, 2]), 1, "Failed on basic trapping case")

        # Test case 5: Complex trapping
        self.assertEqual(trap([4, 2, 0, 3, 2, 5]), 9, "Failed on complex trapping case")

        # Test case 6: Flat elevation
        self.assertEqual(trap([3, 3, 3]), 0, "Failed on flat elevation")

        # Test case 7: Increasing elevation
        self.assertEqual(trap([1, 2, 3, 4]), 0, "Failed on increasing elevation")

        # Test case 8: Decreasing elevation
        self.assertEqual(trap([4, 3, 2, 1]), 0, "Failed on decreasing elevation")

        # Test case 9: Mixed elevation
        self.assertEqual(trap([0, 3, 0, 2, 0, 4]), 7, "Failed on mixed elevation")

        # Test case 10: Single valley
        self.assertEqual(trap([3, 0, 3]), 3, "Failed on single valley case")

        # Defensive assertion tests:
        # Test case 11: Invalid input type (not a list)
        with self.assertRaises(AssertionError):
            trap("invalid input")

        # Test case 12: List with negative integers
        with self.assertRaises(AssertionError):
            trap([1, 2, -1, 3])

        # Test case 13: List with non-integer values
        with self.assertRaises(AssertionError):
            trap([1, 2, "3", 4])

        # Test case 14: List with mixed valid and invalid values
        with self.assertRaises(AssertionError):
            trap([1, 2, 3, "invalid"])


if __name__ == "__main__":
    # Run all tests
    unittest.main()
