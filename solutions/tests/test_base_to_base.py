#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for base_to_base function.
Includes deliberately faulty tests for debugging practice.

Test categories:
    - Edge Cases: '0b0','0o0' and '0x0' and 0
    - Standard Cases: A collection of different base strings.
    - Defensive Tests: wrong input types, assertions.

Created on Jan 4, 2025.
Team Number: 28
Team Name: MIT Alpha
@author: AL-HASSEN SABEEH
"""

import unittest

from ..base_to_base import base_to_base


class TestBaseToBase(unittest.TestCase):
    """Test the base_to_base function"""

    # Test Edge Cases
    def test_base_0b0(self):
        """It should evaluate '0b0' to 0"""
        self.assertEqual(base_to_base("0b0", 10), 0)

    def test_base_0o0(self):
        """It should evaluate '0o0' to 0"""
        self.assertEqual(base_to_base("0o0", 16), "0x0")

    def test_base_0x0(self):
        """It should evaluate '0x0' to 0"""
        self.assertEqual(base_to_base(0, 2), "0b0")

    # Test Standard Cases
    def test_base_0b111(self):
        """It should evaluate '0b111' to '0x7'"""
        self.assertEqual(base_to_base("0b111", 16), "0x7")

    def test_convert_0o12_to_0b1010(self):
        """It should evaluate '0o12' to 10"""
        self.assertEqual(base_to_base("0o12", 2), "0b1010")

    def test_convert_0o12_to_0xc(self):
        """It should evaluate '0o12' to 10"""
        self.assertEqual(base_to_base("0o12", 16), "0xa")

    def test_convert_0b101_to_5(self):
        """It should evaluate '0o12' to 10"""
        self.assertEqual(base_to_base("0b101", 10), 5)

    def test_convert_0o17_to_15(self):
        """It should evaluate '0o12' to 10"""
        self.assertEqual(base_to_base("0o17", 10), 15)

    def test_convert_0x1a_to_26(self):
        """It should evaluate '0o12' to 10"""
        self.assertEqual(base_to_base("0x1a", 10), 26)

    def test_convert_5_to_0b101(self):
        """It should evaluate 5 to '0b101'"""
        self.assertEqual(base_to_base(5, 2), "0b101")

    def test_convert_15_to_0o17(self):
        """It should evaluate 15 to '0o17'"""
        self.assertEqual(base_to_base(15, 8), "0o17")

    def test_convert_26_to_0x1a(self):
        """It should evaluate 26 to '0x1a'"""
        self.assertEqual(base_to_base(26, 16), "0x1a")

    def test_convert_0b101_to_0x5(self):
        """It should evaluate '0b101' to '0x5'"""
        self.assertEqual(base_to_base("0b101", 16), "0x5")

    def test_convert_0o17_to_0b1111(self):
        """It should evaluate '0o17' to '0b1111'"""
        self.assertEqual(base_to_base("0o17", 2), "0b1111")

    def test_convert_0o17_to_0xf(self):
        """It should evaluate '0o17' to '0xf'"""
        self.assertEqual(base_to_base("0o17", 16), "0xf")

    def test_convert_0x1a_to_0o32(self):
        """It should evaluate '0x1A' to '0o32'"""
        self.assertEqual(base_to_base("0x1A", 8), "0o32")

    # Test Defensive Assertions
    def test_defensive_check_base_is_not_string_or_int(self):
        """it should raise an error if the input is not string"""
        with self.assertRaises(AssertionError):
            base_to_base(3.5, 2)

    def test_defensive_check_base_is_not_empty(self):
        """it should raise an error if the sting is empty"""
        with self.assertRaises(AssertionError):
            base_to_base("", 10)

    def test_defensive_check_for_string_have_invalid_digit(self):
        """it should raise an error if the input has invalid digit"""
        with self.assertRaises(AssertionError):
            base_to_base("11180101", 10)

    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            base_to_base(None, None)
