#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides unit tests for the longest_consecutive_sequence function.

Test Categories:
Regular Passing Cases - Tests with typical inputs
Rare or Edge Cases - Tests with empty lists, single elements, and duplicates
Defensive Cases - Tests that verify error handling for invalid inputs

Created on: 2025/1/5
Author: Hamidullah Rajabi
"""

import unittest
from ..longest_consecutive_sequence import longest_consecutive_sequence


class TestLongestConsecutiveSequence(unittest.TestCase):
    """
    Unit tests for the longest_consecutive_sequence function.
    """

    # Regular Passing Cases

    def test_mixed_numbers(self):
        """
        Tests with a list containing mixed integers.
        """
        self.assertEqual(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]), 4)

    def test_negative_numbers(self):
        """
        Tests with a list containing negative numbers.
        """
        self.assertEqual(longest_consecutive_sequence([0, -1, 1, 2, 3, 7, 8, 9]), 5)

    # Rare or Edge Cases

    def test_empty_list(self):
        """
        Tests with an empty list.
        """
        self.assertEqual(longest_consecutive_sequence([]), 0)

    def test_single_element(self):
        """
        Tests with a list containing a single element.
        """
        self.assertEqual(longest_consecutive_sequence([42]), 1)

    def test_duplicates(self):
        """
        Tests with a list containing duplicates.
        """
        self.assertEqual(longest_consecutive_sequence([1, 2, 2, 3, 4, 5, 5, 6]), 6)

    # Defensive Cases That Raises Error

    def test_non_integer_elements(self):
        """
        Tests with a list containing non-integer elements.
        """
        with self.assertRaises(AssertionError):
            longest_consecutive_sequence([1, 2, "three", 4])

    def test_non_list_input(self):
        """
        Tests with non-list input.
        """
        with self.assertRaises(AssertionError):
            longest_consecutive_sequence("1234")

    def test_none_in_list(self):
        """
        Tests with a list containing None.
        """
        with self.assertRaises(ValueError):
            longest_consecutive_sequence([1, 2, None, 4])

    def test_nan_in_list(self):
        """
        Tests with a list containing NaN.
        """
        with self.assertRaises(ValueError):
            longest_consecutive_sequence([1, 2, float("nan"), 4])
