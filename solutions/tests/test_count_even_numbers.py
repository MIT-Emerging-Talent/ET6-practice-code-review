#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on January 4, 2025

@author: Norbert Ndayisenga
"""

import unittest
from ..count_even_numbers import count_even_numbers


class TestCountEvenNumbers(unittest.TestCase):
    """Test the count_even_numbers function"""

    def test_empty_list(self):
        """It should return 0 for an empty list"""
        self.assertEqual(count_even_numbers([]), 0)

    def test_all_even_numbers(self):
        """It should return the correct count for a list of only even numbers"""
        self.assertEqual(count_even_numbers([2, 4, 6, 8, 10]), 5)

    def test_all_odd_numbers(self):
        """It should return 0 for a list of only odd numbers"""
        self.assertEqual(count_even_numbers([1, 3, 5, 7, 9]), 0)

    def test_mixed_numbers(self):
        """It should correctly count only the even numbers in a mixed list"""
        self.assertEqual(count_even_numbers([1, 2, 3, 4, 5, 6]), 3)

    def test_negative_even_numbers(self):
        """It should handle negative even numbers correctly"""
        self.assertEqual(count_even_numbers([-2, -4, -6, -8]), 4)

    def test_non_integer_values(self):
        """It should raise an assertion error for non-integer values"""
        with self.assertRaises(AssertionError):
            count_even_numbers([1, 2, "three", 4.5])

    def test_large_numbers(self):
        """It should correctly count even numbers for large inputs"""
        self.assertEqual(count_even_numbers([10**6, 10**9, 2**10, 2**15, 1]), 4)
