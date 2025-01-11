import unittest
from solutions.reverse import reverse_string

class TestReverseString(unittest.TestCase):
    """
    Test class for the reverse_string function.
    This class contains test cases to validate the functionality of the reverse_string function.
    """
    
    def test_reverse_basic(self):
        """
        Test case for a basic string reversal.
        """
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_empty(self):
        """
        Test case for an empty string.
        The expected output is an empty string.
        """
        self.assertEqual(reverse_string(""), "")

    def test_reverse_single_character(self):
        """
        Test case for a string with a single character.
        The expected output is the same single character.
        """
        self.assertEqual(reverse_string("a"), "a")

if __name__ == "__main__":
    unittest.main()