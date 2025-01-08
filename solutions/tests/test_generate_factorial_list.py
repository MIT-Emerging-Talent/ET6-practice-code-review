import unittest
from ..generate_factorial_list import factorial_list


class TestMathSequences(unittest.TestCase):
    """Test factorial number generation"""

    def test_factorial_list(self):
        self.assertEqual(factorial_list(5), [1, 1, 2, 6, 24, 120])
        """Tests up to 5!"""
        self.assertEqual(factorial_list(0), [1])
        """Tests up to 0!"""
        self.assertEqual(factorial_list(3), [1, 1, 2, 6])
        """Tests up to 3!"""
        with self.assertRaises(AssertionError):
            factorial_list(-5)
        with self.assertRaises(AssertionError):
            factorial_list("5")


if __name__ == "__main__":
    unittest.main()
