import unittest

from password_generator import *

class PasswordGeneratorTests(unittest.TestCase):
      def test_empty_password_length(self):

        """
        Verify that an empty password length raises a ValueError.
        
        :raises ValueError: when calling password_generator with an empty string
        """
        with self.assertRaises(ValueError):
            password_generator("")
            