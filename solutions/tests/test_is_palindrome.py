import unittest
from solutions.is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Test the is_palindrome function"""

    def test_empty_string(self):
        """It should return True for an empty string"""
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        """It should return True for a single character"""
        self.assertTrue(is_palindrome("a"))

    def test_palindrome(self):
        """It should return True for a valid palindrome"""
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome(self):
        """It should return False for a non-palindrome"""
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_with_spaces(self):
        """It should ignore spaces and check for palindrome"""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_palindrome_with_mixed_case(self):
        """It should ignore case and check for palindrome"""
        self.assertTrue(is_palindrome("RaceCar"))

    def test_not_string(self):
        """It should raise AssertionError for non-string input"""
        with self.assertRaises(AssertionError):
            is_palindrome(123)


if __name__ == "__main__":
    unittest.main()
