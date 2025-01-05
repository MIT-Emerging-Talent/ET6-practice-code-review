import unittest

from ..check_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Test the is_palindrome function"""

    def test_valid_palindrome(self):
        """Test with valid palindromes"""
        self.assertTrue(is_palindrome("kayak"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("level"))

    def test_invalid_palindrome(self):
        """Test with non-palindromes"""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        """Test with a single character"""
        self.assertTrue(is_palindrome("a"))

    def test_type_error(self):
        """Test for TypeError with non-string input"""
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome(None)

    def test_case_insensitive(self):
        """Test case-insensitivity"""
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("Madam"))

    def test_spaces_ignored(self):
        """Test handling of spaces"""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
