#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
a Unittest for the Convert_Binary_to_Decimal code.
Created on 01/01/2025

@author: Taher Shaban
"""

import unittest

from Convert_Binary_To_Decimal import conv_bin_dec
class TestConvertBinaryToDecimal(unittest.TestCase):
    """Test the conv_bin_dec function"""
    def test_binary_num(self):
        """It should evaluate 00000110 to 6"""
        actual = conv_bin_dec("00000110") # call function with test arguments
        expected = 6 # hand-write the expected return value
        self.assertEqual(actual, expected)
    
    def test_non_binary_num(self):
        """It should raise an assertion error if the argument is not a binary number"""
        with self.assertRaises(AssertionError):
            conv_bin_dec("001r001")
            
    def test_binary_num_with_space(self):
        """It should evaluate 00 00 01 10 to 6"""
        self.assertEqual( conv_bin_dec("00 00 01 10"), 6)
