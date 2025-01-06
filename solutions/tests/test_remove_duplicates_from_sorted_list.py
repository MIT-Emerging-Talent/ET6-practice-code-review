#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the remove_duplicates_from_sorted_list function.

Created on:  01 01 25
@author: Muhammad Shahroz
"""

import unittest
from ..remove_duplicates_from_sorted_list import (
    ListNode,
    remove_duplicates_from_sorted_list,
)


class TestRemoveDuplicatesFromSortedList(unittest.TestCase):
    """
    Unit tests for the remove_duplicates_from_sorted_list function.
    Ensures that duplicates are removed from a sorted linked list.
    """

    def test_empty_list(self):
        """It should evaluate None to None."""
        result = remove_duplicates_from_sorted_list(None)
        self.assertIsNone(result)

    def test_single_node_value(self):
        """It should evaluate the value of a single-node list."""
        head = ListNode(1)
        result = remove_duplicates_from_sorted_list(head)
        self.assertEqual(result.value, 1)

    def test_single_node_next(self):
        """It should evaluate the next node of a single-node list as None."""
        head = ListNode(1)
        result = remove_duplicates_from_sorted_list(head)
        self.assertIsNone(result.next)

    def test_duplicate_first_node(self):
        """It should remove duplicates at the first node."""
        head = ListNode(1, ListNode(1, ListNode(2)))
        result = remove_duplicates_from_sorted_list(head)
        self.assertEqual(result.value, 1)

    def test_duplicate_second_node(self):
        """It should remove duplicates at the second node."""
        head = ListNode(1, ListNode(1, ListNode(2)))
        result = remove_duplicates_from_sorted_list(head)
        self.assertEqual(result.next.value, 2)

    def test_duplicate_list_ends(self):
        """It should remove duplicates at the end of the list."""
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        result = remove_duplicates_from_sorted_list(head)
        self.assertIsNone(result.next.next.next)

    def test_list_without_duplicates_first_node(self):
        """It should evaluate the first node of a list without duplicates."""
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = remove_duplicates_from_sorted_list(head)
        self.assertEqual(result.value, 1)

    def test_list_without_duplicates_second_node(self):
        """It should evaluate the second node of a list without duplicates."""
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = remove_duplicates_from_sorted_list(head)
        self.assertEqual(result.next.value, 2)

    def test_list_without_duplicates_third_node(self):
        """It should evaluate the third node of a list without duplicates."""
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = remove_duplicates_from_sorted_list(head)
        self.assertEqual(result.next.next.value, 3)

    def test_invalid_input(self):
        """It should raise an assertion error for invalid input."""
        with self.assertRaises(AssertionError):
            remove_duplicates_from_sorted_list("invalid_input")


if __name__ == "__main__":
    unittest.main()
