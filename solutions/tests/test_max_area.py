#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the max_area module.

This module contains unit tests for the Solution class's
max_area method. The tests cover various input cases,
including common scenarios, edge cases, and invalid inputs.
"""

import unittest
from solutions.max_area import Solution


class TestMaxArea(unittest.TestCase):
    """
    Unit tests for the Solution class's max_area method.
    The tests verify the functionality of the method with various input lists of heights,
    including common cases, edge cases, and invalid inputs.
    """

    def setUp(self):
        """Set up the Solution instance for testing."""
        self.solution = Solution()

    def test_basic_case(self):
        """
        Test the case with a mix of heights.
        Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]
        Expected result: 49
        """
        result = self.solution.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertEqual(result, 49)

    def test_single_case(self):
        """
        Test the case with the minimum input size.
        Input: [1, 1]
        Expected result: 1
        """
        result = self.solution.max_area([1, 1])
        self.assertEqual(result, 1)

    def test_increasing_heights(self):
        """
        Test the case where the heights are in increasing order.
        Input: [1, 2, 3, 4, 5]
        Expected result: 6
        """
        result = self.solution.max_area([1, 2, 3, 4, 5])
        self.assertEqual(result, 6)

    def test_decreasing_heights(self):
        """
        Test the case where the heights are in decreasing order.
        Input: [5, 4, 3, 2, 1]
        Expected result: 6
        """
        result = self.solution.max_area([5, 4, 3, 2, 1])
        self.assertEqual(result, 6)

    def test_edge_cases(self):
        """
        Test edge cases such as a single height or an empty list.
        """
        result = self.solution.max_area([1])
        self.assertEqual(result, 0)  # Single height

        result = self.solution.max_area([])
        self.assertEqual(result, 0)  # Empty list

    def test_all_zeros(self):
        """
        Test case where all heights are zero.
        Input: [0, 0, 0, 0]
        Expected result: 0
        """
        result = self.solution.max_area([0, 0, 0, 0])
        self.assertEqual(result, 0)

    def test_invalid_input(self):
        """
        Test invalid input types.
        - Input: non-list (like a string or mixed types).
        - Expected: raises ValueError.
        """
        with self.assertRaises(ValueError):
            self.solution.max_area("string")  # Invalid input type

        with self.assertRaises(ValueError):
            self.solution.max_area([1, -1, 2])  # Negative heights

        with self.assertRaises(ValueError):
            self.solution.max_area([1, "a", 2])  # Non-integer in list


if __name__ == "__main__":
    unittest.main()
