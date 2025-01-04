#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
a Unittest for the Convert_Decimal_to_Binary code.
Created on 01/01/2025

@author: Taher Shaban
"""

import unittest

from Convert_Decimal_To_Binary import conv_dec_bin
class TestConvertDecimalToBinary(unittest.TestCase):
    """Test the conv_dec_bin function"""
    def test_Decimal_num(self):
        """It should evaluate 6 to 110"""
        self.assertEqual(conv_dec_bin(6),"110")
    def test_non_Decimal_num(self):
        """It should raise an assertion error if the argument is not a decimal number"""
        with self.assertRaises(AssertionError):
            conv_dec_bin("Seven")
