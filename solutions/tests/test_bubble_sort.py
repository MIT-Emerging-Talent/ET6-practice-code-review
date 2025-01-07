#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for testing the bubble_sort function.

Test cases include:
    - Valid inputs: sorted and unsorted lists of various sizes.
    - Edge cases: empty, single-element, duplicates, negative numbers, and mixed types.
    - Invalid inputs: non-list inputs and lists containing unsupported types.

Created on 2025-1-4
@author: Tomas Teclehaimanot
"""

import unittest
from ..bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    """Test the bubble_sort function"""

    def test_valid_sorted_list(self):
        """It should handle already sorted lists"""
        arr = [1, 2, 3, 4, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_valid_unsorted_list(self):
        """It should sort unsorted lists"""
        arr = [5, 3, 8, 6, 2, 7]
        bubble_sort(arr)
        self.assertEqual(arr, [2, 3, 5, 6, 7, 8])

    def test_valid_with_duplicates(self):
        """It should correctly handle lists with duplicate values"""
        arr = [4, 2, 5, 2, 4, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 2, 4, 4, 5])

    def test_valid_negative_numbers(self):
        """It should handle lists with negative numbers"""
        arr = [4, -3, 0, -2, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [-3, -2, 0, 1, 4])

    def test_valid_mixed_integers_and_floats(self):
        """It should handle lists with mixed integers and floats"""
        arr = [4.5, 3, 2.7, 1.1, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1.1, 2.7, 3, 4.5, 5])

    def test_edge_case_empty_list(self):
        """It should handle an empty list"""
        arr = []
        bubble_sort(arr)
        self.assertEqual(arr, [])

    def test_edge_case_single_element(self):
        """It should handle a single-element list"""
        arr = [42]
        bubble_sort(arr)
        self.assertEqual(arr, [42])

    def test_invalid_input_not_a_list(self):
        """It should raise an AssertionError for non-list inputs"""
        with self.assertRaises(AssertionError):
            bubble_sort("invalid")

    def test_invalid_input_unsupported_types(self):
        """It should raise an AssertionError for lists with unsupported types"""
        with self.assertRaises(AssertionError):
            bubble_sort([1, 2, "three", 4])

    def test_medium_list(self):
        """It should correctly sort a medium-sized list"""
        arr = [8, 6, 7, 5, 3, 0, 9, 4, 2, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
