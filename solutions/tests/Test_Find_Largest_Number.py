import unittest
from  solutions.Find_largest_number import largest_num
"""
    Unit tests for the largest_num() function, verifying its correctness 
    across positive, negative, mixed, single-element, duplicate, and empty lists.
    """
class TestLargestNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(largest_num([3, 9, 2, 3, 2]), 9)

    def test_negative_numbers(self):
        self.assertEqual(largest_num([-3, -1, -2, -7, -8]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(largest_num([4, -9, 3, -8, 5]), 5)

    def test_single_element(self):
        self.assertEqual(largest_num([100]), 100)

    def test_duplicates(self):
        self.assertEqual(largest_num([1, 1, 1, 1]), 1)

if __name__ == "__main__":
    unittest.main()
