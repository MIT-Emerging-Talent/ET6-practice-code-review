#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Mohammed Elfadil
"""
import unittest

from solutions.IsPrime import IsPrime


class TestIsPrime(unittest.TestCase):
    """test the IsPrime function"""

    def test_0(self):
        """It should evaluate not prime"""
        actual = IsPrime(0)
        expected = "not prime"
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should evaluate not prime"""
        actual = IsPrime(1)
        expected = "not prime"
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = IsPrime(2)
        expected = "prime"
        self.assertEqual(actual, expected)

    def test_4(self):
        """its should evaluate not prime"""
        actual = IsPrime(4)
        expected = "not prime"
        self.assertEqual(actual, expected)

    def test_7(self):
        """It should evaluate prime"""
        actual = IsPrime(7)
        expected = "prime"
        self.assertEqual(actual, expected)

    def test_9(self):
        """It should evaluate not prime"""
        actual = IsPrime(9)
        expected = "not prime"
        self.assertEqual(actual, expected)

    def test_11(self):
        """It should evaluate prime"""
        actual = IsPrime(11)
        expected = "prime"
        self.assertEqual(actual, expected)

    def test_13(self):
        """It should evaluate prime"""
        actual = IsPrime(13)
        expected = "prime"
        self.assertEqual(actual, expected)

    def test_negative(self):
        """It should evaluate not prime"""
        actual = IsPrime(-1)
        expected = "not prime"
        self.assertEqual(actual, expected)

    def test_not_integer(self):
        """It should evaluate not prime"""
        actual = IsPrime(1.5)
        expected = "invalid input"
        self.assertEqual(actual, expected)
if __name__ == "__main__":
    unittest.main()
