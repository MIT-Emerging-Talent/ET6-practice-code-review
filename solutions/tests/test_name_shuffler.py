import sys
print("sys.path:", sys.path)

import unittest
from solutions.name_shuffler import name_shuffler

# Test Cases for the name_shuffler function
class TestNameShuffler(unittest.TestCase):

    def test_empty_input(self):
        """Test empty input raises an error"""
        with self.assertRaises(AssertionError) as context:
            name_shuffler('')
        self.assertEqual(str(context.exception), "Input must be a non-empty string")

    def test_only_first_name_input(self):
        """Test input with a single first name only"""
        self.assertEqual(name_shuffler('Mojtaba'), 'Mojtaba')

    def test_full_name_input(self):
        """Test input with a first and last name"""
        self.assertEqual(name_shuffler('Fatima Malik'), 'Malik Fatima')

    def test_long_name_input(self):
        """Test input with a long name"""
        self.assertEqual(name_shuffler('Fatima Zohra Malik'), 'Malik Zohra Fatima')

if __name__ == '__main__':
    unittest.main()


# run test: python3 -m unittest solutions.tests.test_name_shuffler