#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Monday/ 30/ December/2024
@author: Mayar Ali

"""

import unittest

# --- imports & test class before documenting and testing ---

# from ..TestEvenNumberCount import TestEvenNumberCount

# class TestTestEvenNumberCount(unittest.TestCase):

# --- imports & test class after documenting and testing ---

from ..even_number_count import even_number_count # type: ignore

class TestEvenNumberCount(unittest.TestCase):
    """test the even_number_count function """

    def test_0(self):
        """It should return zero"""
        self.assertEqual(even_number_count([1]), 0)

    def test_1(self):
        """It should count the number of even numbers in a countdown from n to 1 """
        self.assertEqual(even_number_count([1,2]), 1)

    def test_2(self):
        """It should count the number of even numbers in a countdown from n to 1 """
        self.assertEqual(even_number_count([1,2,3]), 1)

    def test_3(self):
        """It should count the number of even numbers in a countdown from n to 1 """
        self.assertEqual(even_number_count([1,2,3,4]), 2)
    
    def test_4(self):
        """It should count the number of even numbers in a countdown from n to 1 """
        self.assertEqual(even_number_count([1,2,3,4,5]), 2)

    def test_5(self):
        """It should count the number of even numbers in a countdown from n to 1 """
        self.assertEqual(even_number_count([1,2,3,4,5,6]), 3)   

    def test_6(self):
        """It should count the number of even numbers in a countdown from n to 1 """
        self.assertEqual(even_number_count([1,2,3,4,5,6,7]), 3)   