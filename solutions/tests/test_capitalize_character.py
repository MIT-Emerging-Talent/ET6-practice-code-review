"""

Unit test for Capitalize character Function 

Created on 12/28/2024

Author : Khadija Al Ramlawi
"""

import unittest
from solutions.capitalize_character import capitalize_character


class TestCapitalizeCharacter(unittest.TestCase):
    def test_single_occurrence(self):
        self.assertEqual(capitalize_character("hello", "h"), "Hello")

    def test_multiple_occurrences(self):
        # The character will be capitalized twice
        self.assertEqual(capitalize_character("hello", "l"), "heLLo")

    def test_no_occurrence(self):
        # No character will be capitalized
        self.assertEqual(capitalize_character("hello", "z"), "hello")

    def test_empty_word(self):
        # Empty entry, No character will be capitalized
        self.assertEqual(capitalize_character("", "a"), "")

    def test_single_character_word(self):
        self.assertEqual(capitalize_character("a", "a"), "A")
        self.assertEqual(capitalize_character("b", "a"), "b")

    def test_special_characters(self):
        self.assertEqual(capitalize_character("he!lo!", "!"), "he!lo!")

    def test_numerical_characters(self):
        self.assertEqual(capitalize_character("h3ll0", "l"), "h3LL0")

    def test_invalid_input_word(self):
        with self.assertRaises(AssertionError):
            capitalize_character(123, "a")

    def test_invalid_input_char(self):
        with self.assertRaises(AssertionError):
            capitalize_character("hello", 123)

    def test_multiple_characters_as_input(self):
        with self.assertRaises(AssertionError):
            capitalize_character("hello", "ll")
