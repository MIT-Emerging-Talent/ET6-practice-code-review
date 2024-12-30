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
    def test_find_middle_element_in_standard_list(self):
        """It should return the index of the middle element in a standard list."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
