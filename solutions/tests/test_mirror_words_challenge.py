"""
Test module for mirror_words function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: Sentences with regular words and punctuation.
    - Edge cases: Empty strings, single words, or sentences with special characters.
    - Defensive cases: Invalid inputs (e.g., non-string types).

Created on 2025-01-05
Author: Aseel AbuKmail
"""

import sys
import os
import unittest
from solutions.mirror_words_challenge import mirror_words

# Add the directory containing mirror_words_challenge.py to the module search path
# This is temporarily needed to ensure that the 'mirror_words_challenge' module can be imported 
# for testing purposes while the project structure is being developed.
sys.path.append(
    "C:/Users/pc/.vscode/VS code Files/MIT - Project/ET6-foundations-group-17-main/solutions"
)

# Add the project root directory to sys.path
# Ensures that the root project directory is included in the module search path for importing 
# other modules or testing purposes.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

class TestMirrorWords(unittest.TestCase):
    """Tests for mirror_words function"""

    # Standard test cases
    def test_mirror_words_regular_sentence(self):
        """It should mirror each word in a regular sentence while maintaining word order"""
        actual = mirror_words("Hello world!")
        expected = "olleH dlrow!"
        self.assertEqual(actual, expected)

    def test_mirror_words_single_word(self):
        """It should reverse a single word in a sentence"""
        actual = mirror_words("Python")
        expected = "nohtyP"
        self.assertEqual(actual, expected)

    def test_mirror_words_with_punctuation(self):
        """It should handle words with punctuation marks"""
        actual = mirror_words("Python is fun")
        expected = "nohtyP si nuf"
        self.assertEqual(actual, expected)

    # Edge cases
    def test_empty_sentence(self):
        """It should return an empty string for an empty sentence"""
        actual = mirror_words("")
        expected = ""
        self.assertEqual(actual, expected)

    def test_single_character(self):
        """It should return the single character unchanged"""
        actual = mirror_words("A")
        expected = "A"
        self.assertEqual(actual, expected)

    def test_sentence_with_special_characters(self):
        """It should handle sentences with special characters correctly"""
        actual = mirror_words("!@# $%^ &*()")
        expected = "!@# $%^ &*()"  # Special characters remain intact
        self.assertEqual(actual, expected)

    # Defensive test cases
    def test_non_string_input(self):
        """It should raise TypeError for non-string input"""
        with self.assertRaises(TypeError):
            mirror_words(12345)

    def test_input_with_mixed_data_types(self):
        """It should raise TypeError for input with mixed types"""
        with self.assertRaises(TypeError):
            mirror_words(["Hello", "world!"])


if __name__ == "__main__":
    unittest.main()
