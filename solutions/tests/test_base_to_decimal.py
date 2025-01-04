#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for base_to_decimal function.
Includes deliberately faulty tests for debugging practice.

Test categories:
    - Edge Cases: '0b0','0o0' and '0x0'
    - Standard Cases: A collection of different base strings.
    - Defensive Tests: wrong input types, assertions.

Created on Jan 2, 2025.
Team Number: 28
Team Name: MIT Alpha
@author: AL-HASSEN SABEEH
"""

import unittest

from ..base_to_decimal import base_to_decimal


class TestbaseToDecimal(unittest.TestCase):
    """Test the base_to_decimal function"""

    # Test Edge Cases
    def test_base_0b0(self):
        """It should evaluate '0b0' to 0"""
        self.assertEqual(base_to_decimal("0b0"), 0)

    def test_base_0o0(self):
        """It should evaluate '0o0' to 0"""
        self.assertEqual(base_to_decimal("0o0"), 0)

    def test_base_0x0(self):
        """It should evaluate '0x0' to 0"""
        self.assertEqual(base_to_decimal("0x0"), 0)

    # Test Standard Cases
    def test_base_0b111(self):
        """It should evaluate '0b111' to 7"""
        self.assertEqual(base_to_decimal("0b111"), 7)

    def test_base_0o12(self):
        """It should evaluate '0o12' to 10"""
        self.assertEqual(base_to_decimal("0o12"), 10)

    def test_base_0x3ff(self):
        """It should evaluate '0x3fF' to 1023"""
        self.assertEqual(base_to_decimal("0x3fF"), 1023)

    def test_base_0b1010101010101010101010(self):
        """It should evaluate '0b1010101010101010101010' to 2796202"""
        self.assertEqual(base_to_decimal("0b1010101010101010101010"), 2796202)

    # Test Defensive Assertions
    def test_defensive_check_base_is_not_string(self):
        """it should raise an error if the input is not string"""
        with self.assertRaises(AssertionError):
            base_to_decimal(6)

    def test_defensive_check_base_is_not_empty(self):
        """it should raise an error if the sting is empty"""
        with self.assertRaises(AssertionError):
            base_to_decimal("")

    def test_defensive_check_for_string_have_invalid_digit(self):
        """it should raise an error if the input has invalid digit"""
        with self.assertRaises(AssertionError):
            base_to_decimal("11180101")

    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            base_to_decimal(None)
