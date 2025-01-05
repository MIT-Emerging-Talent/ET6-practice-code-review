#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test the friend function
Test categories:
    - Standard case: A list of with two friends and one with no friends
    - Edge Case: Test if it will work with non-list input
    
Created on 2025-01-04
Author: Cynthia Wairimu
"""
import unittest
from friend_or_foe import friend


class TestFriendOrFoe(unittest.TestCase):
    def test_two_friends(self):
        result = friend(["Nimo", "Brian", "Joe", "Joan"])
        print(f"Result for test_two_friends: {result}")
        self.assertEqual(result, ["Nimo", "Joan"])

    def test_no_friend(self):
        result = friend(["Ron", "Brian", "Sixisveryfunny", "name4"])
        print(f"Result for test_no_friend: {result}")
        self.assertEqual(result, [])

    def test_not_list(self):
        result = friend("Four")
        print(f"Result for test_no_list: {result}")
        self.assertEqual(result, "Input should be a list of strings")
