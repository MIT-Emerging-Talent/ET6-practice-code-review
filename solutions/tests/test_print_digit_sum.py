#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 06 01 25

@author: Alona Niechvieieva
"""

import unittest


from ..print_digit_sum import print_digit_sum

class TestPrintDigitSum(unittest.TestCase):
    """Test the print_digit_sum function"""

    def test_0(self):
        """It should evaluate 0 to 0"""
        actual = print_digit_sum(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_single_digit(self):
        """It should correctly evaluate single-digit numbers"""
        actual = print_digit_sum(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_multiple_digits(self):
        """It should correctly evaluate multiple-digit numbers"""
        self.assertEqual(print_digit_sum(37), 10)
        self.assertEqual(print_digit_sum(13457), 20)

    def test_less_than_0(self):
        """It should raise an assertion error if the argument is less than 0"""
        with self.assertRaises(AssertionError):
            print_digit_sum(-1)

    def test_not_an_integer(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            print_digit_sum(1.0)

if __name__ == "__main__":
    unittest.main()