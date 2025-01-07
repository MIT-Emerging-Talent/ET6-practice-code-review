#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the sum_elements function

Created on 2025-01-06

@author: Rumiya Ismatova
"""

import unittest
from solutions.sum_elements import sum_elements

class TestSumElements(unittest.TestCase):
    """
    Unit test class for verifying the functionality of the `sum_elements` function.
    """

    def test_positive_numbers(self):
        """
        Test the function with a list of positive numbers.
        Ensures the sum is calculated correctly.
        """
        self.assertEqual(sum_elements([1, 2, 3]), 6)

    def test_negative_numbers(self):
        """
        Test the function with a list of negative numbers.
        Ensures the sum is calculated correctly.
        """
        self.assertEqual(sum_elements([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        """
        Test the function with a list containing positive, negative, and zero values.
        Ensures the sum is calculated correctly.
        """
        self.assertEqual(sum_elements([-1, 0, 1]), 0)

    def test_empty_list(self):
        """
        Test the function with an empty list.
        Ensures the function returns 0 for an empty list.
        """
        self.assertEqual(sum_elements([]), 0)
        
    def test_non_integer_list(self):
        """ 
        It should raise value error is not all elements are integers
        """ 
        with self.assertRaises(ValueError) as context:
            sum_elements([1, 2, 'a'])
        self.assertEqual(str(context.exception), "All elements in the list must be integers.")    
        

# Run the unit tests when this script is executed
if __name__ == '__main__':
    unittest.main()
