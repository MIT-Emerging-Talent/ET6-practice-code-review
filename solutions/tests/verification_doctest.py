"""
test for verification function. the test validate the data that is passed the criteria, and vice versa.
"""

from verification import(
    validate_name,
    validate_id_number, 
    validate_email, 
    validate_credit_card,
    validate_password
)


def test_validate_name():
    """
    >>> validate_name("Camilla Massa")
    True
    >>> validate_name("Joe_Biden")
    False
    >>> validate_name("Mohammed122")
    False
    """
    
def test_validate_id_number():
    """
    >>> validate_id_number("204456247")
    True
    >>> validate_id_number("204456")
    False
    >>> validate_id_number("2A4576983021765")
    False
    >>> validate_id_number("24-6 7684 9085")
    False
    """ 
    
    
def test_credit_card():
    """
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
    
    
def test_validate_email():
    """
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
    
    
def test_validate_passwords():
    """
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