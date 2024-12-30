#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the convert_string_to_uppercase function

Created on 29 Dec 2024
@author: Noorelsalam Almakki
"""

import unittest

from ..convert_string_to_uppercase import convert_string_to_uppercase


class TestConvertStringToUppercase(unittest.TestCase):
    """A class for testing the convert_string_to_uppercase function"""

    def test_empty_string(self):
        """Test the convert_string_to_uppercase function with an empty string"""
        self.assertEqual(convert_string_to_uppercase(""), "")

    def test_lowercase_string(self):
        """Test the convert_string_to_uppercase function with a lowercase string"""
        self.assertEqual(convert_string_to_uppercase("hello"), "HELLO")

    def test_uppercase_string(self):
        """Test the convert_string_to_uppercase function with an uppercase string"""
        self.assertEqual(convert_string_to_uppercase("WORLD"), "WORLD")
