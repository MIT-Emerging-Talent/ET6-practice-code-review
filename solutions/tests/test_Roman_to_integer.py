#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for Roman to integer function.
"""

import unittest


class TestRomanToInteger(unittest.TestCase):
    """
    Unit test class to verify the correctness of the romanToInteger function.
    """


def test_case_0(self):
    """Test conversion of single Roman number to 10"""
    self.assertEqual(self.romanToInteger("X"), 10)
