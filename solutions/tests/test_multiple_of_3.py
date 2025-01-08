# pylint: disable=relative-beyond-top-level
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_multiple_of_3.py

This module tests the multiple_of_3 function
Created on Jan 3, 2024

@author: Meklit Gebregiorgis
"""

import unittest
from ..multiple_of_3 import multiple_of_3


class TestMultipleOf3(unittest.TestCase):
    """Test class for multiple_of_3"""

    def test_3(self):
        """It should correctly display mutliples of 3 <= 15 starting at 3"""
        actual = multiple_of_3(3)
        expected = [3, 6, 9, 12, 15]
        self.assertEqual(actual, expected)

    def test_negative_3(self):
        """It should correctly display the multiples of 3 <=15 starting at -3"""
        actual = multiple_of_3(-3)
        expected = [-3, 0, 3, 6, 9, 12, 15]
        self.assertEqual(actual, expected)

    def test_0(self):
        """It should correctly display the multiples of 3 <=15 starting at 0"""
        actual = multiple_of_3(0)
        expected = [0, 3, 6, 9, 12, 15]
        self.assertEqual(actual, expected)

    def test_18(self):
        """It should display empty string as 18 is a value above 15"""
        actual = multiple_of_3(18)
        expected = []
        self.assertEqual(actual, expected)

    def test_15(self):
        """It should display 15"""
        actual = multiple_of_3(15)
        expected = [15]
        self.assertEqual(actual, expected)
