import unittest

from password_generator import password_generator

class PasswordGeneratorTests(unittest.TestCase):
    def test_empty_password_length(self):

        """
        Verify that an empty password length raises a ValueError.
        
        :raises ValueError: when calling password_generator with an empty string
        """
        with self.assertRaises(ValueError):
            password_generator("")
            
        
    def test_invalid_password_length1(self):
        """
        Verify that a password length of 1 raises a ValueError.
        
        :raises ValueError: when calling password_generator with a length of 1
        """
        with self.assertRaises(ValueError):
            password_generator(1)
        
    def test_invalid_password_length2(self):
        """
        Verify that a password length of 0 raises a ValueError.
        
        :raises ValueError: when calling password_generator with a length of 0
        """
        with self.assertRaises(ValueError):
            password_generator(0)
        
    def test_invalid_password_length3(self):
        """
        Verify that a negative password length raises a ValueError.
        
        :raises ValueError: when calling password_generator with a negative length
        """
        
        with self.assertRaises(ValueError):
            password_generator(-1)
            
    def test_string_input(self):
        """
        Verify that a string input raises a ValueError.
        
        :raises ValueError: when calling password_generator with a string
        """
        
        with self.assertRaises(ValueError):
            password_generator("hello")
            
    def test_float_input(self):
        """
        Verify that a float input raises a ValueError.
        
        :raises ValueError: when calling password_generator with a float
        """
        with self.assertRaises(ValueError):
            password_generator(3.14)
            
    def test_valid_password_length1(self):
        """
        Verify that a password of length 4 is generated correctly.

        :assert: the generated password has a length of 4
        """

        password = password_generator(4)
        self.assertEqual(len(password), 4)
        
    def test_valid_password_length(self):
        """
        Verify that a password of length 10 is generated correctly.

        :assert: the generated password has a length of 10
        """
        
        password = password_generator(10)
        self.assertEqual(len(password), 10)
        
        
if __name__ == "__main__":
    unittest.main()
