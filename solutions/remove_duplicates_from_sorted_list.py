#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: remove_duplicates_from_sorted_list
Description: This module provides a function to remove duplicates from a sorted linked list.
The function ensures each element appears only once while maintaining the sorted order.

Created on: 01 01 25
@author: Muhammad Shahroz
"""

from typing import Optional


class ListNode:
    """A node in a singly linked list."""

    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def remove_duplicates_from_sorted_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Removes duplicates from a sorted linked list.

    Parameters:
        head (Optional[ListNode]): The head node of the sorted linked list.
            - The input is expected to be a valid ListNode or None.
            - The list is assumed to be sorted in non-decreasing order.

    Returns:
        Optional[ListNode]: The head node of the modified linked list with duplicates removed.

    Raises:
        AssertionError: If the argument is not of type ListNode or None.

    Examples:
        >>> head = ListNode(1, ListNode(1, ListNode(2)))
        >>> result = remove_duplicates_from_sorted_list(head)
        >>> [result.value, result.next.value, result.next.next]
        [1, 2, None]

        >>> head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        >>> result = remove_duplicates_from_sorted_list(head)
        >>> [result.value, result.next.value, result.next.next.value]
        [1, 2, 3]

        >>> result = remove_duplicates_from_sorted_list(None)
        >>> result is None
        True

    Example:
        head = ListNode(1, ListNode(1, ListNode(2)))
        result = remove_duplicates_from_sorted_list(head)
        # result is now a list with values: [1, 2]
    """
    # Defensive Assertion
    assert head is None or isinstance(head, ListNode), (
        "Input must be a ListNode or None."
    )

    current_node = head
    while current_node and current_node.next:
        # Traverse the list and remove consecutive duplicates by adjusting pointers.
        if current_node.value == current_node.next.value:
            current_node.next = current_node.next.next  # Skip the duplicate node
        else:
            current_node = current_node.next  # Move to the next unique node

    return head
