import unittest
from solutions.missing_number import missing_number


class TestMissingNumber(unittest.TestCase):
    """
    Test cases for the `missing_number` function, which finds the missing number
    in an array of distinct integers ranging from 0 to n.
    """

    def test_single_missing_number(self):
        """
        Test a case where the input array has a single missing number.
        Example: Input [3, 0, 1] should return 2.
        """
        self.assertEqual(missing_number([3, 0, 1]), 2)

    def test_missing_last_number(self):
        """
        Test a case where the last number in the range is missing.
        Example: Input [0, 1, 2] should return 3.
        """
        self.assertEqual(missing_number([0, 1, 2]), 3)

    def test_missing_first_number(self):
        """
        Test a case where the first number in the range is missing.
        Example: Input [1, 2] should return 0.
        """
        self.assertEqual(missing_number([1, 2]), 0)

    def test_empty_array(self):
        """
        Test the edge case where the input array is empty.
        Example: Input [] should return 0.
        """
        self.assertEqual(missing_number([]), 0)

    def test_large_array(self):
        """
        Test a case with a larger array to ensure the function works with big inputs.
        Example: Input [0, 1, 3, 4] should return 2.
        """
        self.assertEqual(missing_number([0, 1, 3, 4]), 2)

    def test_single_element_zero(self):
        """
        Test a single-element array where the only element is 0.
        Example: Input [0] should return 1.
        """
        self.assertEqual(missing_number([0]), 1)

    def test_single_element_one(self):
        """
        Test a single-element array where the only element is 1.
        Example: Input [1] should return 0.
        """
        self.assertEqual(missing_number([1]), 0)


if __name__ == "__main__":
    unittest.main()
