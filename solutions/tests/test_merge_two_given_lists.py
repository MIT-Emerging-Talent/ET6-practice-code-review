#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for merging two lists of items.

Module contents:
    -merge two lists

Created on 2025-01-08
@author: Ajanduna Emmanuel
"""

import unittest

from merge_two_given_lists import merge_two_given_lists


class TestMergeTwoGivenLists(unittest.TestCase):
    """
    Test cases for the merge_two_given_lists function.
    """

    def test_merge_two_non_empty_lists(self):
        """
        Test merging two non-empty lists of integers.
        """
        result = merge_two_given_lists([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_merge_list_with_empty_list(self):
        """
        Test merging a non-empty list with an empty list.
        """
        result = merge_two_given_lists([1, 2, 3], [])
        self.assertEqual(result, [1, 2, 3])

    def test_merge_empty_list_with_non_empty_list(self):
        """
        Test merging an empty list with a non-empty list.
        """
        result = merge_two_given_lists([], [1, 2, 3])
        self.assertEqual(result, [1, 2, 3])

    def test_merge_lists_with_strings(self):
        """
        Test merging two non-empty lists of strings.
        """
        result = merge_two_given_lists(["a", "b"], ["c", "d"])
        self.assertEqual(result, ["a", "b", "c", "d"])

    def test_merge_list_with_empty_list_of_strings(self):
        """
        Test merging a non-empty list of strings with an empty list.
        """
        result = merge_two_given_lists(["x", "y", "z"], [])
        self.assertEqual(result, ["x", "y", "z"])

    def test_merge_empty_list_with_non_empty_list_of_strings(self):
        """
        Test merging an empty list with a non-empty list of strings.
        """
        result = merge_two_given_lists([], ["m", "n", "o"])
        self.assertEqual(result, ["m", "n", "o"])

    def test_merge_lists_invalid_input(self):
        """
        Test merging with invalid input types.
        """
        with self.assertRaises(TypeError):
            merge_two_given_lists([1, 2, 3], "not a list")
        with self.assertRaises(TypeError):
            merge_two_given_lists("not a list", [1, 2, 3])

    def test_merge_lists_with_mixed_types(self):
        """
        Test merging lists containing mixed types.
        """
        result = merge_two_given_lists([1, "a"], [2, "b"])
        self.assertEqual(result, [1, "a", 2, "b"])


if __name__ == "__main__":
    unittest.main()
