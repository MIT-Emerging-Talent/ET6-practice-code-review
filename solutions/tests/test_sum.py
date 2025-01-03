import unittest
from solutions.sum import Solution

class TestSolution(unittest.TestCase):
    """
    Test cases for the Solution class, specifically the twoSum method.
    """

    def setUp(self):
        """
        Set up the Solution instance before each test.
        """
        self.solution = Solution()

    def test_two_sum_example(self):
        """
        Test an example case with positive numbers.
        """
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_two_sum_negative_numbers(self):
        """
        Test a case with negative numbers.
        """
        self.assertEqual(self.solution.twoSum([-3, 4, 3, 90], 0), [0, 2])

    def test_two_sum_multiple_solutions(self):
        """
        Test a case with multiple possible solutions.
        """
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 5], 9), [3, 4])

    def test_two_sum_large_numbers(self):
        """
        Test a case with large numbers.
        """
        self.assertEqual(
            self.solution.twoSum([1000000, 500000, -1500000], -1000000), [1, 2]
        )

    def test_two_sum_no_solution(self):
        """
        Test a case where no solution exists.
        """
        self.assertEqual(self.solution.twoSum([1, 2, 3], 7), None)
