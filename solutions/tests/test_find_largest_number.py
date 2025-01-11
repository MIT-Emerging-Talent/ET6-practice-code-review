#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the find_largest_number function.

Created on 2025-01-07
@author: Saliha Kalender
"""

import unittest
from ..find_largest_number import find_largest_number


class TestFindLargestNumber(unittest.TestCase):
    """
    Test cases for the `find_largest_number` function.
    Ensures correctness and covers edge cases.
    """

    def test_positive_numbers(self):
        """Test with a list of positive numbers."""
        self.assertEqual(find_largest_number([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        self.assertEqual(find_largest_number([-10, -20, -30, -5]), -5)

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(find_largest_number([42]), 42)

    def test_empty_list(self):
        """Test that ValueError is raised for an empty list."""
        with self.assertRaises(ValueError):
            find_largest_number([])

    def test_non_integer_list(self):
        """Test that ValueError is raised for a list with non-integer elements."""
        with self.assertRaises(ValueError):
            find_largest_number([1, 2, "a"])

    def test_non_list_input(self):
        """Test that TypeError is raised when the input is not a list."""
        with self.assertRaises(TypeError):
            find_largest_number(123)

    def test_boundary_large_numbers(self):
        """Test with a list containing very large numbers."""
        self.assertEqual(find_largest_number([2**31 - 1, -(2**31)]), 2**31 - 1)

    def test_boundary_small_list(self):
        """Test with a list containing the smallest two integers."""
        self.assertEqual(find_largest_number([-1, -2]), -1)


# Run the tests when this script is executed
if __name__ == "__main__":
    unittest.main()
