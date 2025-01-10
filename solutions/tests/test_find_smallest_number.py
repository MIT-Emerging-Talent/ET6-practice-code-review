#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the function that finds the smallest number in a list of integers.

Module contents:
    - TestFindSmallestNumber: unit tests for the `find_smallest_number` function.

Created on 01-04-2025
@author: Saliha Kalender
"""

import unittest
from ..find_smallest_number import find_smallest_number


class TestFindSmallestNumber(unittest.TestCase):
    """
    Unit tests for the `find_smallest_number` function.
    """

    def test_positive_numbers(self):
        # Test with a list of positive integers.
        self.assertEqual(find_smallest_number([3, 1, 4, 1, 5, 9]), 1)

    def test_negative_numbers(self):
        # Test with a list of negative integers.
        self.assertEqual(find_smallest_number([-25, -15, -1, -5, -10]), -25)

    def test_single_element(self):
        # Test with a list containing a single integer.
        self.assertEqual(find_smallest_number([42]), 42)

    def test_empty_list(self):
        # Test with an empty list to ensure ValueError is raised.
        with self.assertRaises(ValueError):
            find_smallest_number([])

    def test_non_integer_elements(self):
        # Test with a list containing non-integer elements to ensure TypeError is raised.
        with self.assertRaises(TypeError):
            find_smallest_number([3, "a", 5])

    def test_non_list_input(self):
        # Test with a non-list input to ensure TypeError is raised.
        with self.assertRaises(TypeError):
            find_smallest_number("not a list")

    def test_boundary_values(self):
        # Test with boundary values, including very large and very small integers.
        self.assertEqual(find_smallest_number([10**6, -(10**6), 0]), -(10**6))


if __name__ == "__main__":
    # This ensures that the unittest framework runs the test cases in this file
    unittest.main()
