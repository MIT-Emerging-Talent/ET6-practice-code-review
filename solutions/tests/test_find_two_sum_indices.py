#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for find_two_sum_indices function.

Created on 2025-01-05

Author: Jeffery Offei Darko
"""

import unittest
from solutions.find_two_sum_indices import find_two_sum_indices


class TestFindTwoSumIndices(unittest.TestCase):
    # Basic tests
    def test_with_simple_target_sum(self):
        """Test basic case with a simple target sum."""
        self.assertEqual(find_two_sum_indices([2, 7, 11, 15], 9), [0, 1])

    def test_with_different_array_and_target(self):
        """Test basic case with a different array and target."""
        self.assertEqual(find_two_sum_indices([3, 2, 4], 6), [1, 2])

    def test_with_duplicates(self):
        """Test basic case with duplicate values."""
        self.assertEqual(find_two_sum_indices([3, 3], 6), [0, 1])

    # Edge cases with integers
    def test_with_negative_numbers(self):
        """Test case with negative numbers."""
        self.assertEqual(find_two_sum_indices([-3, 4, 3, 90], 0), [0, 2])

    def test_with_zeroes(self):
        """Test case where all numbers are zero."""
        self.assertEqual(find_two_sum_indices([0, 0, 0], 0), [0, 1])

    def test_with_large_numbers(self):
        """Test case with large integers."""
        self.assertEqual(
            find_two_sum_indices([1000000, 2500000, 1500000], 3500000), [0, 1]
        )

    # Cases where no solution exists
    def test_no_solution(self):
        """Test case where no solution exists."""
        with self.assertRaises(AssertionError):
            find_two_sum_indices([1, 2, 3], 7)

    def test_empty_list(self):
        """Test case with an empty list."""
        with self.assertRaises(AssertionError):
            find_two_sum_indices([], 5)

    def test_single_element(self):
        """Test case with a single element."""
        with self.assertRaises(AssertionError):
            find_two_sum_indices([1], 1)

    def test_repeated_elements(self):
        """Test case with repeated elements where no solution exists."""
        with self.assertRaises(AssertionError):
            find_two_sum_indices([1, 1, 1, 1], 3)

    # Tests with floats
    def test_with_floats_basic(self):
        """Test with floats that add up to the target."""
        self.assertEqual(find_two_sum_indices([2.5, 7.1, 11.3], 9.6), [0, 1])

    def test_with_floats_and_integers(self):
        """Test with a mix of floats and integers."""
        self.assertEqual(find_two_sum_indices([1, 2.5, 4.5], 7), [1, 2])

    def test_with_floats_no_solution(self):
        """Test with floats where no solution exists."""
        with self.assertRaises(AssertionError):
            find_two_sum_indices([1.2, 3.4, 5.6], 10)

    def test_with_float_target(self):
        """Test with a float target."""
        self.assertEqual(find_two_sum_indices([2, 3.5, 5], 8.5), [1, 2])

    def test_with_float_and_negative(self):
        """Test with floats and negative numbers."""
        self.assertEqual(find_two_sum_indices([-1.5, 3.0, 2.5], 1.0), [0, 2])

    # Invalid input tests
    def test_invalid_input_not_list(self):
        """Test with an invalid input that is not a list."""
        with self.assertRaises(AssertionError):
            find_two_sum_indices("123", 5)

    def test_invalid_input_with_non_number_elements(self):
        """Test with invalid input containing non-number elements."""
        with self.assertRaises(AssertionError):
            find_two_sum_indices([1, "two", 3], 5)

    def test_invalid_target_not_number(self):
        """Test with an invalid target that is not a number."""
        with self.assertRaises(AssertionError):
            find_two_sum_indices([1, 2, 3], "five")

    def test_invalid_input_none(self):
        """Test with an invalid input of None."""
        with self.assertRaises(AssertionError):
            find_two_sum_indices(None, 5)

    def test_invalid_target_none(self):
        """Test with an invalid target of None."""
        with self.assertRaises(AssertionError):
            find_two_sum_indices([1, 2, 3], None)

    # Edge cases for precision and NaN
    def test_with_precision(self):
        """Test edge case with float precision."""
        self.assertEqual(find_two_sum_indices([1.0000001, 2.9999999], 4.0), [0, 1])

    def test_with_nan(self):
        """Test with NaN input or target."""
        with self.assertRaises(AssertionError):
            find_two_sum_indices([float("nan"), 2.5], float("nan"))

    def test_with_zero_target(self):
        """Test when the target is zero."""
        self.assertEqual(find_two_sum_indices([-1, 1, 2], 0), [0, 1])


if __name__ == "__main__":
    unittest.main()
