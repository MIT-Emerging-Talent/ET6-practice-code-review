#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for find_duplicates function.

Created on 2025-01-08
@author: AI Developer
"""

import unittest
from find_duplicates import find_duplicates


class TestFindDuplicates(unittest.TestCase):
    """Test suite for the find_duplicates function."""

    def test_empty_list(self):
        """Test empty list returns empty list."""
        self.assertEqual(find_duplicates([]), [])

    def test_no_duplicates(self):
        """Test list with no duplicates returns empty list."""
        self.assertEqual(find_duplicates([1, 2, 3, 4, 5]), [])

    def test_single_duplicate(self):
        """Test list with one duplicate item."""
        self.assertEqual(find_duplicates([1, 2, 2, 3]), [2])

    def test_multiple_duplicates(self):
        """Test list with multiple duplicate items."""
        self.assertEqual(find_duplicates([1, 2, 2, 3, 3, 3]), [2, 3])

    def test_all_duplicates(self):
        """Test list where all items are duplicates."""
        self.assertEqual(find_duplicates([1, 1, 1, 1]), [1])

    def test_string_duplicates(self):
        """Test list of strings with duplicates."""
        self.assertEqual(find_duplicates(["a", "b", "a", "c", "b"]), ["a", "b"])

    def test_mixed_types(self):
        """Test list with mixed types."""
        self.assertEqual(find_duplicates([1, "1", 1, "1"]), [1, "1"])

    def test_duplicate_order(self):
        """Test that duplicates are returned in order of first appearance."""
        self.assertEqual(find_duplicates([3, 1, 2, 1, 3]), [3, 1])

    def test_case_sensitive_strings(self):
        """Test that string comparison is case-sensitive."""
        self.assertEqual(find_duplicates(["A", "a", "A", "a"]), ["A", "a"])

    def test_nested_lists(self):
        """Test list containing nested lists."""
        self.assertEqual(find_duplicates([[1], [2], [1], [2]]), [[1], [2]])

    # Defensive tests
    def test_none_input(self):
        """Test that None input raises AssertionError."""
        with self.assertRaises(AssertionError):
            find_duplicates(None)

    def test_non_list_input(self):
        """Test that non-list input raises AssertionError."""
        with self.assertRaises(AssertionError):
            find_duplicates("not a list")

    def test_set_input(self):
        """Test that set input raises AssertionError."""
        with self.assertRaises(AssertionError):
            find_duplicates({1, 2, 3})

    def test_tuple_input(self):
        """Test that tuple input raises AssertionError."""
        with self.assertRaises(AssertionError):
            find_duplicates((1, 2, 3))


if __name__ == "__main__":
    unittest.main()
