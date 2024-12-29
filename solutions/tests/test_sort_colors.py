#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 26 10 2024

@author: Mohamed Elnageeb
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
