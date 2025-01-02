import sys
import os
import unittest

# Add the project root directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from solutions.decimal_to_binary import decimal_to_binary


class TestDecimalToBinary(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(255), "11111111")

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "0")

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            decimal_to_binary(-5)

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            decimal_to_binary(10.5)
        with self.assertRaises(ValueError):
            decimal_to_binary("string")


if __name__ == "__main__":
    unittest.main()
