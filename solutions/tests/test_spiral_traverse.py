import unittest

from solutions.spiral_traverse import spiral_traverse


class TestSpiralTraversal(unittest.TestCase):
    """
    This test class contains unit tests for the `spiral_traverse` function.

    It tests the function's ability to handle matrices of various shapes and sizes,
    including edge cases like empty matrices and single-element matrices.
    Defensive tests for invalid inputs are also included.
    """

    def test_square_matrix(self):
        """Test case for a square matrix with numeric elements."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(spiral_traverse(matrix), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_single_row(self):
        """Test case for a single-row matrix."""
        matrix = [[1, 2, 3, 4]]
        self.assertEqual(spiral_traverse(matrix), [1, 2, 3, 4])

    def test_single_column(self):
        """Test case for a single-column matrix."""
        matrix = [[1], [2], [3], [4]]
        self.assertEqual(spiral_traverse(matrix), [1, 2, 3, 4])

    def test_rectangular_matrix(self):
        """Test case for a rectangular matrix."""
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(spiral_traverse(matrix), [1, 2, 3, 6, 5, 4])

    def test_empty_matrix(self):
        """Test case for an empty matrix."""
        matrix = []
        self.assertEqual(spiral_traverse(matrix), [])

    def test_single_element_matrix(self):
        """Test case for a single-element matrix."""
        matrix = [[1]]
        self.assertEqual(spiral_traverse(matrix), [1])

    def test_mixed_numeric_types(self):
        """Test case for a matrix with mixed numeric types (int and float)."""
        matrix = [[1.1, 2, 3], [4, 5.5, 6], [7, 8, 9.9]]
        self.assertEqual(spiral_traverse(matrix), [1.1, 2, 3, 6, 9.9, 8, 7, 4, 5.5])

    def test_invalid_input_none(self):
        """Test case for None as input."""
        with self.assertRaises(ValueError):
            spiral_traverse(None)

    def test_invalid_input_non_matrix(self):
        """Test case for input that is not a 2D list."""
        with self.assertRaises(ValueError):
            spiral_traverse([1, 2, 3])

    def test_invalid_input_non_numeric(self):
        """Test case for a matrix with non-numeric elements."""
        with self.assertRaises(ValueError):
            spiral_traverse([[1, "a", 3], [4, 5, 6]])


if __name__ == "__main__":
    unittest.main()
