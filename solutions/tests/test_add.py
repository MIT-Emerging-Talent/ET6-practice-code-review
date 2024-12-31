#! usr/bin/python3
# -*- coding: utf-8 -*-

""" 
Test for addition of two numbers

Created on 28.12.2024
@author : Ridwan Ayinde


"""


import unittest
from solutions.add import add  # Import the function to test


class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        self.assertEqual(add(4, 6), 10)

    def test_add_negative_numbers(self):
        """Test add two negative numbers"""
        self.assertEqual(add(-4, -5), -9)

    def test_add_mixed_sign_numbers(self):
        """Test adding a positive and a negative number"""
        self.assertEqual(add(4, -5), -1)

    def test_add_zero(self):
        """Test adding zero to a number"""
        self.assertEqual(add(4, 0), 4)

    def test_non_numbers(self):
        """it should raise an AssertionError for non numbers input"""
        with self.assertRaises(AssertionError):
            add("a", 5)  # Invalid input: string instead of a number


if __name__ == "__main__":
    unittest.main()
