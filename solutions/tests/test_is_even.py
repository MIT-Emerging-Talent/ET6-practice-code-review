#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@Luyando Ennie Chitindi
"""

import unittest
from solutions.is_even import is_even


class TestIsEven(unittest.TestCase):
    """Test the is_even function"""


def test_even_number(self):
    """It should evaluate 4 to true"""
    actual = is_even(4)
    expected = True
    self.assertEqual(actual, expected)


def test_odd_number(self):
    """It should evaluate 3 to False"""
    actual = is_even(3)
    expected = False
    self.assertEqual(actual, expected)


def test_zero(self):
    """It should evaluate 0 to True"""
    actual = is_even(0)
    expected = True
    self.assertEqual(actual, expected)


def test_negative_even_number(self):
    """It should evaluate -2 to True"""
    actual = is_even(-2)
    expected = True
    self.assertEqual(actual, expected)


def test_negative_odd_number(self):
    """It should evaluate -3 to False"""
    actual = is_even(-3)
    expected = False
    self.assertEqual(actual, expected)


def test_non_integer_input(self):
    """It should raise an assertion error if the argument is not an integer"""
    with self.assertRaises(AssertionError):
        is_even(3.5)

    with self.assertRaises(AssertionError):
        is_even("string")


def test_less_than_0(self):
    """It should raise an assertion error if the argument is less than 0"""
    with self.assertRaises(AssertionError):
        is_even(-2.5)


if __name__ == "__main__":
    unittest.main()
