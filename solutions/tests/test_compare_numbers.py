#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module is the test function of the compare_numbers
Created on 12 24 2024

@author: Osei Agyemang Sarfo
"""

import unittest


from ..compare_numbers import compare_numbers


class TestCompareNumbers(unittest.TestCase):
    """Test displays the outcome of comparing two integers"""

    def three_digit_integers(self):
        "It should evaluate (234,786) to 234"
        actual = compare_numbers(234, 786)  # Calls function with test argument.
        expected = 234  # Hand written answer.
        self.assertEqual(actual, expected)

    def two_digit_integers(self):
        "It should evaluate (37,40) to 37"
        actual = compare_numbers(37, 40)  # Call function with test argument
        expected = 37  # Hand written answer
        self.assertEqual(actual, expected)

    def same_integers(self):
        "It should evaluate (7,7) to 14"
        actual = compare_numbers(7, 7)  # Call function with test argument
        expected = 14  # Hand written answer
        self.assertEqual(actual, expected)

    def test_not_integer(self):
        """It should raise an assertion error if the argument is less than 0"""
        with self.assertRaises(AssertionError):
            compare_numbers(34, 90.0)

    def four_digit_integers(self):
        "It should evaluate (6577,5907) to 6577"
        actual = compare_numbers(6577, 5907)  # Call function with test argument
        expected = 6577  # Hand written answer
        self.assertEqual(actual, expected)

    def test_not_strings(self):
        """It should raise an assertion error if the argument is less than 0"""
        with self.assertRaises(AssertionError):
            compare_numbers("89", "90.0")
            
    def test_string_integer(self):
        """It should raise an assertion error if the argument is less than 0"""
        with self.assertRaises(AssertionError):
            compare_numbers("34", 90)

    def test_string_float(self):
        """It should raise an assertion error if the argument is less than 0"""
        with self.assertRaises(AssertionError):
            compare_numbers("76", 90.0)
