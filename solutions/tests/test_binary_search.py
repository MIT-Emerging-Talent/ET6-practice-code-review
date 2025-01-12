#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the binary_search function..

Test cases include:
    - Valid inputs: Searching for elements within a sorted list.
    - Edge cases: Searching for elements at the start, middle, or end of the list.
    - Non-existent elements: Searching for elements not in the list.
    - Invalid inputs: Providing invalid ranges or unsorted input.

Created on 2025-01-02
@author: Alexander Andom
"""

import unittest

from ..binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    """Test the binary_search function"""

    def test_search_existing_middle(self):
        """It should return the index of the item in the middle"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 3, 0, len(arr) - 1), 2)

    def test_search_existing_start(self):
        """It should return the index of the item at the start"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 1, 0, len(arr) - 1), 0)

    def test_search_existing_end(self):
        """It should return the index of the item at the end"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 5, 0, len(arr) - 1), 4)

    def test_search_nonexistent(self):
        """It should return -1 for an item not in the list"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 6, 0, len(arr) - 1), -1)

    def test_search_invalid_range(self):
        """It should return -1 for an invalid range"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 3, 3, 2), -1)

    def test_search_empty_list(self):
        """It should return -1 for an empty list"""
        arr = []
        self.assertEqual(binary_search(arr, 1, 0, 0), -1)

    def test_search_single_element_found(self):
        """It should return the index for a single-element list"""
        arr = [3]
        self.assertEqual(binary_search(arr, 3, 0, 0), 0)

    def test_search_single_element_not_found(self):
        """It should return -1 for a single-element list when the item is not found"""
        arr = [3]
        self.assertEqual(binary_search(arr, 4, 0, 0), -1)

    def test_invalid_arr(self):
        """It should raise an assertion error if arr is not a list."""
        with self.assertRaises(AssertionError):
            binary_search("not_a_list", 3, 0, 5)

    def test_invalid_item(self):
        """It should raise an assertion error if item is not an integer."""
        with self.assertRaises(AssertionError):
            binary_search([1, 2, 3], "3", 0, 2)

    def test_invalid_start_type(self):
        """It should raise an assertion error if start is not an integer."""
        with self.assertRaises(AssertionError):
            binary_search([1, 2, 3], 2, "start", 2)

    def test_invalid_start_value(self):
        """It should raise an assertion error if start is negative."""
        with self.assertRaises(AssertionError):
            binary_search([1, 2, 3], 2, -1, 2)

    def test_invalid_end_type(self):
        """It should raise an assertion error if end is not an integer."""
        with self.assertRaises(AssertionError):
            binary_search([1, 2, 3], 2, 0, "end")

    def test_invalid_end_value(self):
        """It should raise an assertion error if end is negative."""
        with self.assertRaises(AssertionError):
            binary_search([1, 2, 3], 2, 0, -2)

    def test_unsorted_list(self):
        """It should raise an assertion error if the list is unsorted."""
        with self.assertRaises(AssertionError):
            binary_search([3, 1, 2], 2, 0, 2)


if __name__ == "__main__":
    unittest.main()
