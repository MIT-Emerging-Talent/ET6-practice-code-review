#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the standard_deviation function.

Test categories:
    - Standard cases: Verifies normal function behavior
    - Edge cases: Tests boundaries and extreme values
    - Defensive tests: Handles invalid or malicious inputs
    - Side effect test: Ensuring that the function has no side effects

Created on 30 12 2024
MIT Alpha Project Group
Author: Salih Adam
"""

import unittest
from ..standard_deviation import standard_deviation


class TestStandardDeviation(unittest.TestCase):
    """Test suite for the standard_deviation function"""

    # Standard test cases

    def test_positive_list(self):
        """It should return the standard deviation of the list"""
        actual = standard_deviation([13, 45.11, 32, 25.25, 20.01])
        expected = 10.96
        self.assertEqual(actual, expected)

    def test_negative_list(self):
        """It should return the standard deviation of the list"""
        actual = standard_deviation([-87.43, -90, -63.08, -11.07, -27])
        expected = 31.79
        self.assertEqual(actual, expected)

    def test_long_list(self):
        """It should return the standard deviation of the list"""
        actual = standard_deviation([-65.6, 74, 23, 19.7, -4, 27, 99.5, 8, 67.8, 1])
        expected = 44.42
        self.assertEqual(actual, expected)

    def test_list_of_two(self):
        """It should return the standard deviation of the list"""
        actual = standard_deviation([93.7, 276])
        expected = 91.15
        self.assertEqual(actual, expected)

    # Edge cases

    def test_no_variation_list(self):
        """It should return 0 as there is no variation"""
        actual = standard_deviation([67, 67, 67, 67, 67])
        expected = 0
        self.assertEqual(actual, expected)

    def test_small_variation_list(self):
        """It should round the small variation down to 0"""
        actual = standard_deviation([0.998, 0.996, 1, 1.004, 1.008])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_item_list(self):
        """It should return 0 as there no variation in a single number"""
        actual = standard_deviation([99])
        expected = 0
        self.assertEqual(actual, expected)

    # Defensive tests

    def test_non_list_input(self):
        """It should raise AssertionError if input is not a list"""
        with self.assertRaises(AssertionError):
            standard_deviation(10)

    def test_empty_list_input(self):
        """It should raise AssertionError if input is an empty list"""
        with self.assertRaises(AssertionError):
            standard_deviation([])

    def test_list_items_not_integers_or_floats(self):
        """It should raise AssertionError if list items are not integers or float"""
        with self.assertRaises(AssertionError):
            standard_deviation([55, "-222", 177.65, "thirty", 86])

    # Testing side effects

    def test_side_effect(self):
        """The input argument should not change after calling the function"""
        numbers = [2, 45, 33, 11.67, -9.55]
        standard_deviation(numbers)
        self.assertEqual(numbers, [2, 45, 33, 11.67, -9.55])
