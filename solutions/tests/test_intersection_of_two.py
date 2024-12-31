#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the intersection_of_two function.
Contains comprehensive tests to ensure the correctness
of the intersection_of_two function.
It is designed to work with lists containing any data type allowed in a list.
Lists cannot be empty.

Test categories:

    - Standard cases: Lists with common items, lists with special characters.,
        lists with mixed data types,


    - Edge cases: Lists with no intersection, single-element lists, duplicated items,
        different types but equal values, lists with spaces items,
        sublist intersection, different case items

    - Defensive tests: Non-list inputs, one empty list, both empty lists

Created on 30-12-2024
Author: Linah Khayri
"""

import unittest

from ..intersection_of_two import intersection_of_two


class TestIntersectionOfTwo(unittest.TestCase):
    """Test suite for the intersection_of_two function that handles different cases."""

    # Standard cases

    def test_numbers_intersection(self):
        """Test intersection of two lists containing numbers (int or float)."""
        list1 = [1, 2, 3.6]
        list2 = [2, 3.6, 4]
        self.assertEqual(intersection_of_two(list1, list2), [2, 3.6])

    def test_strings_intersection(self):
        """Test intersection of two lists containing strings with common items."""
        list1 = ["apple", "banana", "cherry"]
        list2 = ["banana", "cherry", "orange"]
        self.assertEqual(intersection_of_two(list1, list2), ["banana", "cherry"])

    def test_special_characters_intersection(self):
        """Test intersection of lists with special characters."""
        list1 = ["!", "@", "%", "&", "&"]
        list2 = ["*", "!", "&"]
        self.assertEqual(intersection_of_two(list1, list2), ["!", "&"])

    def test_mixed_types_intersection(self):
        """Test intersection of lists with mixed types (int, float, string, etc.)."""
        list1 = [1, "apple", 3.5, 4, "*"]
        list2 = ["apple", "*", 3.5, 2]
        self.assertEqual(intersection_of_two(list1, list2), ["apple", 3.5, "*"])

    # Edge cases

    def test_no_intersection(self):
        """Test with no intersection; should return an empty list."""
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        self.assertEqual(intersection_of_two(list1, list2), [])

    def test_single_element_lists_with_intersection(self):
        """Should return the list with the single item"""
        list1 = [1]
        list2 = [1]
        self.assertEqual(intersection_of_two(list1, list2), [1])

    def test_single_element_lists_no_intersection(self):
        """Should return an empty list."""
        list1 = [1]
        list2 = [2]
        self.assertEqual(intersection_of_two(list1, list2), [])

    def test_duplicated_items_intersection(self):
        """Should return the common duplicated item once"""
        list1 = [1, 2, 3, 3, 4]
        list2 = [3, 3, 5]
        self.assertEqual(intersection_of_two(list1, list2), [3])

    def test_duplicated_items_no_intersection(self):
        """Test lists with duplicated items and no intersection; should return an empty list."""
        list1 = [1, 2, 2, 3]
        list2 = [4, 4, 5]
        self.assertEqual(intersection_of_two(list1, list2), [])

    def test_different_types_but_equal_values(self):
        """Test when items have different types but equal values (e.g., int and whole float)."""
        list1 = [1, 2, 3.0]
        list2 = [3, 2, 1.0]
        self.assertEqual(intersection_of_two(list1, list2), [1, 2, 3.0])

    def test_sublist_intersection(self):
        """Test intersection when one list is a sublist of the other."""
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 3, 4]
        self.assertEqual(intersection_of_two(list1, list2), [2, 3, 4])

    def test_identical_lists(self):
        """Test when two identical lists are passed; should return the list itself."""
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        self.assertEqual(intersection_of_two(list1, list2), [1, 2, 3])

    def test_spaces_intersection(self):
        """Test lists containing spaces as items; lists should handle spaces"""
        list1 = [" ", 2, 3]
        list2 = ["A", " ", " "]
        self.assertEqual(intersection_of_two(list1, list2), [" "])

    def test_different_case_intersection(self):
        """Test case-sensitivity in intersection (should not match 'HELLO' with 'hello')."""
        list1 = ["HELLO", "KITTY", 3]
        list2 = ["hello", "kitty", " "]
        self.assertEqual(intersection_of_two(list1, list2), [])

    # Defensive tests

    def test_one_empty_list(self):
        """Test when the one of the lists is empty."""
        list1 = []
        list2 = [1, 2, 3]
        with self.assertRaises(AssertionError):
            intersection_of_two(list1, list2)

    def test_both_lists_empty(self):
        """Test when both lists are empty."""
        list1 = []
        list2 = []
        with self.assertRaises(AssertionError):
            intersection_of_two(list1, list2)

    def test_any_non_list_input(self):
        """Test when any of the inputs is not a list."""
        list1 = "cat"
        list2 = []
        with self.assertRaises(AssertionError):
            intersection_of_two(list1, list2)
