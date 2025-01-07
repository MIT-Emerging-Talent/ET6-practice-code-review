"""
Unit tests for the Pascal's Triangle function.

This script contains test cases to verify the correctness of the `pascal_triangle` function.
The `pascal_triangle` function generates a list of lists representing Pascal's triangle
up to the nth row.

Test Cases:
- Test for basic functionality with a small number of rows.
- Test for edge cases like zero rows or negative input.
- Test for larger values of `n` to ensure the function works for extensive inputs.

To run the tests, execute this script. The results will indicate whether the function
passes all test cases.
"""

import unittest

from solutions.pascal_triangle import pascal_triangle


class TestPascalTriangle(unittest.TestCase):
    """
    Test cases for the pascal_triangle function.

    This class contains multiple test cases that test the correct functionality
    of the pascal_triangle function.Each test case is explained with the expected
    behavior and output for different values of n.
    """

    def test_basic_case(self):
        """
        Test case for generating Pascal's triangle with 5 rows.

        We are testing for the standard case where n = 5. The function should return
        the first 5 rows of Pascal's triangle:
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        """
        result = pascal_triangle(5)
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertEqual(result, expected)

    def test_zero_rows(self):
        """
        Test case when n = 0.

        When n is 0, the function should return an empty list because Pascal's triangle
        cannot be generated with zero rows.
        Expected output: []
        """
        result = pascal_triangle(0)
        expected = []
        self.assertEqual(result, expected)

    def test_single_row(self):
        """
        Test case for generating Pascal's triangle with 1 row.

        For n = 1, the function should return a triangle with only the first row, which is just [1].
        Expected output: [[1]]
        """
        result = pascal_triangle(1)
        expected = [[1]]
        self.assertEqual(result, expected)

    def test_negative_input(self):
        """
        Test case for negative input.

        When n is a negative number (e.g., -5), the function should return an empty list because
        generating a Pascal's triangle with a negative number of rows is not possible.
        Expected output: []
        """
        result = pascal_triangle(-5)
        expected = []
        self.assertEqual(result, expected)

    def test_large_input(self):
        """
        Test case for large input n = 10.

        This test case ensures that the function can generate Pascal's triangle with a larger value
        of n (10 in this case).The output should be the first 10 rows of Pascal's triangle.
        Expected output: A list of 10 rows,starting with [1],[1, 1], .., & ending with the 10th row.
        """
        result = pascal_triangle(10)
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1],
            [1, 8, 28, 56, 70, 56, 28, 8, 1],
            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
        ]
        self.assertEqual(result, expected)

    def test_large_row(self):
        """
        Test case for generating Pascal's triangle with a larger row value (n = 20).

        This test case checks if the function works correctly with an even larger value for n.
        The result should contain the first 20 rows of Pascal's triangle.
        """
        result = pascal_triangle(20)
        self.assertEqual(len(result), 20)  # Ensure there are 20 rows
        self.assertEqual(len(result[19]), 20)  # Ensure the last row has 20 elements


if __name__ == "__main__":
    unittest.main()
