#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the parse_email_alias module.

This module contains unit tests for the parse_email_alias function,
including normal cases, edge cases, and error conditions.

Created on 4 01 2025
@author: Mahdia Ahmadi
"""

import unittest

from solutions.parse_email_alias import parse_email_alias


class TestParseEmailAlias(unittest.TestCase):
    """
    Test suite for the parse_email_alias function.

    This class contains unit tests covering various email parsing scenarios,
    including valid emails, invalid formats, and edge cases.
    """

    def test_valid_email(self):
        """
        Test a basic valid email address.

        Verifies that the function correctly parses a standard email address.
        """
        self.assertEqual(parse_email_alias("user@example.com")["valid"], True)

    def test_email_with_tags(self):
        """
        Test an email with alias tags.

        Checks if the function properly handles Gmail-style + aliases.
        """
        self.assertEqual(parse_email_alias("user+tag@example.com")["tags"], ["tag"])

    def test_multiple_tags(self):
        """
        Test an email with multiple alias tags.

        Ensures the function can handle multiple + separated tags.
        """
        self.assertEqual(
            parse_email_alias("user+tag1+tag2@example.com")["tags"], ["tag1", "tag2"]
        )

    def test_subdomain(self):
        """
        Test an email with a subdomain.

        Verifies correct handling of domain names with subdomains.
        """
        self.assertEqual(
            parse_email_alias("user@sub.example.com")["domain"], "sub.example.com"
        )

    def test_invalid_email_format(self):
        """
        Test an email without @ symbol.

        Checks if the function correctly identifies missing @ as an error.
        """
        self.assertIn("Missing @ symbol", parse_email_alias("invalid.email")["errors"])

    def test_empty_local_part(self):
        """
        Test an email with empty local part.

        Ensures the function recognizes an empty local part as an error.
        """
        self.assertIn("Empty local part", parse_email_alias("@example.com")["errors"])

    def test_invalid_characters_in_local_part(self):
        """
        Test an email with invalid characters in the local part.

        Verifies that the function detects non-standard characters in the local part.
        """
        self.assertIn(
            "Invalid characters in local part",
            parse_email_alias("user<>@example.com")["errors"],
        )

    def test_empty_domain(self):
        """
        Test an email with empty domain.

        Checks if the function correctly identifies an empty domain as an error.
        """
        self.assertIn("Empty domain", parse_email_alias("user@")["errors"])

    def test_missing_top_level_domain(self):
        """
        Test an email with missing top-level domain.

        Verifies that the function detects domains without TLDs as invalid.
        """
        self.assertIn(
            "Invalid domain (missing TLD)", parse_email_alias("user@sub.")["errors"]
        )

    def test_invalid_domain_format(self):
        """
        Test an email with an invalid domain format.

        Checks if the function correctly identifies non-standard domain formats.
        """
        self.assertIn(
            "Invalid domain format", parse_email_alias("user@[192.168.1.1]")["errors"]
        )

    def test_empty_email(self):
        """
        Test an empty email string.

        Ensures the function handles empty inputs correctly.
        """
        self.assertIn("Email cannot be empty", parse_email_alias("")["errors"])

    def test_non_string_input(self):
        """
        Test non-string input to check defensive assertion.

        Verifies that the function raises an AssertionError for non-string inputs.
        """
        with self.assertRaises(AssertionError):
            parse_email_alias(123)

    def test_long_local_part(self):
        """
        Test an email with a very long local part.

        Checks if the function can handle unusually long local parts.
        """
        long_local = "a" * 1000
        self.assertTrue(parse_email_alias(f"{long_local}@example.com")["valid"])

    def test_long_domain(self):
        """
        Test an email with a very long domain.

        Ensures the function can handle unusually long domain names.
        """
        long_domain = "example.com" * 100
        self.assertTrue(parse_email_alias(f"user@{long_domain}")["valid"])


if __name__ == "__main__":
    unittest.main()
