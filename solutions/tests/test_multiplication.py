import unittest
from ..multiplication import multiplication


class TestMultiplication(unittest.TestCase):
    """
    Unit tests for the `reversed_positive_number` function.
    """

    def test_multiply_3_num_with_single_digit(self):
        """Tests multiplication of 3 single-digit numbers ."""
        result = multiplication(first_num=5, sec_num=5, third_num=2)
        expected_result = 50
        self.assertEqual(result, expected_result)

    def test_multiply_3_num_with_two_digit(self):
        """Tests multiplication of 3 double-digit numbers ."""
        result = multiplication(first_num=10, sec_num=20, third_num=30)
        expected_result = 6000
        self.assertEqual(result, expected_result)

    def test_multiply_3_negative_num_with_two_digit(self):
        """Tests multiplication of 3 negative double-digit numbers ."""
        result = multiplication(first_num=-10, sec_num=-20, third_num=-30)
        expected_result = -6000
        self.assertEqual(result, expected_result)
