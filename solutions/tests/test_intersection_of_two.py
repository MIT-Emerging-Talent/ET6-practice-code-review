#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for intersection_of_two function.
Contains comprehensive tests to ensure the correctness
of the intersection_of_two function.
It is designed to work with lists containing any data type allowed in a list.
lists can not be empty

Test categories:
    - Standard cases: Lists with common items, lists with mixed data types,
    lists with special characters, repeated items list
    - Edge cases: lists with no intersection, single-element lists, duplicated items,
      Different Types but Equal Values, sublist intersection, different case items
    - Defensive tests: Non-list inputs, one empty list, both empty list

Created on 30-12-2024
Author: Linah Khayri
"""

import unittest

from ..intersection_of_two import intersection_of_two


class TestIntersectionOfTwo(unittest.TestCase):
    """Test suite for the intersection_of_two function that handle different cases"""

    # Standard cases

    def test_numbers_intersection(self):
        "Two lists containing numbers"
        list1 = [1, 2, 3.6]
        list2 = [2, 3.6, 4]
        self.assertEqual(intersection_of_two(list1, list2), [2, 3.6])

    def test_strings_intersection(self):
        "Two lists of strings with common items"
        list1 = ["apple", "banana", "cherry"]
        list2 = ["banana", "cherry", "orange"]
        self.assertEqual(intersection_of_two(list1, list2), ["banana", "cherry"])

    def test_mixed_types_intersection(self):
        "Lists with mixed types (int, float, string)"
        list1 = [1, "apple", 3.5, 4]
        list2 = ["apple", 3.5, 2]
        self.assertEqual(intersection_of_two(list1, list2), ["apple", 3.5])

    def test_repeated_items_intersection(self):
        "Lists with repeated items"
        list1 = [1, 2, 3, 3, 4]
        list2 = [3, 3, 5]
        self.assertEqual(intersection_of_two(list1, list2), [3])

    def test_special_characters_intersection(self):
        "Lists with special character"
        list1 = ["!", "@", "%", "&", "&"]
        list2 = ["*", "!", "&"]
        self.assertEqual(intersection_of_two(list1, list2), ["!", "&"])

    # Edge cases

    def test_no_intersection(self):
        "test with no intersection should return an empty list"
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        self.assertEqual(intersection_of_two(list1, list2), [])

    def test_single_element_lists_with_intersection(self):
        "test with single item should return the single item in both"
        list1 = [1]
        list2 = [1]
        self.assertEqual(intersection_of_two(list1, list2), [1])

    def test_single_element_lists_no_intersection(self):
        "Should return an empty list"
        list1 = [1]
        list2 = [2]
        self.assertEqual(intersection_of_two(list1, list2), [])

    def test_duplicated_items_no_intersection(self):
        "lists with duplicated items ni intersection should return an empty list"
        list1 = [1, 2, 2, 3]
        list2 = [4, 4, 5]
        self.assertEqual(intersection_of_two(list1, list2), [])

    def test_different_types_but_equal_values(self):
        "should handle when items have different types but same value"
        list1 = [1, 2, 3.0]
        list2 = [3, 2, 1.0]
        self.assertEqual(intersection_of_two(list1, list2), [1, 2, 3.0])

    def test_sublist_intersection(self):
        "should return the sublist list"
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 3, 4]
        self.assertEqual(intersection_of_two(list1, list2), [2, 3, 4])

    def test_sublist_no_intersection(self):
        "should return an empty list"
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        self.assertEqual(intersection_of_two(list1, list2), [])

    def test_identical_lists(self):
        "should return a list with the identical items"
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        self.assertEqual(intersection_of_two(list1, list2), [1, 2, 3])

    def test_spaces_intersection(self):
        """Test with lists containing space characters."""
        list1 = [" ", 2, 3]
        list2 = ["A", " ", " "]
        self.assertEqual(intersection_of_two(list1, list2), [" "])

    def test_different_case_intersection(self):
        """Test case-sensitivity in intersection (should not match 'HELLO' with 'hello')."""
        list1 = ["HELLO", "KITTY", 3]
        list2 = ["hello", "kitty", " "]
        self.assertEqual(intersection_of_two(list1, list2), [])

    # Defensive tests

    def test_first_list_empty(self):
        """Test one empty list."""
        list1 = []
        list2 = [1, 2, 3]
        with self.assertRaises(AssertionError):
            intersection_of_two(list1, list2)

    def test_both_lists_empty(self):
        """Test both lists are empty."""
        list1 = []
        list2 = []
        with self.assertRaises(AssertionError):
            intersection_of_two(list1, list2)

    def test_any_non_list_input(self):
        """Test both lists are empty."""
        list1 = "cat"
        list2 = []
        with self.assertRaises(AssertionError):
            intersection_of_two(list1, list2)
