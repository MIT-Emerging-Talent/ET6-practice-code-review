"""
Unit tests for the max_coders_chessboard function.
"""

import unittest
from solutions.max_coders_chessboard import max_coders_chessboard


class TestMaxCodersChessboard(unittest.TestCase):
    """
    Unit tests for the `max_coders_chessboard` function.
    """

    def test_small_board(self):
        """Test the function with a small board size."""
        self.assertEqual(max_coders_chessboard(3), (5, ["C.C", ".C.", "C.C"]))

    def test_even_sized_board(self):
        """Test the function with an even-sized board."""
        self.assertEqual(
            max_coders_chessboard(4), (8, ["C.C.", ".C.C", "C.C.", ".C.C"])
        )

    def test_single_cell_board(self):
        """Test the function with a single-cell board."""
        self.assertEqual(max_coders_chessboard(1), (1, ["C"]))

    def test_invalid_board_size(self):
        """Test the function raises an error for invalid board size."""
        with self.assertRaises(ValueError):
            max_coders_chessboard(0)

    def test_large_board(self):
        """Test the function with a large board size."""
        n = 1000
        result = max_coders_chessboard(n)
        self.assertEqual(result[0], (n * n + 1) // 2)  # Check max coders count
        self.assertEqual(len(result[1]), n)  # Check board size


if __name__ == "__main__":
    unittest.main()
