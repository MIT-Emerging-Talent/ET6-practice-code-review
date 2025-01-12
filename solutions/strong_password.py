"""The module input, verify password and
return strong password

Created on Fri Jan 10 2025
@author: Yool Malaak
"""


def strong_password(password):
    """Validate password based on the following criteria for strength:
    - At least 8 characters long
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one numeric digit
    - At least one special character from "!@#$%^&*()-+"

    Parameters:
        password (str): The password to be checked.

    Returns:
        bool: True if the password is strong, False otherwise.

    Examples:
    >>> strong_password("Johneavans@2026.com")
    True
    >>> strong_password("J@c0b.israel")
    True
    >>> strong_password("johnevans@2028.com")
    False
    >>> strong_password("Megan_mit$%")
    False
    >>> strong_password("202987423690")
    False
    >>> strong_password("Short2!")
    False
    """

    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-+" for char in password)
    return has_upper and has_lower and has_digit and has_special
