import unittest

from ..Remove_Duplicates import Remove_Duplicates


class TestRemoveDuplicates(unittest.TestCase):
    """Test the Remove_Duplicates function - some tests are buggy!"""

    def test_empty_list(self):
        """It should return [] for an empty string"""
        self.assertEqual(Remove_Duplicates([]), [])

    def test_no_duplicants(self):
        """It should return the same list for list without duplicants"""
        self.assertEqual(Remove_Duplicates([1, 2, 3]), [1, 2, 3])

    def test_not_list(self):
        """It should raise AssertionError for non-list input"""
        with self.assertRaises(AssertionError):
            Remove_Duplicates("123")
