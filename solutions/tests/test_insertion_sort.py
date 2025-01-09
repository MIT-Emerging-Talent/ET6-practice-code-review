#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for testing the insertion_sort function.

Test cases include:
    - Valid inputs: lists of integers, floats, and mixed comparable types.
    - Edge cases: empty, single-element, sorted and reverse-sorted, and lists with duplicates.
    - Invalid inputs: non-list values (e.g., integers, strings, None).

Created on 2025-1-05
@author: Tomas Teclehaimanot
"""

import unittest

from ..insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    """Test the insertion_sort function"""

    def test_sorted_list(self):
        """It should handle already sorted lists"""
        arr = [1, 2, 3, 4, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """It should sort reverse-ordered lists"""
        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        """It should sort an unsorted list"""
        arr = [4, 2, 5, 1, 3]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_empty_list(self):
        """It should handle empty lists"""
        arr = []
        insertion_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element_list(self):
        """It should handle single-element lists"""
        arr = [42]
        insertion_sort(arr)
        self.assertEqual(arr, [42])

    def test_list_with_duplicates(self):
        """It should handle lists with duplicate elements"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_list_with_floats(self):
        """It should handle lists with float elements"""
        arr = [3.1, 2.4, 5.6, 1.0]
        insertion_sort(arr)
        self.assertEqual(arr, [1.0, 2.4, 3.1, 5.6])

    def test_mixed_comparable_types(self):
        """It should handle lists with mixed comparable types"""
        arr = [3, 2.4, 5, 1.0]
        insertion_sort(arr)
        self.assertEqual(arr, [1.0, 2.4, 3, 5])

    def test_invalid_input_none(self):
        """It should raise a AssertionError for None"""
        with self.assertRaises(AssertionError):
            insertion_sort(None)

    def test_invalid_input_string(self):
        """It should raise a AssertionError for string inputs"""
        with self.assertRaises(AssertionError):
            insertion_sort("not a list")

    def test_invalid_input_integer(self):
        """It should raise a AssertionError for integer inputs"""
        with self.assertRaises(AssertionError):
            insertion_sort(12345)


if __name__ == "__main__":
    unittest.main()
