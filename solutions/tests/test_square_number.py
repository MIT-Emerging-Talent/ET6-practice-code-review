#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_square_number.py
Unit tests for the square_number module.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from solutions.square_number import square_number


class TestSquareNumber(unittest.TestCase):
    """
    Unit tests for the square_number function.
    """

    def test_positive_integer(self):
        """
        Test squaring a positive integer.
        """
        self.assertEqual(square_number(5), 25)

    def test_negative_integer(self):
        """
        Test squaring a negative integer.
        """
        self.assertEqual(square_number(-3), 9)

    def test_positive_float(self):
        """
        Test squaring a positive float.
        """
        self.assertEqual(square_number(2.5), 6.25)

    def test_zero(self):
        """
        Test squaring zero.
        """
        self.assertEqual(square_number(0), 0)

    def test_invalid_input(self):
        """
        Test handling of invalid input (non-number).
        """
        with self.assertRaises(TypeError):
            square_number("abc")


if __name__ == "__main__":
    unittest.main()
