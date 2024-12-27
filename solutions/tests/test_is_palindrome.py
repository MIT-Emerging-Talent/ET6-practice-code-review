import unittest

from ..is_palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    """Test the is_palindrome function"""

    def TestEmptyString(self):
        """It should return True for an empty string"""
        self.assertTrue(is_palindrome(""))

    def TestSingleCharacter(self):
        """It should return True for a single character"""
        self.assertTrue(is_palindrome("a"))

    def TestPalindrome(self):
        """It should return True for a valid palindrome"""
        self.assertTrue(is_palindrome("racecar"))

    def TestNonPalindrome(self):
        """It should return False for a non-palindrome"""
        self.assertFalse(is_palindrome("hello"))

    def TestPalindromeWithSpaces(self):
        """It should ignore spaces and check for palindrome"""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def TestPalindromeWithMixedCase(self):
        """It should ignore case and check for palindrome"""
        self.assertTrue(is_palindrome("RaceCar"))

    def TestNotString(self):
        """It should raise AssertionError for non-string input"""
        with self.assertRaises(AssertionError):
            is_palindrome(123)

if __name__ == "__main__":
    unittest.main()
