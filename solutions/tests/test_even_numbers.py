#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Test module to check is a number is even

Created on 2025-01-11

Author:Martha Yelademe Nyekanga
"""

import unittest
from ..even_numbers import is_even


class TestIsEven(unittest.TestCase):
    # Test case for a positive even number
    def test_positive_even(self):
        self.assertTrue(is_even(2))

    # Test case for a positive odd number
    def test_positive_odd(self):
        self.assertFalse(is_even(3))

    # Test case for zero (edge case)
    def test_zero(self):
        self.assertTrue(is_even(0))

    # Test case for a negative even number
    def test_negative_even(self):
        self.assertTrue(is_even(-4))

    # Test case for a negative odd number
    def test_negative_odd(self):
        self.assertFalse(is_even(-7))

    # Test case for a large positive even number
    def test_large_even(self):
        self.assertTrue(is_even(1000000))

    # Test case for a large positive odd number
    def test_large_odd(self):
        self.assertFalse(is_even(1000001))

    # Test case for a small positive even number
    def test_small_even(self):
        self.assertTrue(is_even(2))

    # Test case for a small positive odd number
    def test_small_odd(self):
        self.assertFalse(is_even(1))

    # Test case to check if a float raises a TypeError
    def test_type_error_with_float(self):
        with self.assertRaises(AssertionError):
            is_even(4.5)

    # Test case to check if a string raises a TypeError
    def test_type_error_with_string(self):
        with self.assertRaises(AssertionError):
            is_even("10")

    # Test case to check if a list raises a TypeError
    def test_type_error_with_list(self):
        with self.assertRaises(AssertionError):
            is_even([2])

    # Test case to check if a dictionary raises a TypeError
    def test_type_error_with_dict(self):
        with self.assertRaises(AssertionError):
            is_even({"number": 4})

    # Test case to check if None raises a TypeError
    def test_type_error_with_none(self):
        with self.assertRaises(AssertionError):
            is_even(None)

    # Test case to check if a boolean raises a TypeError
    def test_type_error_with_bool(self):
        with self.assertRaises(AssertionError):
            is_even(True)
