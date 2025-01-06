import unittest
from ..int_to_roman import int_to_roman

class TestIntToRoman(unittest.TestCase):
    """Unit tests for the `int_to_roman` function."""

    def test_basic_conversion(self):
        """Tests standard Roman numeral conversions."""
        self.assertEqual(int_to_roman(3), "III")

    def test_boundary_values(self):
        """Tests boundary cases."""
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")

    def test_out_of_range(self):
        """Tests invalid range."""
        with self.assertRaises(AssertionError):
            int_to_roman(0)

if __name__ == "__main__":
    unittest.main()
