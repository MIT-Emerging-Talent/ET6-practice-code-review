"""
Created on 04/01/2025

@author: Tibyan Khalid
"""

import unittest

from ..is_palindrome import is_palindrome


class Testis_palindrome(unittest.TestCase):
    """Unittests for the is_palindrome function"""

    def test_palindrome(self):
        self.assertEqual(is_palindrome("level"), "Palindrome")

    def test_not_palindrome(self):
        self.assertEqual(is_palindrome("world"), "Not Palindrome")

    def test_empty_string(self):
        "Empty string is considered a Palindrome"
        self.assertEqual(is_palindrome(""), "Palindrome")

    def test_non_string_entry(self):
        "Raise an error if entry is not a string"
        with self.assertRaises(AssertionError):
            is_palindrome(3)

    def test_upper_lower_cases(self):
        "Case matters here, radar is a Palindrome but Radar is not"
        self.assertEqual(is_palindrome("Radar"), "Not Palindrome")
        self.assertEqual(is_palindrome("Radar".lower()), "Palindrome")
