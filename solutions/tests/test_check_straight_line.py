"""
Unit tests for the check_straight_line module.
"""

import unittest
from solutions.check_straight_line import Solution


class TestCheckStraightLine(unittest.TestCase):
    """
    Test cases for the Solution class's checkStraightLine method.
    """

    def test_all_points_on_line(self):
        """
        Test that the function correctly identifies points on a straight line.
        """
        solution = Solution()
        coordinates = [[1, 2], [2, 3], [3, 4]]
        self.assertTrue(solution.check_line(coordinates))

    def test_points_not_on_line(self):
        """
        Test that the function correctly identifies points not on a straight line.
        """
        solution = Solution()
        coordinates = [[1, 1], [2, 2], [3, 4]]
        self.assertFalse(solution.check_line(coordinates))

    def test_vertical_line(self):
        """
        Test that the function works for vertical lines.
        """
        solution = Solution()
        coordinates = [[2, 1], [2, 3], [2, 5]]
        self.assertTrue(solution.check_line(coordinates))

    def test_insufficient_points(self):
        """
        Test that the function raises an exception for fewer than two points.
        """
        solution = Solution()
        coordinates = [[1, 1]]
        with self.assertRaises(ValueError):
            solution.check_line(coordinates)

    def test_horizontal_line(self):
        """
        Test that the function works for horizontal lines.
        """
        solution = Solution()
        coordinates = [[1, 2], [3, 2], [5, 2]]
        self.assertTrue(solution.check_line(coordinates))

    def test_boundary_case(self):
        """
        Test that the function handles edge cases for large input ranges.
        """
        solution = Solution()
        coordinates = [[-1000000, -1000000], [0, 0], [1000000, 1000000]]
        self.assertTrue(solution.check_line(coordinates))


if __name__ == "__main__":
    unittest.main()
