import unittest

from ..filter_list import filter_list

class TestFilterList(unittest.TestCase):
    def test_mixed_list(self):
        """return a list of integers from a mixed list of integers and strings."""
        actual = filter_list([1, 2, 'a', 'b', 32, 21])
        expected = [1, 2, 32, 21]
        self.assertEqual(actual, expected)

    def test_integers_and_strings(self):
        """return a list of integers when both integers and strings are present."""
        actual = filter_list([1, 72, 'a', 'b', 0, 15])
        expected = [1, 72, 0, 15]
        self.assertEqual(actual, expected)

    def test_strings_and_integers(self):
        """filter out all strings and return only integers."""
        actual = filter_list([1, 2, 'aasf', '1', '123', 123, 'wuor'])
        expected = [1, 2, 123]
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """return an empty list when input is an empty list."""
        actual = filter_list([])
        expected = []
        self.assertEqual(actual, expected)

    def test_all_strings(self):
        """return an empty list when input contains only strings."""
        actual = filter_list(['a', 'b', 'c', 'bhang'])
        expected = []
        self.assertEqual(actual, expected)

    def test_all_integers(self):
        """return the same list when input contains only integers."""
        actual = filter_list([0, 1, 2, 3, 4, 5, 6, 7, 8])
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(actual, expected)