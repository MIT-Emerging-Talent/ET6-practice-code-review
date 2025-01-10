#!/user/bin/env/python3
# -*- coding: utf-8 -*-
"""
Created on Dec 29 2024

@author: Yool Malaak

test for verification function. the test validate the data that is passed the criteria, and vice versa.
"""


def validate_name(name):
    """validate the names to ensure that it contains alphabetical characters and spaces only

    parameters:
        name (str): the name to be validated

    Returns:
        bool: true if the name is valid, false otherwise.
    examples:
    >>> validate_name("Camilla Massa")
    True
    >>> validate_name("Joe_Biden")
    False
    >>> validate_name("Mohammed122")
    False
    """
    if all(char.isalpha() or char.isspace() for char in name):
        return True
    else:
        return False


def validate_id_number(id_number):
    """validate ID number that contains numbers only and has at least 9 digits

    parameters:
        ID_number (str): ID number to validate

    Returns:
        bool:  true if true, otherwise false
    examples:
    >>> validate_id_number("204456247")
    True
    >>> validate_id_number("204456")
    False
    >>> validate_id_number("2A4576983021765")
    False
    >>> validate_id_number("24-6 7684 9085")
    False
    """
    if id_number.isdigit() and len(id_number) >= 9:
        return True
    else:
        return False


def validate_credit_card(card_number):
    """validate credit card number using the Luhn algorithm

    parameters:
        card_number (str): credit card number to be validated

    Returns:
        bool: true if the credit card number is valid, otherwise false
    examples:
    >>> validate_credit_card("6011 1111 1111 1117")
    True
    >>> validate_credit_card("3782 8224 6310 005")
    True
    >>> validate_credit_card("12345-6789038693")
    False
    >>> validate_credit_card("2A89497534975jc")
    False
    >>> validate_credit_card("abcdefghijkl")
    False
    """
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        return False
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0


def validate_email(email):
    """Validate the email address that contain @ and dot(.)

    parameters:
        email (str): email address to be validated

    Returns:
        bool: true if email address is valid, false otherwise
    examples:
    >>> validate_email("martha@gmail.com")
    True
    >>> validate_email("katrina@school.edu")
    True
    >>> validate_email("patrick-email.com")
    False
    >>> validate_email("adam@gmail_com")
    False
    >>> validate_email("ahmed@")
    False
    """
    if "@" not in email or "." not in email:
        return False
    at_index = email.index("@")
    dot_index = email.rindex(".")
    if at_index == 0 or dot_index < at_index + 2 or dot_index == len(email) - 1:
        return False
    return True


def validate_password(password):
    """validate password base on the following criteria
    - at least 8 characters
    - at least one uppercase
    - at least one lowercase
    - at least one number
    - at least one special character("!@#$%^&*()-+")

    parameters:
        password (str): password to be checked

    Returns:
        bool: true if password is valid, false otherwise.
    examples:
    >>> validate_password("Johneavans@2026.com")
    True
    >>> validate_password("J@c0b.israel")
    True
    >>> validate_password("johnevans@2028.com")
    False
    >>> validate_password("Megan_mit$%")
    False
    >>> validate_password("202987423690")
    False
    >>> validate_password("Short2!")
    False
    """
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-+" for char in password)
    return has_upper and has_lower and has_digit and has_special
