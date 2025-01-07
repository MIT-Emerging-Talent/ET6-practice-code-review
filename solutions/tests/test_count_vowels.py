import unittest
from vowel_counter import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_only_vowels(self):
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_mixed_characters(self):
        self.assertEqual(count_vowels("Hello, World!"), 3)

    def test_numbers_and_symbols(self):
        self.assertEqual(count_vowels("12345!@#$%"), 0)

if __name__ == "__main__":
    unittest.main()
