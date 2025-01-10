"""

class tests the function that takes in a string and two lists of strings
and checks if the str is in _only one_ of the lists.

"""

import unittest

from ..only_in_one_list import only_in_one_list


class TestOnlyinOneList(unittest.TestCase):
    """Tests the only_in_one_list function"""

    def test_arg_a_type(self):
        """returns True if assertion error is raised when arg a is not list"""
        with self.assertRaises(AssertionError):
            only_in_one_list("cap", [8, 9], "well")

    def test_arg_b_type(self):
        """returns True if assertion error is raised when arg b is not list"""
        with self.assertRaises(AssertionError):
            only_in_one_list(["cap"], 8, "well")

    def test_arg_c_type(self):
        """returns True if assertion error is raised when arg c is not str"""
        with self.assertRaises(AssertionError):
            only_in_one_list(["cap"], ["hat"], ["well"])

    def test_item_in_both_list(self):
        """return false if item is found in both list"""
        self.assertEqual(only_in_one_list(["i", "j", "k"], ["k", "l", "m"], "k"), False)

    def test_item_not_in_lists(self):
        """return false if item is not in both list"""
        self.assertEqual(only_in_one_list(["i", "j"], ["l", "m"], "k"), False)

    def test_item_in_one_list(self):
        """return true if item is in oneof the list"""
        self.assertEqual(only_in_one_list(["i", "j", "k"], ["l", "m"], "k"), True)
