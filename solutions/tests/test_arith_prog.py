"""unittest code verifies the behavior of the function generate_arithmetic_progression"""
import unittest

from solutions.arith_prog import generate_arithmetic_progression

class TestArithmeticProgression(unittest.TestCase):
    """To test the function generate_arithmetic_progression"""

    def test_positive_difference(self):
        """Tests a common positive difference with multiple terms"""
        result = generate_arithmetic_progression(2, 3, 5)
        self.assertEqual(result, [2, 5, 8, 11, 14])

    def test_negative_difference(self):
        """Tests a negative common difference"""
        result = generate_arithmetic_progression(10, -2, 5)
        self.assertEqual(result, [10, 8, 6, 4, 2])

    def test_zero_difference(self):
        """Checks if the function handles a zero difference correctly"""
        result = generate_arithmetic_progression(7, 0, 4)
        self.assertEqual(result, [7, 7, 7, 7])

    def test_float_values(self):
        """Ensures the function works with floating-point values"""
        result = generate_arithmetic_progression(1.5, 0.5, 4)
        self.assertEqual(result, [1.5, 2.0, 2.5, 3.0])

    def test_no_terms(self):
        """Checks the behavior when the number of terms is zero"""
        result = generate_arithmetic_progression(3, 2, 0)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
