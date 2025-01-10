#!/usr/bin/env python3

"""
A module for unit testing the password strength checker.

Module contents:
    - TestPasswordStrength: Unit test for the password_strength function.

Author: Anas Ziadah
Created: 2025-01-05
"""

import unittest
from solutions.password_strength import password_strength


class TestPasswordStrength(unittest.TestCase):
    """Unit tests for the password_strength function."""

    def test_strong_password(self):
        """Test that a strong password returns the correct message."""
        self.assertEqual(password_strength("StrongP@ssw0rd"), "Strong password")

    def test_weak_password_criteria(self):
        """Test various weak passwords missing specific criteria."""
        test_cases = [
            ("weakpass1@", "Missing uppercase letter"),  # No uppercase
            ("NoSpecial123", "Missing special character"),  # No special character
            ("Short1!", "Password too short"),  # Too short
            ("", "Password too short"),  # Empty password
            ("12345678", "Missing uppercase letter"),  # Only digits
            ("abcdefgh", "Missing uppercase letter"),  # Only lowercase
            ("ABCDEFGH", "Missing lowercase letter"),  # Only uppercase
            ("!@#$%^&*", "Missing uppercase letter"),  # Only special characters
        ]
        for password, expected in test_cases:
            with self.subTest(password=password):
                self.assertEqual(password_strength(password), expected)

    def test_strong_password_variations(self):
        """Test variations of strong passwords."""
        test_cases = [
            ("GoodPassword1@", "Strong password"),
            ("Another$tr0ng1", "Strong password"),
        ]
        for password, expected in test_cases:
            with self.subTest(password=password):
                self.assertEqual(password_strength(password), expected)


if __name__ == "__main__":
    unittest.main()
