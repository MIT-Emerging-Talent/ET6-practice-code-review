#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for binary_to_decimal function.
Includes deliberately faulty tests for debugging practice.

Test categories: 
    - Edge Cases: '0', '1' and a large string.
    - Standard Cases: A collection of different binary strings.
    - Defensive Tests: wrong input types, assertions.

Created on Dec 28, 2024.

@author: AL-HASSEN SABEEH
"""
import unittest

from ..binary_to_decimal import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):
    """Test the binary_to_decimal function"""

    #Test Edge Cases
    def test_binary_0(self):
        """It should evaluate '0' to 0"""
        self.assertEqual(binary_to_decimal('0'), 0)

    def test_binary_1(self):
        """It should evaluate '1' to 1"""
        self.assertEqual(binary_to_decimal('1'), 1)

    #Test Standard Cases
    def test_binary_10(self):
        """It should evaluate '10' to 2"""
        self.assertEqual(binary_to_decimal('10'), 2)

    def test_binary_111(self):
        """It should evaluate '111' to 7"""
        self.assertEqual(binary_to_decimal('111'), 7)

    def test_binary_1010(self):
        """It should evaluate '1010' to 10"""
        self.assertEqual(binary_to_decimal('1010'), 10)

    def test_binary_1111111111(self):
        """It should evaluate '1111111111' to 1023"""
        self.assertEqual(binary_to_decimal('1111111111'), 1023)

    def test_binary_1010101010101010101010(self):
        """It should evaluate '1010101010101010101010' to 1023"""
        self.assertEqual(binary_to_decimal('1010101010101010101010'), 2796202)

    #Test Defensive Assertions
    def test_defensive_check_binary_is_not_string(self):
        """it should raise an error if the input is not string"""
        with self.assertRaises(AssertionError):
            binary_to_decimal(6)

    def test_defensive_check_for_string_not_0_or_1(self):
        """it should raise an error if the input has char not 0 or 1"""
        with self.assertRaises(AssertionError):
            binary_to_decimal('11180101')

    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            binary_to_decimal(None)
