import unittest

def count_words(text):
    """
    Counts the number of words in a given string.

    Args:
        text (str): The string to analyze.

    Returns:
        int: The number of words in the string.
    """
    words = text.split()
    return len(words)

class TestCountWords(unittest.TestCase):
    def test_empty_string(self):
        """Test with an empty string"""
        self.assertEqual(count_words(""), 0)

    def test_single_word(self):
        """Test with a single word"""
        self.assertEqual(count_words("hello"), 1)

    def test_multiple_words(self):
        """Test with multiple words"""
        self.assertEqual(count_words("Hello, world!"), 2)

    def test_extra_spaces(self):
        """Test with extra spaces"""
        self.assertEqual(count_words("   Hello   world   "), 2)

    def test_numbers_and_words(self):
        """Test with a mix of numbers and words"""
        self.assertEqual(count_words("123 hello 456 world"), 4)

    def test_special_characters(self):
        """Test with special characters"""
        self.assertEqual(count_words("!@# $%^ &*()"), 3)

if __name__ == "__main__":
    unittest.main()