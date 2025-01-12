#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the print_odd_numbers_in_list function.

Created on: 01 01 25
@author: Muhammad Shahroz
"""

import unittest
from ..filter_odd_numbers import filter_odd_numbers


class TestFilterOddNumbers(unittest.TestCase):
    """
    Unit tests for the filter_odd_numbers function.
    """

    def test_empty_list(self):
        """It should return an empty list for an empty input."""
        self.assertEqual(filter_odd_numbers([]), [])

    def test_all_integers(self):
        """It should filter odd numbers from a list of integers."""
        self.assertEqual(filter_odd_numbers([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_negative_integers(self):
        """It should handle negative integers correctly."""
        self.assertEqual(filter_odd_numbers([-1, -2, -3, -4, -5]), [-1, -3, -5])

    def test_mixed_types(self):
        """It should ignore non-integer inputs."""
        self.assertEqual(filter_odd_numbers([1, 2, "three", 4.5, None]), [1])

    def test_all_floats(self):
        """It should return an empty list if all elements are floats."""
        self.assertEqual(filter_odd_numbers([1.1, 2.2, 3.3]), [])

    def test_all_strings(self):
        """It should return an empty list if all elements are strings."""
        self.assertEqual(filter_odd_numbers(["one", "two", "three"]), [])


if __name__ == "__main__":
    unittest.main()
