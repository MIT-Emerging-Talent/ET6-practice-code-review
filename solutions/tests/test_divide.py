#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 05.01.2025

@author: Zephaniah Okoye
"""

import unittest

# --- imports & test class before documenting and testing ---

# from ..mystery_0 import mystery_0

# class TestMystery0(unittest.TestCase):

# --- imports & test class after documenting and testing ---

from ..divide import divide

class TestDivide(unittest.TestCase):
    """ Test for testing our divide function"""
    
    def test_divide_integers(self):
        """It should produce the accurate results of a division operation for two integer inputs"""
        
        actual = divide(10, 2) # Calling function with test arguments
        expected = 5.0 # Expected result
        self.assertEqual(actual, expected)
        
        actual = divide(9, 3) # Calling function with test arguments
        expected = 3.0 # Expected result
        self.assertEqual(actual, expected)
        
        actual = divide(0, 1) # Calling function with test arguments
        expected = 0.0 # Expected result
        self.assertEqual(actual, expected)

    def test_divide_floats(self):
        """It should produce the accurate results of a division operation for two float inputs"""
        
        actual = divide(10.5, 2.5) # Calling function with test arguments
        expected = 4.2 # Expected result
        self.assertAlmostEqual(actual, expected)
        
        actual = divide(-7.0, 2.0) # Calling function with test arguments
        expected = -3.5 # Expected result
        self.assertAlmostEqual(actual, expected)

    def test_divide_zero(self):
        """It should show a ZeroDivisionError whenever the denominator input is zero"""
        
        with self.assertRaises(ZeroDivisionError) as context:
            divide(7, 0) # Calling function with test arguments
        expected = "Cannot divide by zero" # Expected result
        self.assertTrue(expected in str(context.exception))

    def test_divide_type_error(self):
     """It should show a TypeError when either argument is not a number"""
    
     with self.assertRaises(TypeError) as context:
        divide("10", 2)  # Calling function with test arguments
     expected = "Both arguments must be numbers"  # Expected result
     self.assertTrue(expected in str(context.exception))
    
     with self.assertRaises(TypeError) as context:
        divide(10, "2")  # Calling function with test arguments
     expected = "unsupported operand type(s) for /: 'int' and 'str'"  # Updated expected result
     self.assertTrue(expected in str(context.exception))
    
     with self.assertRaises(TypeError) as context:
        divide("10", "2")  # Calling function with test arguments
     expected = "Both arguments must be numbers"  # Expected result
     self.assertTrue(expected in str(context.exception))
 
 
#Additional test method
if __name__ == "__main__":
    unittest.main()
