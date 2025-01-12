
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for character counting functionality.

Created on 2025-01-12

@author: Karina
"""

import unittest
from solutions.count_characters import count_characters

class TestCountCharacters(unittest.TestCase):
    """Test the count_characters function"""

    def test_empty_string(self):
        """Test empty string returns empty dictionary"""
        self.assertEqual(count_characters(""), {})

    def test_single_character(self):
        """Test string with single character"""
        self.assertEqual(count_characters("a"), {"a": 1})

    def test_repeated_characters(self):
        """Test string with repeated characters"""
        self.assertEqual(count_characters("aaa"), {"a": 3})

    def test_different_characters(self):
        """Test string with different characters"""
        self.assertEqual(count_characters("abc"), {"a": 1, "b": 1, "c": 1})

    def test_with_spaces(self):
        """Test string containing spaces"""
        self.assertEqual(count_characters("a b c"), {"a": 1, "b": 1, "c": 1, " ": 2})

    def test_case_sensitivity(self):
        """Test case sensitivity"""
        self.assertEqual(count_characters("aA"), {"a": 1, "A": 1})

    def test_special_characters(self):
        """Test string with special characters"""
        self.assertEqual(count_characters("a!@#"), {"a": 1, "!": 1, "@": 1, "#": 1})

    def test_numbers(self):
        """Test string with numbers"""
        self.assertEqual(count_characters("a1b2"), {"a": 1, "1": 1, "b": 1, "2": 1})

    def test_complex_string(self):
        """Test complex string with multiple character types"""
        self.assertEqual(
            count_characters("Hello, World!"),
            {
                "H": 1,
                "e": 1,
                "l": 3,
                "o": 2,
                ",": 1,
                " ": 1,
                "W": 1,
                "r": 1,
                "d": 1,
                "!": 1,
            },
        )

    def test_invalid_input(self):
        """Test that non-string input raises AssertionError"""
        with self.assertRaises(AssertionError):
            count_characters(123)


if __name__ == "__main__":
    unittest.main()
