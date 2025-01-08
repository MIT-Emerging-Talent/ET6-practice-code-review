#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for string

Module contents:
     to calculate the string of the list

Created on 03-01-2025
@author:Samir Ahmed Shaifta
"""

import unittest

from ..challenge_5 import is_in_list


class TeststringFunction(unittest.TestCase):
    """Unit tests for the is_in_list function."""

    def test_is_in_list_with_apple(self):
        """It should return True when the input is 'apple'."""
        actual = is_in_list("apple")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_in_list_with_grape(self):
        """It should return True when the input is 'grape'."""
        actual = is_in_list("grape")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_in_list_with_mango(self):
        """It should return False when the input is 'mango'."""
        actual = is_in_list("mango")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_in_list_with_empty_string(self):
        """It should return False when the input is an empty string."""
        actual = is_in_list("")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_in_list_with_capitalized_word(self):
        """It should return False when the input is a capitalized word like 'Apple'."""
        actual = is_in_list("Apple")
        expected = False
        self.assertEqual(actual, expected)

        if __name__ == "__main__":
            unittest.main()
