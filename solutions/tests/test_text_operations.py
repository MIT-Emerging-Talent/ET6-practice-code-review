"""
Test module for the text_processor module.

Created on: 04/01/2025
@author: Your Name
"""

import unittest

from text_processor import count_vowels, reverse_text, to_uppercase


class TestTextProcessor(unittest.TestCase):
    """
    Unit tests for the text_processor functions.
    """

    def test_count_vowels(self):
        """Test the count_vowels function."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_reverse_text(self):
        """Test the reverse_text function."""
        self.assertEqual(reverse_text("hello"), "olleh")
        self.assertEqual(reverse_text("Python"), "nohtyP")
        self.assertEqual(reverse_text("12345"), "54321")
        self.assertEqual(
            reverse_text(""), ""
        )  # Empty string should return empty string.

    def test_to_uppercase(self):
        """Test the to_uppercase function."""
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase("Python"), "PYTHON")
        self.assertEqual(to_uppercase("12345"), "12345")  # Numbers should stay the same
        self.assertEqual(
            to_uppercase("!@#$"), "!@#$"
        )  # Special characters should stay the same


if __name__ == "__main__":
    unittest.main()
