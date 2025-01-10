#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test module for sum_positive_numbers function.

Contains tests for summing positive numbers in a list, handling edge cases, and ensuring
proper input validation.

Test categories:
    - Functionality tests: checking if the function correctly sums positive numbers and
      ignores negatives or zeros
    - Edge cases: testing with empty lists, lists with only negative numbers or zeros,
      and lists with mixed data types
    - Defensive tests: incorrect input types such as non-list values or lists contains
    non-numeric data


Created on 2025-01-10
Author: Huda Alamassi
"""

import unittest

from solutions.sum_positive_numbers import sum_positive_numbers


class TestSumPositiveNumbers(unittest.TestCase):
    """Test the sum_positive_numbers function."""

    def test_sum_with_positive_numbers(self):
        """It should return the correct sum of positive numbers."""
        actual = sum_positive_numbers([1, 2, 3])
        self.assertEqual(actual, 6)

    def test_floats_and_integers(self):
        """It should return the sum of both positive integers and floats properly."""
        actual = sum_positive_numbers([1.5, 2, 3.5])
        self.assertEqual(actual, 7.0)

    def test_sum_with_mixed_numbers(self):
        """It should return the sum of the positive numbers and ignore negative numbers and zeros"""
        actual = sum_positive_numbers([5, 0, 10.5, -2, 3])
        self.assertEqual(actual, 18.5)

    def test_single_positive_number(self):
        """It should return the single positive number."""
        actual = sum_positive_numbers([7])
        self.assertEqual(actual, 7)

    def test_sum_with_no_positive_numbers(self):
        """It should return 0 if there are no positive numbers."""
        actual = sum_positive_numbers([-1, -2, -3])
        self.assertEqual(actual, 0)

    def test_empty_list(self):
        """It should return 0 if the list is empty."""
        actual = sum_positive_numbers([])
        self.assertEqual(actual, 0)

    def test_list_with_only_zeros(self):
        """It should return 0 if the list contains only zeros."""
        actual = sum_positive_numbers([0, 0, 0])
        self.assertEqual(actual, 0)

    def test_single_negative_number(self):
        """It should return 0 if the list contains only a single negative number."""
        actual = sum_positive_numbers([-5])
        self.assertEqual(actual, 0)

    # Test defensive assertions
    def test_defensive_assertion_for_non_list_input(self):
        """Test that an assertion is raised if the input is not a list."""
        with self.assertRaises(AssertionError):
            sum_positive_numbers(123)

    def test_defensive_assertion_for_non_numeric_elements(self):
        """Test that an assertion is raised if the list contains non-numeric elements."""
        with self.assertRaises(AssertionError):
            sum_positive_numbers([1, "a", 3])  # list contains a non-numeric element
