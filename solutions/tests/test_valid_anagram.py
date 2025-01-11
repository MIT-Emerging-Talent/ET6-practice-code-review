import unittest
from solutions.valid_anagram import valid_anagram


class Testvalidanagram(unittest.TestCase):
    """Test cases for valid_anagram function."""

    def test_basic_anagram(self):
        """It should identify basic anagrams correctly."""
        self.assertTrue(valid_anagram("listen", "silent"))

    def test_not_anagram(self):
        """It should return False for non-anagram strings."""
        self.assertFalse(valid_anagram("hello", "world"))

    def test_same_word(self):
        """It should identify same words as anagrams."""
        self.assertTrue(valid_anagram("word", "word"))


if __name__ == "__main__":
    unittest.main()
