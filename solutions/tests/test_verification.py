"""the unittests validate names,email address, password, credit card number
    """
import unittest

import verification

class TestValidation(unittest.TestCase):
    
    
    def test_valid_name(self):
        """test that the name pass the validation
        """
        self.assertTrue(verification.validate_name("Pope Francis"))
        
    def test_invalid_name(self):
        """ test that the invalid name fail the validation
        """
        self.assertFalse(verification.validate_name("Mohameed1@234")) 
        self.assertFalse(verification.validate_name("Huaaien195"))   
        
    def test_valid_ID_number(self):
        """test that the valid ID number pass the validation
        """
        self.assertTrue(verification.validate_id_number("204456247"))
        
    def test_invalid_ID_number(self):
        """test that the invalid ID number fail the validation
        """
        self.assertFalse(verification.validate_id_number("A25 3874 926"))
        self.assertFalse(verification.validate_id_number("278 654 68"))   
        self.assertFalse(verification.validate_id_number("2-76 901 254")) 
            
        
    def test_valid_email(self):
        """test that the email is valid and pass the check
        """
        self.assertTrue(verification.validate_email("yool@gmail.com"))
        self.assertTrue(verification.validate_email("mahdia@school.edu"))
        
    
    
    def test_invalid_email(self):
        """ test that invalid fail the validation
        """
        self.assertFalse(verification.validate_email("joseph-email")) 
        self.assertFalse(verification.validate_email("@james.com"))
        self.assertFalse(verification.validate_email("peter@gmail-com"))
        self.assertFalse(verification.validate_email("ahmed@"))
        
        
        
    def test_valid_credit_card(self):
        """ test the credit card number pass the Luhn algorithm
        """
        self.assertTrue(verification.validate_credit_card("6011 1111 1111 1117"))
        self.assertTrue(verification.validate_credit_card("3782 8224 6310 005"))  
        
        
    def test_invalid_credit_card(self):
        """test the invalid credit card number fail the Luhn algorithm
        """
        self.assertFalse(verification.validate_credit_card("1234-5678 9875 0876"))
        self.assertFalse(verification.validate_credit_card("123446acbdte")) 
        self.assertFalse(verification.validate_credit_card("abcdefhgy")) 
        
        
    def test_valid_password(self):
        """ test that the valid password pass the validation criteria
        """
        self.assertTrue(verification.validate_password("Evans@2025!")) 
        self.assertTrue(verification.validate_password("Abr@h@m233"))
        self.assertTrue(verification.validate_password("Jer0megeo@")) 
        
        
    def test_invalid_password(self):
        """test that the invalid password fail the validation criteria
        """
        self.assertFalse(verification.validate_password("evans@2025!"))
        self.assertFalse(verification.validate_password("Password.com"))
        self.assertFalse(verification.validate_password("James_mit@"))
        self.assertFalse(verification.validate_password("123456789"))
        self.assertFalse(verification.validate_password("Job@1"))         
        
if __name__ == "__main__":
    unittest.main()          