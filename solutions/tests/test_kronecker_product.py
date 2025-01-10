"""
test_kronecker_product.py

This module contains unit tests for the `kronecker_product` function.
The function computes the Kronecker product
(matrix_a ⊗ matrix_b)
for two matrices `matrix_a` and `matrix_b`.

Author: Fahed Daibes
Date: Thu Jan 9 2025
Group: ET6-foundations-group-16

Tests:
- Valid integer matrix inputs for Kronecker product.
- Invalid inputs, such as non-matrix or non-list inputs.
"""

import unittest

from solutions.kronecker_product import kronecker_product


class TestKroneckerProduct(unittest.TestCase):
    """
    This test class contains unit tests for the `kronecker_product` function.

    It tests the function's ability to compute the Kronecker product for various valid inputs,
    including edge cases and invalid inputs such as non-list matrices.
    """

    def test_valid_matrices(self):
        """Test case for valid 2x2 matrices."""
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[0, 5], [6, 7]]
        expected_result = [
            [0, 5, 0, 10],
            [6, 7, 12, 14],
            [0, 15, 0, 20],
            [18, 21, 24, 28],
        ]
        self.assertEqual(kronecker_product(matrix_a, matrix_b), expected_result)

    def test_identity_matrix(self):
        """Test case for Kronecker product with identity matrix."""
        matrix_a = [[1, 0], [0, 1]]  # 2x2 identity matrix
        matrix_b = [[2, 3], [4, 5]]  # 2x2 matrix
        expected_result = [[2, 3, 0, 0], [4, 5, 0, 0], [0, 0, 2, 3], [0, 0, 4, 5]]
        self.assertEqual(kronecker_product(matrix_a, matrix_b), expected_result)

    def test_zero_matrix(self):
        """Test case for Kronecker product with a zero matrix."""
        matrix_a = [[0, 0], [0, 0]]  # 2x2 zero matrix
        matrix_b = [[1, 2], [3, 4]]  # 2x2 matrix
        expected_result = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]  # All zeros
        self.assertEqual(kronecker_product(matrix_a, matrix_b), expected_result)

    def test_invalid_input_string(self):
        """Test case for non-matrix input."""
        with self.assertRaises(AssertionError):
            kronecker_product("matrix_a", [[1, 2]])

    def test_invalid_input_non_array(self):
        """Test case for invalid input that is not a list."""
        with self.assertRaises(AssertionError):
            kronecker_product([1, 2], [[1, 2]])

    def test_non_square_matrix(self):
        """Test case for non-square matrices."""
        matrix_a = [[1, 2, 3], [4, 5, 6]]  # 2x3 matrix
        matrix_b = [[1, 2], [3, 4]]  # 2x2 matrix
        result = kronecker_product(matrix_a, matrix_b)
        self.assertEqual(len(result), 4)  # 4 rows in the result
        self.assertEqual(len(result[0]), 6)  # 6 columns in the result


if __name__ == "__main__":
    unittest.main()
