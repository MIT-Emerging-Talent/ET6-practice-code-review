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

    def test1(self):
        "It should evaluate (234,786) to 234"
        actual = compare_numbers(234, 786)  # Calls function with test argument.
        expected = 234  # Hand written answer.
        self.assertEqual(actual, expected)

    def test2(self):
        "It should evaluate (37,40) to 37"
        actual = compare_numbers(37, 40)  # Call function with test argument
        expected = 37  # Hand written answer
        self.assertEqual(actual, expected)

    def test3(self):
        "It should evaluate (7,7) to 14"
        actual = compare_numbers(7, 7)  # Call function with test argument
        expected = 14  # Hand written answer
        self.assertEqual(actual, expected)

    def test_not_integer(self):
        """It should raise an assertion error if the argument is less than 0"""
        with self.assertRaises(AssertionError):
            compare_numbers(34, 90.0)
