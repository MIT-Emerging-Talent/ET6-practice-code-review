#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the common elements between two input lists.

Created on 11/1/2025
@author: Mohamed Altayeb
Group: ET foundations group 16 (Matrix)

Module functions:
    - common_elements: finds the common elements between two lists.

"""


def common_elements(list1: list, list2: list) -> list:
    """
    Compares two input lists and returns a list that contains
    all the common elements between the two input lists without repeating
    the common elements if they are duplicated in the input lists:

    Arguments:
        list1 (list): the first list we want to compare.
        list2 (list): the second list we want to compare.

    Returns-> list: A list containing all common elements between two input lists,
                    the returned list will have the common elements of the first input list
                    followed by the common elements of the second input list.


    Raises:
    AssertionError: if inputs are not lists.

    >>> common_elements([1,2,3,4,5,6] , [4,5,6,7])
    [4, 5, 6]

    >>> common_elements(["c", "a", "r"] , ["c", "a", "t"])
    ['c', 'a']

    >>> common_elements([[1,2] , [2,3,4], ["mohamed"]]  ,  [["mohamed"], [1,2,3], [2,3,4], [4,5,6]])
    [[2, 3, 4], ['mohamed']]
    """
    # Ensure both inputs are lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise AssertionError("Both inputs must be lists")

    common_list_no_duplicates = []

    # Iterate through elements of the first list
    for element1 in list1:
        # Iterate through elements of second list comparing
        # each element in the second list to the element in the first list
        for element2 in list2:
            if element1 == element2 and element1 not in common_list_no_duplicates:
                # Add the element to the resultant list
                common_list_no_duplicates.append(element1)

    # Return the resultant list with common elements with no duplicated elements
    return common_list_no_duplicates
