"""
Test module for is_palindrome function.
Tests standard cases, edge cases and input validation.
"""

import unittest
from ..is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Test suite for is_palindrome function."""

    def test_palindrome_madam(self):
        """Tests 'madam' is identified as palindrome."""
        self.assertTrue(is_palindrome("madam"))

    def test_palindrome_racecar(self):
        """Tests 'racecar' is identified as palindrome."""
        self.assertTrue(is_palindrome("racecar"))

    def test_palindrome_numbers(self):
        """Tests numeric palindrome."""
        self.assertTrue(is_palindrome("12321"))

    def test_non_palindrome_hello(self):
        """Tests 'hello' is identified as non-palindrome."""
        self.assertFalse(is_palindrome("hello"))

    def test_non_palindrome_python(self):
        """Tests 'python' is identified as non-palindrome."""
        self.assertFalse(is_palindrome("python"))

    def test_case_sensitive_Madam(self):
        """Tests case is ignored."""
        self.assertTrue(is_palindrome("Madam"))

    def test_spaces_and_punctuation(self):
        """Tests spaces and punctuation are ignored."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_empty_string(self):
        """Tests empty string is palindrome."""
        self.assertTrue(is_palindrome(""))

    def test_single_char(self):
        """Tests single character is palindrome."""
        self.assertTrue(is_palindrome("a"))

    def test_spaces_only(self):
        """Tests string with only spaces is palindrome."""
        self.assertTrue(is_palindrome("   "))

    def test_invalid_input_none(self):
        """Tests None input raises AssertionError."""
        with self.assertRaises(AssertionError):
            is_palindrome(None)

    def test_invalid_input_number(self):
        """Tests numeric input raises AssertionError."""
        with self.assertRaises(AssertionError):
            is_palindrome(123)


if __name__ == "__main__":
    unittest.main()
