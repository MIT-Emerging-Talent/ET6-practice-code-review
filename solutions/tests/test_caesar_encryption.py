import unittest

from ..caesar_encryption import caesar_encryption


class TestCaesarEncryption(unittest.TestCase):
    """Test if the encryption is correct using caesar encryption."""

    # Regular test cases
    def test_non_alpha_characters(self):
        """it should shift alphabetic characters, while non-alphabetic characters remain unchanged."""
        actual = caesar_encryption("Hello, World!", 3)
        expected = "Khoor, Zruog!"
        self.assertEqual(actual, expected)

    def test_negative_shift(self):
        """it should correctly shift characters backward in the alphabet given a negative shift."""
        actual = caesar_encryption("ABC", -1)
        expected = "ZAB"
        self.assertEqual(actual, expected)

    def test_no_shift(self):
        """it should leave the input string unchanged."""
        actual = caesar_encryption("abc", 0)
        expected = "abc"
        self.assertEqual(actual, expected)

    def test_numeric_and_special_characters(self):
        """it should leave numbers and special characters while alphabetic characters are shifted."""
        actual = caesar_encryption("Python 3.9!", 5)
        expected = "Udymts 3.9!"
        self.assertEqual(actual, expected)

    # Edge cases
    def test_empty_string(self):
        """
        Test that an empty string returns an empty string.
        """
        actual = caesar_encryption("", 5)
        expected = ""
        self.assertEqual(actual, expected)

    def test_single_character_uppercase(self):
        """
        Test shifting a single uppercase character.
        """
        actual = caesar_encryption("A", 1)
        expected = "B"
        self.assertEqual(actual, expected)

    def test_single_character_lowercase(self):
        """
        Test shifting a single lowercase character.
        """
        actual = caesar_encryption("a", 1)
        expected = "b"
        self.assertEqual(actual, expected)

    def test_shift_wraparound(self):
        """ it should  wrap around correctly (Z -> B)(x -> a)."""
        actual = caesar_encryption("Zx", 2)
        expected = "Ba"
        self.assertEqual(actual, expected)

    # Defensive Tests
    def test_invalid_text_type(self):
        """it should raise an AssertionError if the text parameter is not a string."""
        with self.assertRaises(AssertionError):
            caesar_encryption(123, 3)

    def test_invalid_shift_type(self):
        """it should raise an AssertionError if the shift parameter is not an integer."""
        with self.assertRaises(AssertionError):
            caesar_encryption("Hello", "three")
