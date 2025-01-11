#!/usr/bin/env python3

"""
A module for unit testing the password strength checker.

Module contents:
    - TestPasswordStrength: Unit test for the password_strength function.

Author: Anas Ziadah
Created: 2025-01-05
"""

import unittest
import os
from solutions.password_strength import password_strength


# Debugging: Print current working directory to ensure proper location
print("Current working directory:", os.getcwd())


class TestPasswordStrength(unittest.TestCase):
    """Unit tests for the password_strength function."""

    def test_strong_password(self):
        """Test that a strong password returns the correct message."""
        self.assertEqual(password_strength("StrongP@ssw0rd"), "Strong password")

    def test_weak_password_no_uppercase(self):
        """Test that a weak password with no uppercase letter returns 'Weak password'."""
        self.assertEqual(password_strength("weakpass1@"), "Weak password")

    def test_weak_password_no_special_char(self):
        """Test that a weak password with no special character returns 'Weak password'."""
        self.assertEqual(password_strength("NoSpecial123"), "Weak password")

    def test_weak_password_too_short(self):
        """Test that a short password returns 'Weak password'."""
        self.assertEqual(password_strength("Short1!"), "Weak password")

    def test_strong_password_with_special_characters(self):
        """Test that a valid password with all requirements returns 'Strong password'."""
        self.assertEqual(password_strength("GoodPassword1@"), "Strong password")

    def test_weak_password_missing_special_characters(self):
        """Test that a password missing special characters returns 'Weak password'."""
        self.assertEqual(password_strength("NoSpecial123"), "Weak password")


if __name__ == "__main__":
    unittest.main()
