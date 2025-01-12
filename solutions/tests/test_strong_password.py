"""test module for getting strong password
This unittest contains edge cases
for the strong password

Created on Fri Jan 10 2025

@author: Yool Malaak
"""

import unittest

from ..strong_password import strong_password


class TestStrongPassword(unittest.TestCase):
    """
    Unit tests for the strong_password
    function which validates a password
    based on several strength criteria.
    """

    def test_valid_password(self):
        """
        Test case for a valid strong password.
        """
        self.assertTrue(strong_password("Johneavans@2026.com"))
        self.assertTrue(strong_password("J@c0b.israel"))

    def test_missing_uppercase(self):
        """
        Test case where the password is missing an uppercase letter.
        """
        self.assertFalse(strong_password("johnevans@2028.com"))

    def test_missing_lowercase(self):
        """
        Test case where the password is missing a lowercase letter.
        """
        self.assertFalse(strong_password("MEGANMIT$%"))

    def test_missing_digit(self):
        """
        Test case where the password is missing a digit.
        """
        self.assertFalse(strong_password("Megan_mit$%"))

    def test_missing_special(self):
        """
        Test case where the password is missing a special character.
        """
        self.assertFalse(strong_password("Megan2028"))

    def test_short_password(self):
        """
        Test case for a password shorter than 8 characters.
        """
        self.assertFalse(strong_password("Short2!"))

    def test_numeric_password(self):
        """
        Test case for a password with only numbers.
        """
        self.assertFalse(strong_password("202987423690"))

    def test_valid_edge_case(self):
        """
        Test case for a valid password at the edge of the length criteria.
        """
        self.assertTrue(strong_password("Short12!A"))

    def test_empty_password(self):
        """
        Test case for an empty password string.
        """
        self.assertFalse(strong_password(""))


if __name__ == "__main__":
    unittest.main()
