#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/01/2025
@author: Dorcas Wanja Njeri
"""

import unittest

from solution.remove_Duplicates_from_sorted_Array import remove_Duplicates_from_sorted_Array


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    """Test the remove_duplicates_from_sorted_array function"""

    def test_basic_example(self):
        """Should remove duplicates in a basic sorted array"""
        nums = [1, 1, 2]
        length = remove_Duplicates_from_sorted_Array(nums)
        self.assertEqual(length, 2)

    def remove_suplicates_from_sorted_array(self):
        """Should remove duplicates from a longer sorted array"""
        nums = [0, 0, 1, 1, 2, 2, 3, 3, 4]
        length = remove_Duplicates_from_sorted_Array(nums)
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(nums[:length], expected)

    def test_no_duplicates(self):
        """Should return the same list if there are no duplicates"""
        nums = [1, 2, 3, 4, 5]
        length = remove_Duplicates_from_sorted_Array(nums)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(nums[:length], expected)

    def test_all_duplicates(self):
        """Should return a list with a single element if all elements are duplicates"""
        nums = [2, 2, 2, 2, 2]
        length = remove_Duplicates_from_sorted_Array(nums)
        expected = [2]
        self.assertEqual(nums[:length], expected)

    def test_empty_array(self):
        """Should return 0 for an empty array"""
        nums = []
        length = remove_Duplicates_from_sorted_Array(nums)
        self.assertEqual(length, 0)

    def test_single_element(self):
        """Should return the same list if there is only one element"""
        nums = [5]
        length = remove_Duplicates_from_sorted_Array(nums)
        expected = [5]
        self.assertEqual(nums[:length], expected)


if __name__ == "__main__":
    unittest.main()
