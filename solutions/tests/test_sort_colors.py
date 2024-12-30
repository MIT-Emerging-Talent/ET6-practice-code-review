#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains the test cases for the sort_colors function.

The function sort_colors(nums) sorts a given list of integers representing
colors (0 for red, 1 for white, and 2 for blue) in-place without using any
built-in sorting libraries. It ensures the list is sorted in ascending order
while modifying the original list directly.

Test cases:
- Standard test cases:
  - test_empty_list: Handles an empty input list.
  - test_single_element: Handles a list containing a single element.
  - test_all_same_elements: Handles a list where all elements are the same.
  - test_already_sorted: Ensures an already sorted list is not modified.
  - test_unsorted_list: Sorts a typical unsorted list.

- Edge cases:
  - test_large_list: Tests the function with a large input list.
  - test_randomly_generated_list: Tests with a randomly generated list.

- Exception test cases:
  - test_not_a_list: Ensures an AssertionError is raised for non-list inputs.
  - test_invalid_elements: Ensures an AssertionError is raised for invalid
    elements (e.g., elements not in the range [0, 2]).

Created on 26 10 2024

@author: Mohamed-Elnageeb
"""

import random
import unittest

# Import the function to be tested
from ..sort_colors import sort_colors


class TestSortColors(unittest.TestCase):
    """Test the sort_colors function"""

    def test_empty_list(self):
        """It should handle an empty list"""
        nums = []
        sort_colors(nums)
        self.assertEqual(nums, [])

    def test_single_element(self):
        """It should handle a list with one element"""
        nums = [1]
        sort_colors(nums)
        self.assertEqual(nums, [1])

    def test_all_same_elements(self):
        """It should handle a list with all elements being the same"""
        nums = [2, 2, 2]
        sort_colors(nums)
        self.assertEqual(nums, [2, 2, 2])

    def test_already_sorted(self):
        """It should not modify an already sorted list"""
        nums = [0, 0, 1, 1, 2, 2]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])  # Fixed expected output

    def test_unsorted_list(self):
        """It should sort an unsorted list"""
        nums = [2, 0, 2, 1, 1, 0]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_large_list(self):
        """It should handle a large list"""
        nums = [0, 2, 1] * 100000
        sort_colors(nums)
        self.assertEqual(nums, [0] * 100000 + [1] * 100000 + [2] * 100000)

    def test_not_a_list(self):
        """It should raise an assertion error if the input is not a list"""
        with self.assertRaises(AssertionError):
            sort_colors("not a list")

    def test_invalid_elements(self):
        """It should raise an assertion error for invalid elements"""
        nums = [0, 1, 3]  # Invalid element 3
        with self.assertRaises(AssertionError):
            sort_colors(nums)

    def test_randomly_generated_list(self):
        """It should sort an unsorted list"""
        nums = [random.randint(0, 2) for i in range(1000)]
        expected = list(sorted(nums))
        sort_colors(nums)
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()
