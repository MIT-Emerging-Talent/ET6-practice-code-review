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

    def test_absolute_value_of_zero(self):
        """It should return 0 when the input is 0"""
        actual = absolute_value(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_absolute_value_of_positive_number(self):
        """It should return the positive value of a number"""
        actual = absolute_value(10)
        expected = 10
        self.assertEqual(actual, expected)

    def test_absolute_value_of_negative_number(self):
        """It should return the positive value of a negative number"""
        actual = absolute_value(-10)
        expected = 10
        self.assertEqual(actual, expected)

    def test_type_error_for_non_number_input(self):
        """It should raise a TypeError for non-number input"""
        with self.assertRaises(TypeError):
            absolute_value("hello")
