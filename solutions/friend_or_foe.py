#!/usr/bin/env python3
"""
This is a function that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
Otherwise, you can be sure he's not...

Examples:
Input = ["Nimo", "Brian", "Joe", "Joan"]
Output = ["Nimo", "Joan"]

Input = ["Ron", "Stephen", "Philip"]
Output = []

Created on 2025-01-04
Author: Cynthia Wairimu
"""


def friend(x):
    """
    Input should be a list containing only strings
    We will be returning names with 4 characters.
    """
    friends = []
    if type(x) is list:  # Assert input is a list
        for name in x:
            if type(name) is str:  # Assert list item is string
                if len(name) == 4:
                    friends.append(name)

        return friends
    else:
        return "Input should be a list of strings"
