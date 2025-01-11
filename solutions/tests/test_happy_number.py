#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the happy_number function
"""

import unittest

from ..happy_number import happy_number


class TestHappyNumber(unittest.TestCase):
    """Unit tests for the happy_number function"""

    # Standard Cases
    def test_happy_number_is_true(self):
        """Test that a happy number returns True"""
        self.assertEqual(happy_number(19), True)

    def test_unhappy_number_is_false(self):
        """Test that a unhappy number returns False"""
        self.assertEqual(happy_number(2), False)

    def test_happy_number_one(self):
        """Test that the smallest happy number returns True"""
        self.assertEqual(happy_number(1), True)

    # Boundary Cases
    def test_smallest_unhappy_number(self):
        """Test that the smallest unhappy number returns False"""
        self.assertEqual(happy_number(4), False)

    def test_large_happy_number(self):
        """Test that a large happy number returns True"""
        self.assertEqual(happy_number(998), True)

    def test_large_unhappy_number(self):
        """Test that a large unhappy number returns False"""
        self.assertEqual(happy_number(987654321), False)

    # Defensive Cases
    def test_negative_number(self):
        """Test that a negative number raises an AssertionError"""
        with self.assertRaises(AssertionError):
            happy_number(-5)

    def test_zero_input(self):
        """Test that zero raises an AssertionError"""
        with self.assertRaises(AssertionError):
            happy_number(0)

    def test_string_input(self):
        """Test that a non-integer input raises an AssertionError"""
        with self.assertRaises(AssertionError):
            happy_number("33")

    def test_float_input(self):
        """Test that a float input raises an AssertionError"""
        with self.assertRaises(AssertionError):
            happy_number(19.0)


if __name__ == "__main__":
    unittest.main()
