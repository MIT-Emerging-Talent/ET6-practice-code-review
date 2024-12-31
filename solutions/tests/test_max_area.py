import unittest
from solutions.max_area import Solution


class test_max_area(unittest.TestCase):
    """Unit tests for max_area function."""

    def test_basic_cases(self):
        """Test basic cases."""
        self.assertEqual(Solution().max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(Solution().max_area([1, 1]), 1)
        self.assertEqual(Solution().max_area([4, 3, 2, 1, 4]), 16)

    def test_edge_cases(self):
        """Test edge cases."""
        self.assertEqual(Solution().max_area([1]), 0)  # Single height
        self.assertEqual(Solution().max_area([]), 0)  # Empty list

    def test_boundary_cases(self):
        """Test boundary cases."""
        self.assertEqual(Solution().max_area([0, 0, 0, 0]), 0)  # All heights are 0
        self.assertEqual(Solution().max_area([1, 2, 3, 4, 5]), 6)  # Increasing heights
        self.assertEqual(Solution().max_area([5, 4, 3, 2, 1]), 6)  # Decreasing heights

    def test_invalid_input(self):
        """Test invalid input."""
        with self.assertRaises(ValueError):
            Solution().max_area("string")  # Invalid input type
        with self.assertRaises(ValueError):
            Solution().max_area([1, -1, 2])  # Negative heights
        with self.assertRaises(ValueError):
            Solution().max_area([1, "a", 2])  # Non-integer in list


if __name__ == "__main__":
    unittest.main()
