"""
Tests for the find_partitions function from the find_partitions.py module
Run with `python3 -m unittest test_find_partition.py`
"""

import unittest


def find_partitions(n, max_num):
    """
    Find all possible partitions of a number `n` using integers from 1 to `max_num`.

    A partition of `n` is a way of writing it as a sum of positive integers, where
    the order of terms doesn't matter. This function returns all unique partitions
    of `n` using numbers from 1 to `max_num`.

    Parameters:
    - n (int): The number to be partitioned.
    - max_num (int): The largest integer that can be used in the partition.

    Returns:
    - list of lists: A list containing all partitions, where each partition is a
      list of integers that sum to `n`. All numbers used are <= `max_num`.
    """
    # Base case: If n is negative or max_num is 0, return an empty list
    if n < 0 or max_num == 0:
        return []

    # Initialize a list for partitions that exactly match n
    exact_match = []

    # If n equals max_num, include the partition [max_num]
    if n == max_num:
        exact_match = [[max_num]]

    # Find partitions that include max_num by subtracting it from n
    with_max_num = [
        partition + [max_num] for partition in find_partitions(n - max_num, max_num)
    ]

    # Find partitions that exclude max_num by reducing max_num
    without_max_num = find_partitions(n, max_num - 1)

    # Return combined partitions: exact matches, with max_num, and without max_num
    return sorted(exact_match) + sorted(with_max_num) + sorted(without_max_num)


# Example usage: Find partitions of 6 using numbers from 1 to 4
print(find_partitions(6, 4))


class TestFindPartitions(unittest.TestCase):
    def compare_unordered_lists(self, list1, list2):
        """
        Compare two lists of lists in an unordered fashion.
        Sort each sublist before comparing the lists themselves.
        """
        # Sort the sublists within both lists
        list1_sorted = [sorted(sublist) for sublist in list1]
        list2_sorted = [sorted(sublist) for sublist in list2]

        # Sort the entire lists to compare unordered contents
        return sorted(list1_sorted) == sorted(list2_sorted)

    def test_partition_basic(self):
        # Test for small basic cases
        result = find_partitions(6, 4)
        expected = [
            [2, 4],
            [1, 1, 4],
            [3, 3],
            [1, 2, 3],
            [1, 1, 1, 3],
            [2, 2, 2],
            [1, 1, 2, 2],
            [1, 1, 1, 1, 2],
            [1, 1, 1, 1, 1, 1],
        ]
        self.assertTrue(self.compare_unordered_lists(result, expected))

    def test_partition_zero(self):
        # Test for partitioning 0 (should return an empty partition)
        self.assertEqual(find_partitions(0, 5), [])

    def test_partition_one(self):
        # Test for partitioning 1 (should return [[1]])
        self.assertEqual(find_partitions(1, 1), [[1]])

    def test_partition_empty_case(self):
        # Test with n = 5 but max_num = 0 (should return an empty list)
        self.assertEqual(find_partitions(5, 0), [])

    def test_partition_negative(self):
        # Test for partitioning a negative number (should return an empty list)
        self.assertEqual(find_partitions(-1, 5), [])

    def test_partition_no_valid_parts(self):
        # Test where n = 3 and max_num = 2 (only partitions using 1 and 2)
        result = find_partitions(3, 2)
        expected = [[2, 1], [1, 1, 1]]
        self.assertTrue(self.compare_unordered_lists(result, expected))


if __name__ == "__main__":
    unittest.main()
