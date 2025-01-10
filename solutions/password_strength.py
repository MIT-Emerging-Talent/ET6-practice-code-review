#!/usr/bin/env python3

"""
A module for checking the strength of a password.

Module contents:
    - password_strength: Checks the strength of a given password.

Author: Anas Ziadah
Created: 2025-01-05
"""

import re


def password_strength(password: str) -> str:
    """Checks the strength of a given password with detailed feedback.

    The password strength is determined by the following rules:
    - Minimum length of 8 characters.
    - Must contain at least one uppercase letter.
    - Must contain at least one lowercase letter.
    - Must contain at least one digit.
    - Must contain at least one special character (e.g., @, #, $, etc.).

    Parameters:
        password: str, the password to check.

    Returns:
        str: A message indicating the missing requirement or 'Strong password'.

    Raises:
        AssertionError: If the input is not a string.

    Examples:
        >>> password_strength("StrongP@ssw0rd")
        'Strong password'
        >>> password_strength("weakpass")
        'Missing uppercase letter'
        >>> password_strength("Short1!")
        'Password too short'
    """
    # Make sure password is a string
    if not isinstance(password, str):
        raise AssertionError("Password must be a string")

    # Handle password strength rules
    # Sequentially validate the password against different strength criteria
    if len(password) < 8:
        return "Password too short"

    if not re.search(r"[A-Z]", password):
        return "Missing uppercase letter"

    if not re.search(r"[a-z]", password):
        return "Missing lowercase letter"

    if not re.search(r"[0-9]", password):
        return "Missing digit"

    if not re.search(r"[@$!%*?&]", password):
        return "Missing special character"

    # If all checks pass, the password is considered strong
    return "Strong password"
