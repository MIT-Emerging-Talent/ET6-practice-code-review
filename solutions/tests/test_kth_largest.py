"""
Test module for kth largest in a list function.

This module contains unit tests for the kth largest in a list
function using the unittest framework.

Created: 04/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Ahd AbdelRahim
"""

import unittest

from ..kth_largest import kth_largest


class TestKthLargest(unittest.TestCase):
    """Test kth largest Function"""

    # BASE CASES
    def test_normal_case(self):
        """It should return the correct kth largest element"""
        actual = kth_largest(["3", "2", "1", "5", "6", "4"], 2)
        expected = "5"  # The result should be a string
        self.assertEqual(actual, expected)

    def test_duplicate_elements(self):
        """It should return the correct kth largest element"""
        actual = kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 4)
        expected = "4"  # The result should be a string
        self.assertEqual(actual, expected)

    def test_k_is_one(self):
        """It should return the largest element in the list"""
        actual = kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 1)
        expected = "6"
        self.assertEqual(actual, expected)

    # EDGE CASES
    def test_k_is_greater_than_list_length(self):
        """It should return the smallest element in the list"""
        actual = kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 9)
        expected = "1"
        self.assertEqual(actual, expected)

    def test_single_element(self):
        """It should return the only element when the list has one element"""
        actual = kth_largest(["42"], 1)
        expected = "42"
        self.assertEqual(actual, expected)

    def test_sorted_list_k_is_1(self):
        """It should return the largest element when the list is sorted"""
        actual = kth_largest(["1", "2", "3", "4", "5"], 1)
        expected = "5"
        self.assertEqual(actual, expected)

    def test_identical_elements(self):
        """It should return the correct kth largest element when all elements are identical"""
        actual = kth_largest(["7", "7", "7", "7"], 3)
        expected = "7"
        self.assertEqual(actual, expected)

    def test_large_number(self):
        """It should return the correct kth largest element when the numbers are large"""
        actual = kth_largest(["1000000", "1", "5000"], 2)
        expected = "5000"
        self.assertEqual(actual, expected)

    # DEFENSIVE CASES
    def test_zero_case(self):
        """It should raise an IndexError for an empty list"""
        with self.assertRaises(IndexError):  # Expect an error for empty list input
            kth_largest([], 1)

    # WhyIndexError?: there's no element at position 0.

    def test_non_numeric_strings(self):
        """It should raise a ValueError if non-numeric strings are included"""
        with self.assertRaises(ValueError):
            kth_largest(["apple", "banana", "cherry"], 2)

    def test_k_is_negative(self):
        with self.assertRaises(IndexError):
            kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], -1)

    def test_k_is_zero(self):
        with self.assertRaises(IndexError):
            kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 0)
