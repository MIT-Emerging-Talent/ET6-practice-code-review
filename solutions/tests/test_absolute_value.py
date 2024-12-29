#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole
"""

import unittest

from ..absolute_value import absolute_value


class TestAbsoluteValue(unittest.TestCase):
    """Test the absolute_value function"""

    def test_0(self):
        """It should return 0 when the input is 0"""
        actual = absolute_value(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should return 10 when the input is 10"""
        actual = absolute_value(10)
        expected = 10
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should return 10 when the input is -10"""
        actual = absolute_value(-10)
        expected = 10
        self.assertEqual(actual, expected)
