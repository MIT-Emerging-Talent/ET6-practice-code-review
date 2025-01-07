#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A test module that tests the split_and_add function.

"""

import unittest
from ..split_and_add import split_and_add


class TestSplitAndAdd(unittest.TestCase):
    """This module tests the split_and_add function"""

    def test_list_of_numbers(self):
        """This test should pass"""
        self.assertEqual(split_and_add([2, 5, 7, 9], 3), [9, 2, 5, 7])

    def test_list_of_string(self):
        """It should return the expected value"""
        actual = split_and_add(["peter", "two", "boy", "mat", "three", "bloom"], 4)
        expected = ["three", "bloom", "peter", "two", "boy", "mat"]
        self.assertEqual(actual, expected)

    def test_list_mixed_with_number_and_string(self):
        """It should return the expected value"""
        actual = split_and_add([9, "four", 3, 6, "you", "act", "rope"], 2)
        expected = [3, 6, "you", "act", "rope", 9, "four"]
        self.assertEqual(actual, expected)

    def test_negative_integer_index_within_range(self):
        """ """
        actual = split_and_add([3, 6, "you", "act", "rope", 9, "four"], -3)
        expected = ["rope", 9, "four", 3, 6, "you", "act"]
        self.assertEqual(actual, expected)

    def test_zero_index(self):
        """It should return the input list when the index is zero"""
        actual = split_and_add(["pull", "bag", "toy", "earth"], 0)
        expected = ["pull", "bag", "toy", "earth"]
        self.assertEqual(actual, expected)

    def test_positive_index_outside_range(self):
        """Returns the input list when the index is greater than the length of the list"""
        actual = split_and_add(["peter", "two", "boy", "mat", "three", "bloom"], 7)
        expected = ["peter", "two", "boy", "mat", "three", "bloom"]
        self.assertEqual(actual, expected)

    def test_negative_index_outside_range(self):
        """It should return the input list when the negative index is less than"""
        actual = split_and_add(["peter", "two", "boy", "mat", "three", "bloom"], -7)
        expected = ["peter", "two", "boy", "mat", "three", "bloom"]
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """It should return an empty list"""
        self.assertEqual(split_and_add([], 2), [])

    def test_single_list_element(self):
        """It should return the list"""
        self.assertEqual(split_and_add([4], 1), [4])

    def test_non_integer_index(self):
        """It should raise an AssertionError for a non integer index"""
        with self.assertRaises(AssertionError):
            split_and_add(["ten", "set", "gloat", "gan"], "one")

    def test_float_index(self):
        """It should raise an AssertionError for a float index"""
        with self.assertRaises(AssertionError):
            split_and_add(["4", "5", "6", "9"], 2.0)

    def test_non_list_input(self):
        """Raises an AssertionError when first input is not a list"""
        with self.assertRaises(AssertionError):
            split_and_add("groove", 3)


if __name__ == "__main__":
    unittest.main()
