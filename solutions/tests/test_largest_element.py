# pylint: disable=relative-beyond-top-level
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_largest_element.py

This module tests the largest element function which returns the largest
element in a list of numbers.

Created on Dec 21, 2024

@author: Meklit Gebregiorgis
"""

import unittest

from ..largest_element import largest_element


class TestLargeNumbers(unittest.TestCase):
    """Test for the largest_element function"""

    def test_positive_numbers(self):
        """It should correctly display the largest positive number"""
        actual = largest_element([1, 2, 3])
        expected = 3
        self.assertEqual(actual, expected)

    def test_negative_numbers(self):
        """It should correctly display the largest negative number"""
        actual = largest_element([-1, -2, -3])
        expected = -1
        self.assertEqual(actual, expected)

    def test_mixed_numbers(self):
        """It should correctly display the largest value"""
        actual = largest_element([-1, 0, 2.5])
        expected = 2.5
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """It should correctly return None"""
        actual = largest_element([])
        expected = None
        self.assertEqual(actual, expected)

    def test_same_numbers(self):
        """It should display the number"""
        actual = largest_element([6, 6, 6])
        expected = 6
        self.assertEqual(actual, expected)

    def test_one_element(self):
        """It should display the one element"""
        actual = largest_element([1])
        expected = 1
        self.assertEqual(actual, expected)
