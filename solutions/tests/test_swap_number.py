#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for swap_numbers function

Test categories:
 - Standard cases: typical inputs
 - Edge cases: extreme inputs and boundaries
 - Defensive tests: wrong input types, assertions

Created on 11/1/2025
@author: Majd Abualsoud
Group: ET foundations group 16
"""

import unittest

from ..swap_number import swap_numbers


"""Test suite for the swap_numbers function"""


# Standard cases
def test_swap_two_positive_numbers(self):
    """It should swap two positive numbers"""
    self.assertEqual(swap_numbers(1, 2), (2, 1))


def test_swap_two_negative_numbers(self):
    """It should swap two negative numbers"""
    self.assertEqual(swap_numbers(-1, -2), (-2, -1))


def test_swap_a_positive_and_a_negative_number(self):
    """It should swap a positive and a negative number"""
    self.assertEqual(swap_numbers(1, -2), (-2, 1))


def test_swap_zero_and_a_number(self):
    """It should swap zero with another number"""
    self.assertEqual(swap_numbers(0, 5), (5, 0))


# Edge cases
def test_swap_large_numbers(self):
    """It should swap large numbers correctly"""
    self.assertEqual(swap_numbers(10**6, 10**9), (10**9, 10**6))


def test_swap_float_numbers(self):
    """It should swap float numbers correctly"""
    self.assertEqual(swap_numbers(1.5, 2.5), (2.5, 1.5))


# Defensive tests
def test_non_numeric_input_a(self):
    """It should raise AssertionError if the first input is not numeric"""
    with self.assertRaises(AssertionError):
        swap_numbers("1", 2)


def test_non_numeric_input_b(self):
    """It should raise AssertionError if the second input is not numeric"""
    with self.assertRaises(AssertionError):
        swap_numbers(1, "2")


def test_non_numeric_input_both(self):
    """It should raise AssertionError if both inputs are not numeric"""
    with self.assertRaises(AssertionError):
        swap_numbers("1", "2")


if __name__ == "__main__":
    unittest.main()
