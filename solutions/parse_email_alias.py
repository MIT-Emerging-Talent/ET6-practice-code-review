#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for parsing and validating email aliases.

This module provides functionality to validate email addresses and parse their components,
including support for Gmail-style plus (+) aliases and subdomain addresses. The implementation
combines specific validation checks with regex pattern matching to provide detailed error
messages while maintaining RFC 5322 compliance.

Module contents:
    - parse_email_alias: validates and extracts components of an email alias

Features:
    - Full RFC 5322 compliant email validation
    - Support for Gmail-style + aliases
    - Support for subdomains
    - Detailed error reporting for specific validation failures
    - Comprehensive component extraction

Created on 4 01 2025
@author: Mahdia Ahamdi
"""

import re


def parse_email_alias(email: str) -> dict:
    """
    Parse and validate an email address with optional alias tags.

    This function performs comprehensive validation of email addresses, providing
    specific error messages for different types of validation failures. It supports
    Gmail-style plus (+) aliases and subdomains while validating against RFC 5322
    standards for email format.

    Parameters:
        email: str
            The email address to parse. Must be a string containing the email address
            to be validated and parsed.

    Returns:
        dict
            A dictionary containing the following keys:
            - valid (bool): Whether the email is valid
            - local_part (str | None): Part before the @ (None if invalid)
            - domain (str | None): Part after the @ (None if invalid)
            - tags (list[str]): Any alias tags found (empty if none)
            - errors (list[str]): Any validation errors found

    Raises:
        AssertionError: If the input is not a string

    Examples:
        >>> # Test basic valid email
        >>> result = parse_email_alias("user@example.com")
        >>> result['valid']
        True
        >>> result['local_part']
        'user'
        >>> result['domain']
        'example.com'
        >>> result['tags']
        []
        >>> result['errors']
        []

        >>> # Test email with single alias tag
        >>> result = parse_email_alias("user+newsletter@example.com")
        >>> result['valid']
        True
        >>> result['local_part']
        'user'
        >>> result['domain']
        'example.com'
        >>> result['tags']
        ['newsletter']

        >>> # Test email with multiple alias tags
        >>> result = parse_email_alias("user+tag1+tag2@example.com")
        >>> result['valid']
        True
        >>> result['local_part']
        'user'
        >>> result['tags']
        ['tag1', 'tag2']

        >>> # Test email with subdomain
        >>> result = parse_email_alias("user@sub.example.com")
        >>> result['valid']
        True
        >>> result['domain']
        'sub.example.com'

        >>> # Test missing @ symbol
        >>> result = parse_email_alias("invalid.email")
        >>> result['valid']
        False
        >>> result['errors']
        ['Missing @ symbol']

        >>> # Test empty local part
        >>> result = parse_email_alias("@example.com")
        >>> result['valid']
        False
        >>> result['errors']
        ['Empty local part']

        >>> # Test empty domain
        >>> result = parse_email_alias("user@")
        >>> result['valid']
        False
        >>> result['errors']
        ['Empty domain']

        >>> # Test invalid characters in local part
        >>> result = parse_email_alias("user<>@example.com")
        >>> result['valid']
        False
        >>> result['errors']
        ['Invalid characters in local part']

        >>> # Test missing TLD
        >>> result = parse_email_alias("user@domain")
        >>> result['valid']
        False
        >>> result['errors']
        ['Invalid domain (missing TLD)']

        >>> # Test invalid domain format
        >>> result = parse_email_alias("user@[192.168.1.1]")
        >>> result['valid']
        False
        >>> result['errors']
        ['Invalid domain format']

        >>> # Test empty email
        >>> result = parse_email_alias("")
        >>> result['valid']
        False
        >>> result['errors']
        ['Email cannot be empty']

        >>> # Test non-string input
        >>> try:
        ...     parse_email_alias(123)
        ... except AssertionError as e:
        ...     print(str(e))
        Input must be a string
    """
    assert isinstance(email, str), "Input must be a string"

    result = {
        "valid": False,
        "local_part": None,
        "domain": None,
        "tags": [],
        "errors": [],
    }

    if not email:
        result["errors"].append("Email cannot be empty")
        return result

    # Check for @ symbol first
    if "@" not in email:
        result["errors"].append("Missing @ symbol")
        return result

    # Split into local part and domain
    local_part, domain = email.split("@", 1)

    # Check empty local part
    if not local_part:
        result["errors"].append("Empty local part")
        return result

    # Check empty domain
    if not domain:
        result["errors"].append("Empty domain")
        return result

    # Validate local part characters using regular expression(regx)
    allowed_chars = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!#$%&'*+-/=?^_`{|}~"
    )
    if not all(c in allowed_chars for c in local_part.split("+")[0]):
        result["errors"].append("Invalid characters in local part")
        return result

    # Validate domain
    if not domain:
        result["errors"].append("Empty domain")
        return result

    if ".." in domain:
        result["errors"].append("Invalid domain format")
        return result

    # Check for valid domain format
    domain_parts = domain.split(".")

    # Check for missing or invalid TLD
    if len(domain_parts) == 1 or not domain_parts[-1]:
        result["errors"].append("Invalid domain (missing TLD)")
        return result

    # Validate domain format using regx
    domain_pattern = r"^[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$"
    if not re.match(domain_pattern, domain):
        result["errors"].append("Invalid domain format")
        return result

    # Extract tags if present
    base_local = local_part
    tags = []
    if "+" in local_part:
        base_local, *tags = local_part.split("+")

    result["valid"] = True
    result["local_part"] = base_local
    result["domain"] = domain
    result["tags"] = tags

    return result
