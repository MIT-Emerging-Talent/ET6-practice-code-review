#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: test_mean

Description:
    This module contains the unit tests for the mean function in the solutions package.
    the function calculates the mean of a list of numbers.

Author: Mohammed Elfadil
Date: 31/12/2024
"""
import unittest
from solutions.mean import mean


class TestMean(unittest.TestCase):
    """test the mean function"""

    def test_positive_numbers(self):
        """It should evaluate 3.0"""
        actual = mean([1, 2, 3, 4, 5])
        expected = 3.0
        self.assertEqual(actual, expected)

    def test_positive_numbers2(self):
        """It should evaluate 30.0"""
        actual = mean([10, 20, 30, 40, 50])
        expected = 30.0
        self.assertEqual(actual, expected)

    def test_zeros(self):
        """It should evaluate 0.0"""
        actual = mean([0, 0, 0, 0, 0])
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_single_input(self):
        """It should evaluate 1.0"""
        actual = mean([1])
        expected = 1.0
        self.assertEqual(actual, expected)

    def test_integer(self):
        """It should evaluate invalid input"""
        actual = mean(1)
        expected = "invalid input"
        self.assertEqual(actual, expected)

    def test_negatives(self):
        """It should evaluate -4.0"""
        actual = mean([-2, -4, -6])
        expected = -4.0
        self.assertEqual(actual, expected)

    def test_floats(self):
        """It should evaluate 2.5"""
        actual = mean([1.5, 2.5, 3.5])
        expected = 2.5
        self.assertEqual(actual, expected)

    def test_string(self):
        """It should evaluate inavlid input"""
        actual = mean("2 4 6")
        expected = "invalid input"
        self.assertEqual(actual, expected)
