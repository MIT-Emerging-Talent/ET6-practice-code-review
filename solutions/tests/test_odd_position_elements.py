#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
Created on 12.26.2024

@author: Anna Shumylina

"""

import unittest

from ..odd_position_elements import odd_position_elements


class TestOddPositionElements(unittest.TestCase):
    """Test module for odd_position_elements function"""

    # Empty string test case
    def test_empty_string(self):
        self.assertEqual(odd_position_elements(""), "")

    # Numerical string test case
    def test_numerical(self):
        self.assertEqual(odd_position_elements("123456789"), "13579")

    # Basic string test case
    def test_basic(self):
        self.assertEqual(odd_position_elements("Hello World!"), "HloWrd")

    # Special characters test case
    def test_long_string(self):
        self.assertEqual(
            odd_position_elements(
                "Use of the word //string, to mean any items arranged in a *line*"
            ),
            "Ueo h od/srn,t enayiesarne na*ie",
        )
