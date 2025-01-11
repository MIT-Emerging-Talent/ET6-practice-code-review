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

    def test_weak_password_no_uppercase(self):
        """Test that a weak password with no uppercase letter returns 'Missing uppercase letter'."""
        self.assertEqual(password_strength("weakpass1@"), "Missing uppercase letter")

    def test_weak_password_no_special_char(self):
        """Test that a weak password with no special character returns 'Missing special character'."""
        self.assertEqual(password_strength("NoSpecial123"), "Missing special character")

    def test_weak_password_too_short(self):
        """Test that a short password returns 'Password too short'."""
        self.assertEqual(password_strength("Short1!"), "Password too short")

    def test_strong_password_with_special_characters(self):
        """Test that a valid password with all requirements returns 'Strong password'."""
        self.assertEqual(password_strength("GoodPassword1@"), "Strong password")

    def test_weak_password_missing_special_characters(self):
        """Test that a password missing special characters returns 'Missing special character'."""
        self.assertEqual(password_strength("NoSpecial123"), "Missing special character")

    def test_empty_password(self):
        """Test that an empty password returns 'Password too short'."""
        self.assertEqual(password_strength(""), "Password too short")

    def test_password_with_only_digits(self):
        """Test that a password with only digits returns 'Missing uppercase letter'."""
        self.assertEqual(password_strength("12345678"), "Missing uppercase letter")

    def test_password_with_only_special_characters(self):
        """Test that a password with only special characters returns 'Missing uppercase letter'."""
        self.assertEqual(password_strength("!@#$%^&*"), "Missing uppercase letter")

    def test_invalid_input(self):
        """Test that a non-string input raises an AssertionError."""
        with self.assertRaises(AssertionError) as context:
            password_strength(12345)  # Non-string input
        self.assertEqual(str(context.exception), "Password must be a string")


if __name__ == "__main__":
    unittest.main()
