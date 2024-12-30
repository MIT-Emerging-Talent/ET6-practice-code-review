#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A test module for the binary_search function in solutions/binary_search.py

Test categories:
    - Standard test cases: Test cases that test the function with standard input.
    - Edge test cases: Test cases that test the function with edge cases.
    - Defensive test cases: Test cases that test the function with invalid input.
    
Created on 2024-12-27
Author: Awaab98"""

import unittest
from solutions.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    """A class for testing the binary_search function."""
    
    # Standard test cases
    def test_find_middle_element(self):
        """It should return the index of the middle element."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        
    def test_find_last_element(self):
        """It should return the index of the last element."""
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 50), 4)

    def test_find_first_element(self):
        """It should return the index of the first element."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_find_float(self):
        """It should return the index of the float element."""
        self.assertEqual(binary_search([0.1, 0.2, 0.3, 0.4, 0.5], 0.4), 3)

    def test_find_string(self):
        """It should return the index of the string element."""
        self.assertEqual(binary_search(["apple", "banana", "cherry"], "banana"), 1)
        
    # Edge test cases
    def test_single_element_list(self):
        """Test finding the element in a single-element list."""
        self.assertEqual(binary_search([42], 42), 0)

    def test_smallest_element_in_list(self):
        """Test finding the smallest element in the list."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_largest_element_in_list(self):
        """Test finding the largest element in the list."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)
