#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for conversion from number to word.

This module contains unittest test and edge cases for the number_to_word.

Created on 03 01 2025
@author: Terry Aziaba
"""

import unittest

from ..number_to_word import number_to_word


class TestNumberToWord(unittest.TestCase):
    """Unit tests for the number_to_word function."""

    def test_zero(self):
        """Test the input 0."""
        self.assertEqual(number_to_word(0), "zero")

    def test_one(self):
        """Test the input 1."""
        self.assertEqual(number_to_word(1), "one")

    def test_two(self):
        """Test the input 2."""
        self.assertEqual(number_to_word(2), "two")

    def test_three(self):
        """Test the input 3."""
        self.assertEqual(number_to_word(3), "three")

    def test_four(self):
        """Test the input 4."""
        self.assertEqual(number_to_word(4), "four")

    def test_five(self):
        """Test the input 5."""
        self.assertEqual(number_to_word(5), "five")

    def test_six(self):
        """Test the input 6."""
        self.assertEqual(number_to_word(6), "six")

    def test_seven(self):
        """Test the input 7."""
        self.assertEqual(number_to_word(7), "seven")

    def test_eight(self):
        """Test the input 8."""
        self.assertEqual(number_to_word(8), "eight")

    def test_nine(self):
        """Test the input 9."""
        self.assertEqual(number_to_word(9), "nine")

    def test_invalid_input_ten(self):
        """Test the input 10 (two-digit number)."""
        with self.assertRaises(ValueError):
            number_to_word(10)

    def test_invalid_input_negative(self):
        """Test the input -1 (negative number)."""
        with self.assertRaises(ValueError):
            number_to_word(-1)

    def test_invalid_input_large_number(self):
        """Test the input 100 (large number)."""
        with self.assertRaises(ValueError):
            number_to_word(100)

    def test_invalid_input_float(self):
        """Test the input 3.5 (float)."""
        with self.assertRaises(ValueError):
            number_to_word(3.5)

    def test_invalid_input_string(self):
        """Test the input "three" (string)."""
        with self.assertRaises(ValueError):
            number_to_word("three")

    def test_invalid_input_none(self):
        """Test the input None."""
        with self.assertRaises(ValueError):
            number_to_word(None)

    def test_edge_case_zero(self):
        """Test the lower boundary input 0."""
        self.assertEqual(number_to_word(0), "zero")

    def test_edge_case_nine(self):
        """Test the upper boundary input 9."""
        self.assertEqual(number_to_word(9), "nine")
