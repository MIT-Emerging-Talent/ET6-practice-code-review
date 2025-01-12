#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test_sum_list.py
# Author: Jha-mal
"""
Module: test_sum_list

Unit tests for the 'sum_list' function.

Behavior:
- Contains a test class with multiple methods.
- Each test has exactly one assertion and no extra logic.
"""

import unittest

from ..sum_list import sum_list


class TestSumList(unittest.TestCase):
    """
    TestSumList provides unit tests for sum_list.
    """

    def test_sums_positive_integers(self):
        """
        Test that sum_list correctly sums positive integers.
        """
        self.assertEqual(sum_list([1, 2, 3]), 6)

    def test_sums_negative_numbers(self):
        """
        Test that sum_list correctly sums negative numbers.
        """
        self.assertEqual(sum_list([-1, -2, -3]), -6)

    def test_sums_mixed_numbers(self):
        """
        Test that sum_list correctly sums a mix of negative, positive, and floats.
        """
        self.assertEqual(sum_list([-1, 1, 2.5]), 2.5)

    def test_empty_list_returns_zero(self):
        """
        Test that sum_list returns 0 for an empty list.
        """
        self.assertEqual(sum_list([]), 0)

    def test_defensive_check_non_numeric(self):
        """
        Test that a TypeError is raised if non-numeric items are included.
        """
        with self.assertRaises(TypeError):
            sum_list([1, "two", 3])


if __name__ == "__main__":
    unittest.main()
