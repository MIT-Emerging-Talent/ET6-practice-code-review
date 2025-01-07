"""This function validate names,email address, password, credit card number, and id number
"""
def validate_name(name):
    """ validate the names to ensure that it contains alphabetical characters and spaces only

    parameters:
        name (str): the name to be validated 

    Returns:
        bool: true if the name is valid, false otherwise.
    """
    if all(char.isalpha() or char.isspace() for char in name):
        return True
    else:
        return False


def validate_id_number(id_number):
    """ validate ID number that contains numbers only and has at least 9 digits

    parameters:
        ID_number (str): ID number to validate

    Returns:
        bool:  true if true, otherwise false
    """
    if  id_number.isdigit() and len(id_number) >= 9:
        return True
    else:
        return False

def validate_email(email):
    """ Validate the email address that contain @ and dot(.)

    parameters:
        email (str): email address to be validated

    Returns:
        bool: true if email address is valid, false otherwise
    """
    if "@" not in email or "." not in email:
        return False
    at_index = email.index("@")
    dot_index = email.rindex(".")
    if at_index == 0 or dot_index < at_index + 2 or dot_index == len(email) - 1:
        return False
    return True

def validate_credit_card(card_number):
    """ validate credit card number using the Luhn algorithm

    parameters:
        card_number (str): credit card number to be validated

    Returns:
        bool: true if the credit card number is valid, otherwise false
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

def validate_password(password):
    """ validate password base on the following criteria
    - at least 8 characters
    - at least one uppercase
    - at least one lowercase
    - at least one number
    - at least one special character("!@#$%^&*()-+")

    parameters:
        password (str): password to be checked

    Returns:
        bool: true if password is valid, false otherwise.
    """
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-+" for char in password)
    return has_upper and has_lower and has_digit and has_special     