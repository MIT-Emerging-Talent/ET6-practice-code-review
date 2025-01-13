#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 06 01 25

@author: Alona Niechvieieva
"""

import unittest

from ..digit_sum import digit_sum  # type: ignore # noqa: E402

""" A module for testing the function that computes the sum of digits of a number
Module contents: TestTestDigitSum: unit tests for the `digit_sum` function.
"""


class TestDigitSum(unittest.TestCase):
    """Test the digit_sum function"""

    def test_0(self):
        # It should evaluate 0 to 0
        self.assertEqual(digit_sum(0), 0)

    def test_single_digit(self):
        # It should correctly evaluate single-digit numbers
        self.assertEqual(digit_sum(5), 5)

    def test_two_digit_number(self):
        # It should correctly calculate the sum of digits for a two-digit number
        self.assertEqual(digit_sum(37), 10)

    def test_multiple_digit_number(self):
        # It should correctly calculate the sum of digits for a five-digit number
        self.assertEqual(digit_sum(13457), 20)

    def test_less_than_0(self):
        # It should raise an assertion error if the argument is less than 0
        with self.assertRaises(AssertionError):
            digit_sum(-1)

    def test_not_an_integer(self):
        # It should raise an assertion error if the argument is not an integer
        with self.assertRaises(AssertionError):
            digit_sum(1.0)


# Run the unit tests when the script is executed directly
if __name__ == "__main__":
    unittest.main()
