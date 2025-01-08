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
    """Checks the strength of a given password.

    The password strength is determined by the following rules:
    - Minimum length of 8 characters.
    - Must contain at least one uppercase letter.
    - Must contain at least one lowercase letter.
    - Must contain at least one digit.
    - Must contain at least one special character (e.g., @, #, $, etc.).

    Parameters:
        password: str, the password to check.

    Returns:
        str: A message indicating why the password is weak or strong.

    Examples:
        >>> password_strength("StrongP@ssw0rd")
        'Strong password'
        >>> password_strength("weakpass")
        'Password too short'
        >>> password_strength("Short1!")
        'Password too short'
        >>> password_strength("NoSpecial123")
        'Missing special character'
    """

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

    return "Strong password"
