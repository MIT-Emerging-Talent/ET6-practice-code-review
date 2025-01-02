#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for Lowest Common Ancestor in Binary search tree function.

"""

import unittest


class TreeNode:
    """Define class for TreeNode"""

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TestLowestCommonAncestor(unittest.TestCase):
    """Test the Lowest common Ancestor in Binary search tree function
    Binary Search Tree structure:
    
         5
       /   \
      3     8
     / \   / \
    1   4 7   9
     \
      2

    """


def setUp_BTS(self):
    "create Binary search tree from the example"
    self.root = TreeNode(5)
    self.root.left = TreeNode(3)
    self.root.right = TreeNode(8)
    self.root.left.left = TreeNode(1)
    self.root.left.right = TreeNode(4)
    self.root.right.left = TreeNode(7)
    self.root.right.right = TreeNode(9)
    self.root.left.left.right = TreeNode(2)


def test_case_1(self):
    "This test case 1"
