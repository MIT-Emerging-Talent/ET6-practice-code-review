#! usr/bin/env python3
# -*- coding: utf-8 -*-

"""  
Test for subtraction of one number from the other.

Created on 31.12.2024

@author: 


"""

import unittest
from solutions.subtract import subtract

class TestSubtractFunction(unittest.TestCase):
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers """
        self.assertEqual(subtract(7,4), 3)
        
    def test_subtract_negative_numbers(self):
        """Test subtract two negative numbers"""
        self.assertEqual (subtract(-5, -5), 0)
        
    def test_subtract_mixed_sign_numbers(self):
        """This test should subtract the negative second 
        number from the first number"""
        self.assertEqual (subtract(7, -5), 12)

    def test_not_numbers(self):
        """This should raise an AssertionError for not numbers input"""
        self.assertEqual (subtract(-5, -5), 0)
    
    
if __name__ == "__main__":
    unittest.main()
