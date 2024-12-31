#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the search_insert_position function
Created on 2024-12-31
Author: Omnia
"""

import unittest
from ..search_insert_position import search_insert_position


class TestIsIn(unittest.TestCase):
    """Test Suite for the search_insert_position function"""

    def test_minimal_input(self):
        """Test when numbers is an empty list"""
        self.assertEqual(search_insert_position([], 0), 0)

    def test_target_found(self):
        """Test when target is found in the numbers list"""
        self.assertEqual(search_insert_position([1, 3, 5, 6], 1), 0)

    def test_target_not_found(self):
        """Test when target is not found in the numbers list"""
        self.assertEqual(search_insert_position([1, 3, 5, 6], 7), 4)

    def test_one_element(self):
        """Test when the numbers list contain one element"""
        self.assertEqual(search_insert_position([-1], 1), 1)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(search_insert_position([-10, -5, 0, 5], -6), 1)

    def test_large_list(self):
        """Test with a large list"""
        self.assertEqual(search_insert_position(list(range(1, 10001)), 10001), 10000)

    # defensive tests
    def test_invalid_numbers_input(self):
        """should raise assertion error because first parameter is not a list of only integers"""
        with self.assertRaises(AssertionError):
            search_insert_position(["3", 4, 6], 5)

    def test_invalid_target_input(self):
        """should raise assertion error because second parameter is not an integer"""
        with self.assertRaises(AssertionError):
            search_insert_position([1, 2, 3], "x")

    def test_unsorted_list(self):
        """Test defensive assertion for an unsorted list."""
        with self.assertRaises(AssertionError):
            search_insert_position([3, 1, 4, 2], 2)


if __name__ == "__main__":
    unittest.main()
