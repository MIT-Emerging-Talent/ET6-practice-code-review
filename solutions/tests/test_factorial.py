#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 01-03-2024

@author: Abdul Qader Dost
"""

import unittest

from ..factorial import factorial


class TestFactorial(unittest.TestCase):
    """Test the absolute_value function"""

    def test_factorial_of_zero(self):
        """It should return 1 for the special case of zero, where 0! = 1."""
        actual = factorial(0)
        expected = 1
        self.assertEqual(actual, expected)

    def test_factorial_of_one(self):
        """It should return 1 when the input is 1, as 1! equals 1."""
        actual = factorial(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_factorial_of_two(self):
        """It should return 1 when the input is 2, as 2! equals 2."""
        actual = factorial(2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_factorial_of_three(self):
        """It should return 1 when the input is 3, as 3! equals 6."""
        actual = factorial(3)
        expected = 6
        self.assertEqual(actual, expected)

    def test_factorial_of_four(self):
        """It should return 1 when the input is 4, as 4! equals 24."""
        actual = factorial(4)
        expected = 24
        self.assertEqual(actual, expected)
