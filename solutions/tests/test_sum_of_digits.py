#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the sum_of_digits function

Created on 25 Dec 2024
@author: Noorelsalam Almakki
"""

import unittest
from ..sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
  """A class for testing the sum_of_digits function"""
  
  def test_2_digits(self):
    """Test the sum_of_digits function with a 2-digit number"""
    self.assertEqual(sum_of_digits(12), 3)

  def test_6_digits(self):
    """Test the sum_of_digits function with a 6-digit number"""
    self.assertEqual(sum_of_digits(123456), 21)
