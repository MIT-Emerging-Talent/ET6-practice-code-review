#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for testing the sum_of_list function.

Test categories:
    - Standard cases:
    - Edge cases:
    - Defensive tests:

Created on 02/01/2025
@author: Ndubuisi Agbo
"""

import unittest
from ..sum_of_list import sum_of_list


class TestSumOfList(unittest.TestCase):
    """This module tests the sum_of_list function"""

    # Standard test cases
    def test_list_of_integers_input(self):
        """It should return the sum of the list"""
        self.assertEqual(sum_of_list([3, 6, 9]), 18)

    def test_list_of_floats_input(self):
        """It should return the sum of the list"""
        self.assertEqual(sum_of_list([4.2, 6.9, 7.1]), 18.2)

    def test_list_of_mixed_number_input(self):
        """It should return the sum of the list"""
        self.assertEqual(sum_of_list([8, 3.8, 1, 9]), 21.8)

    # Edge cases
    def test_empty_list_input(self):
        """Returns zero when an empty list is passed"""
        self.assertEqual(sum_of_list([]), 0)
    
    def test_single_element(self):
        """"It should return the element in the list"""
        self.assertEqual(sum_of_list([7]), 7)
    
    # Defensive tests
    def test_list_of_strings(self):
        """Raises AssertionError when a list containing a string is passed"""
        with self.assertRaises(AssertionError):
            sum_of_list(["3", "9", "6"])

    def test_non_list_input(self):
        """Raises AssertionError when a non-list is passed"""
        with self.assertRaises(AssertionError):
            sum_of_list("two")




if __name__ == "__main__":
    unittest.main()