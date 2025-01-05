#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit test for title_case function.git

Module contents:
    - TestStringToTitleCase: Unit test class for the title_case function.
    
Created on 5 1 2025
@author: Nour Elhuda Haidar
"""

import unittest
from ..title_case import title_case  
class TestStringToTitleCase(unittest.TestCase):
    """ Unit test for title case function."""
    
    def test_regular_sentence(self):
        """ test for regular sentence"""
        self.assertEqual(title_case("python is awesome"), "Python Is Awesome")

    def test_empty_string(self):
        """ test for empty string"""
        self.assertEqual(title_case(""), "")

    def test_numeric_and_text(self):
        """ test for numeric and text"""
        self.assertEqual(title_case("123abc"), "123Abc")
        
    def test_invalid_input_int(self):
        """Test for invalid input (integer)."""
        with self.assertRaises(AssertionError):
            title_case(765)
    def test_invalid_input_float(self):
        """Test for invalid input (float)."""
        with self.assertRaises(AssertionError):
            title_case(7.98)
        
