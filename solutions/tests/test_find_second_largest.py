#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from ..find_second_largest import find_second_largest  # Import the function to test


class TestFindSecondLargest(unittest.TestCase):
    # Test with a normal list
    def test_normal_case(self):
        self.assertEqual(find_second_largest([2, 3, 6, 6, 5]), 5)

    # Test with a sorted list
    def test_sorted_list(self):
        self.assertEqual(find_second_largest([1, 2, 3, 4, 5]), 4)

    # Test with repeated numbers
    def test_repeated_numbers(self):
        self.assertEqual(find_second_largest([10, 9, 9, 8, 8, 8, 7]), 9)

    # Test with not enough unique numbers
    def test_not_enough_unique_numbers(self):
        with self.assertRaises(ValueError):
            find_second_largest([1, 1, 1, 1])

    # Test with negative numbers
    def test_negative_numbers(self):
        self.assertEqual(find_second_largest([-1, -2, -3, -4, -5]), -2)

    # Test with mixed positive and negative numbers
    def test_mixed_numbers(self):
        self.assertEqual(find_second_largest([-10, 5, 3, 5, -10, 7]), 5)
