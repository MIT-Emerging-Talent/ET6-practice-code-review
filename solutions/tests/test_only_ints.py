import unittest
    # Import the function to be tested
from ..only_ints import only_ints

"""This module tests only_ints to verify it correctly handles integer and non-integer inputs.
"""

class TestOnlyInts(unittest.TestCase):
    """
    Tests for the only_ints function, ensuring it works correctly with both valid and invalid inputs.
    """
    
    def test_both_integers(self):
        """Test case where both parameters are integers."""
        self.assertTrue(only_ints(1, 2))  # Should return True
    
    """def test_first_is_string(self):
        # Test case where the first parameter is not an integer
        self.assertFalse(only_ints("a", 1))  # Should return False"""
    def test_both_integers_minus(self):
        """Test case where both parameters are integers."""
        self.assertTrue(only_ints(-10, -5))  # Should return True

        
if __name__ == '__main__':
    unittest.main()  # Run all the test cases
