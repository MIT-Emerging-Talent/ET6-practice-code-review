#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This a unit test for find_second_largest function"""

import unittest

from ..find_second_largest import find_second_largest  # Import the function to test


class TestFindSecondLargest(unittest.TestCase):
    """Test the find_second_largest function"""

    def test_unsorted_list(self):
        """
        Test with a normal unsorted list
        """
        self.assertEqual(find_second_largest([2, 3, 1, 6, 5]), 5)

    def test_sorted_list(self):
        """
        Test with a sorted list
        """
        self.assertEqual(find_second_largest([1, 2, 3, 4, 5]), 4)

    def test_duplicate_numbers(self):
        """
        Test with duplicate numbers
        """
        self.assertEqual(find_second_largest([10, 9, 9, 8, 8, 8, 7]), 9)

    def test_not_enough_unique_numbers(self):
        """
        Test with not enough unique numbers
        """
        with self.assertRaises(ValueError):
            find_second_largest([1, 1, 1, 1])

    def test_negative_numbers(self):
        """
        Test with negative numbers
        """
        self.assertEqual(find_second_largest([-1, -2, -3, -4, -5]), -2)

    def test_positive_and_negative_numbers(self):
        """
        Test with mixed positive and negative numbers
        """
        self.assertEqual(find_second_largest([-10, 5, 3, 5, -10, 7]), 5)

    def test_empty_list(self):
        """
        Test with an empty list
        """
        with self.assertRaises(ValueError):
            find_second_largest([])

    def test_single_element_list(self):
        """
        Test with a single element list
        """
        with self.assertRaises(ValueError):
            find_second_largest([1])
