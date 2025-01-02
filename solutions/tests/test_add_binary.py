"""
Unit tests for the add_binary function.
"""

import unittest

from solutions.add_binary import add_binary


class TestAddBinary(unittest.TestCase):
    """
    Unit tests for the add_binary function.
    """

    def test_basic_case(self):
        """
        Tests basic binary addition.
        Expected output: '100'
        """
        self.assertEqual(add_binary("11", "1"), "100")

    def test_different_lengths(self):
        """
        Tests binary strings of different lengths.
        Expected output: '10101'
        """
        self.assertEqual(add_binary("1010", "1011"), "10101")

    def test_all_zeros(self):
        """
        Tests when both inputs are '0'.
        Expected output: '0'
        """
        self.assertEqual(add_binary("0", "0"), "0")

    def test_leading_zeros(self):
        """
        Tests inputs with leading zeros.
        Expected output: '100'
        """
        self.assertEqual(add_binary("00011", "1"), "100")

    def test_large_binary_strings(self):
        """
        Tests very large binary strings.
        Input: bin_num1 = '1'*10000, bin_num2 = '1'
        Expected output: '1' followed by 10000 '0's.
        """
        bin_num1 = "1" * 10000
        bin_num2 = "1"
        expected = "1" + "0" * 10000
        self.assertEqual(add_binary(bin_num1, bin_num2), expected)

    def test_empty_input(self):
        """
        Tests that a ValueError is raised for empty input strings.
        """
        with self.assertRaises(ValueError):
            add_binary("", "1")
        with self.assertRaises(ValueError):
            add_binary("1", "")

    def test_invalid_characters(self):
        """
        Tests that a ValueError is raised for inputs with invalid characters.
        Examples:
        - Input: '102', '1'
        - Input: '11a', '1'
        """
        with self.assertRaises(ValueError):
            add_binary("102", "1")
        with self.assertRaises(ValueError):
            add_binary("11a", "1")

    def test_whitespace_in_input(self):
        """
        Tests that a ValueError is raised for input strings with embedded whitespace.
        """
        with self.assertRaises(ValueError):
            add_binary(" 1010 ", "101")
        with self.assertRaises(ValueError):
            add_binary("1010", " 101 ")

    def test_boundary_case_zeros(self):
        """
        Tests binary addition where one or both inputs are zeros with leading zeros.
        Expected output: '0'
        """
        self.assertEqual(add_binary("0", "00000"), "0")
        self.assertEqual(add_binary("000", "0"), "0")

    def test_alternating_pattern(self):
        """
        Tests binary strings with alternating patterns of '1' and '0'.
        Expected output: '111111'
        """
        self.assertEqual(add_binary("101010", "010101"), "111111")

    def test_boundary_case_max_length_simple(self):
        """
        Tests the function with maximum length inputs with simple values.
        Input: bin_num1 = '1'*10000, bin_num2 = '0'*10000
        Expected output: '1'*10000
        """
        bin_num1 = "1" * 10000
        bin_num2 = "0" * 10000
        expected = "1" * 10000
        self.assertEqual(add_binary(bin_num1, bin_num2), expected)

    def test_boundary_case_max_length_mixed(self):
        """
        Tests the function with maximum length inputs with mixed patterns.
        Input: bin_num1 = '10'*5000, bin_num2 = '01'*5000
        Expected output: '111...111' (10000 '1's)
        """
        bin_num1 = "10" * 5000
        bin_num2 = "01" * 5000
        expected = "1" * 10000
        self.assertEqual(add_binary(bin_num1, bin_num2), expected)


if __name__ == "__main__":
    unittest.main()
