#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the sum_of_digits function

Created on 25 Dec 2024
@author: Noorelsalam Almakki
"""

import unittest
from ..sum_of_digits import sum_of_digits


class TestSumOfDigits(unittest.TestCase):
    """A class for testing the sum_of_digits function"""

    def test_0(self):
        """Test the sum_of_digits function with 0"""
        self.assertEqual(sum_of_digits(0), 0)

    def test_one_digit(self):
        """Test the sum_of_digits function with one digit"""
        self.assertEqual(sum_of_digits(5), 5)

    def test_2_digits(self):
        """Test the sum_of_digits function with a 2-digit number"""
        self.assertEqual(sum_of_digits(12), 3)

    def test_6_digits(self):
        """Test the sum_of_digits function with a 6-digit number"""
        self.assertEqual(sum_of_digits(123456), 21)

    def test_large_number(self):
        """Test the sum_of_digits function with a large number"""
        self.assertEqual(sum_of_digits(1234567890), 45)

    def test_negative_number(self):
        """Test the sum_of_digits function with a negative number"""
        self.assertEqual(sum_of_digits(-123), -6)

    def test_large_negative_number(self):
        """Test the sum_of_digits function with a large negative number"""
        self.assertEqual(sum_of_digits(-1234567890), -45)

    def test_not_an_integer(self):
        """Test the sum_of_digits function with a non-integer number"""
        with self.assertRaises(AssertionError):
            sum_of_digits(12.4)
