"""
Module represents unit test for check_palindromes

Created on 01/11/2025
Author fevziismailsahin
"""

import unittest

from solutions.check_palindromes import check_palindromes


class TestPalindromeChecker(unittest.TestCase):
    def test_palindrome_words(self):
        """
        Test: Check palindrome words correctly identified.
        """
        with self.assertLogs(level="INFO") as log:
            check_palindromes(["Radar", "12321", "aA"])
            self.assertIn("'Radar' is a palindrome.", log.output)
            self.assertIn("'12321' is a palindrome.", log.output)
            self.assertIn("'aA' is a palindrome.", log.output)

    def test_non_palindrome_words(self):
        """
        Test: Check non-palindrome words correctly identified.
        """
        with self.assertLogs(level="INFO") as log:
            check_palindromes(["Hello", "12345", "Test"])
            self.assertIn("'Hello' is not a palindrome.", log.output)
            self.assertIn("'12345' is not a palindrome.", log.output)
            self.assertIn("'Test' is not a palindrome.", log.output)

    def test_mixed_case(self):
        """
        Test: Check case-insensitive palindrome detection.
        """
        with self.assertLogs(level="INFO") as log:
            check_palindromes(["aA"])
            self.assertIn("'aA' is a palindrome.", log.output)

    def test_special_characters(self):
        """
        Test: Check if special characters are correctly removed and palindrome check works.
        """
        with self.assertLogs(level="INFO") as log:
            check_palindromes(["1.232.1"])
            self.assertIn("'1.232.1' is a palindrome.", log.output)


if __name__ == "__main__":
    unittest.main()
