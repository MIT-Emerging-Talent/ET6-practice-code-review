#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test file code for if the `number is a Square` function.


"""


import unittest

from ..is_square import is_square


class TestIsSquare(unittest.TestCase):
    def test_negative_number(self):
        """It should return False for negative numbers."""
        actual = is_square(-1)
        expected = False
        self.assertEqual(actual, expected)

    def test_zero(self):
        """It should return True for zero."""
        actual = is_square(0)
        expected = True
        self.assertEqual(actual, expected)

    def test_one(self):
        """It should return True for one."""
        actual = is_square(1)
        expected = True
        self.assertEqual(actual, expected)

    def test_two(self):
        """It should return False for two."""
        actual = is_square(2)
        expected = False
        self.assertEqual(actual, expected)

    def test_three(self):
        """It should return False for three."""
        actual = is_square(3)
        expected = False
        self.assertEqual(actual, expected)

    def test_four(self):
        """It should return True for four."""
        actual = is_square(4)
        expected = True
        self.assertEqual(actual, expected)

    def test_nine(self):
        """It should return True for nine."""
        actual = is_square(9)
        expected = True
        self.assertEqual(actual, expected)

    def test_sixteen(self):
        """It should return True for sixteen."""
        actual = is_square(16)
        expected = True
        self.assertEqual(actual, expected)

    def test_twenty_five(self):
        """It should return True for twenty-five."""
        actual = is_square(25)
        expected = True
        self.assertEqual(actual, expected)

    def test_twenty_six(self):
        """It should return False for twenty-six."""
        actual = is_square(26)
        expected = False
        self.assertEqual(actual, expected)

    def test_thirty_six(self):
        """It should return True for thirty-six."""
        actual = is_square(36)
        expected = True
        self.assertEqual(actual, expected)

    def test_fifty(self):
        """It should return False for fifty."""
        actual = is_square(50)
        expected = False
        self.assertEqual(actual, expected)

    def test_hundred(self):
        """It should return True for one hundred."""
        actual = is_square(100)
        expected = True
        self.assertEqual(actual, expected)

    def test_one_hundred_one(self):
        """It should return False for one hundred one."""
        actual = is_square(101)
        expected = False
        self.assertEqual(actual, expected)
