#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the remove_duplicates_from_sorted_list function.

Created on: XX XX XX
@author: Your Name
"""

import unittest
from ..remove_duplicates_from_sorted_list import ListNode, remove_duplicates


class TestRemoveDuplicatesFromSortedList(unittest.TestCase):
    """
    Unit tests for the remove_duplicates function.
    Ensures that duplicates are removed from a sorted linked list.
    """

    def test_empty_list(self):
        """It should evaluate None to None."""
        self.assertIsNone(remove_duplicates(None))

    def test_single_node(self):
        """It should evaluate a single-node list as unchanged."""
        head = ListNode(1)
        result = remove_duplicates(head)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)

    def test_list_with_duplicates(self):
        """It should remove duplicates from a sorted linked list."""
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        result = remove_duplicates(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertIsNone(result.next.next.next)

    def test_list_without_duplicates(self):
        """It should evaluate a list with no duplicates as unchanged."""
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = remove_duplicates(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertIsNone(result.next.next.next)

    def test_invalid_input(self):
        """It should raise an assertion error for invalid input."""
        with self.assertRaises(AssertionError):
            remove_duplicates("invalid_input")


if __name__ == "__main__":
    unittest.main()
