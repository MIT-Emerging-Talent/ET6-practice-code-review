#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Monday/30/December/2024
@author:Mayar Ali
"""
import unittest

#---imports & test class before documenting and testing---
# from ..arithmetic_sequence import arithmetic_sequence
# class TestArithmeticSequence(unittest.TestCase):
#---imports & test class after documenting and testing---

from ..arithmetic_sequence import arithmetic_sequence

class TestArithmeticSequence(unittest.TestCase):
    """Test the arithmetic_sequence function"""
 
    def test_0(self):
        "It should evaluate 0 to []"
        self.assertEqual(arithmetic_sequence(0), [])

    def test_1(self):
        "Should evaluate 1 to [0]"
        self.assertEqual(arithmetic_sequence(1), [1])

    def test_2(self):
        "Should evaluate 2 to [0,1]"
        self.assertEqual(arithmetic_sequence(2) ,[0,1])

    def test_3(self):
        "Should evaluate 3 to [0, 1, 5]"
        self.assertEqual(arithmetic_sequence(3) ,[0, 1, 4])

    
