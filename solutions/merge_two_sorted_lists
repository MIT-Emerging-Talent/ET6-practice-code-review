#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 04/01/2025
@author: Peter Ngugi

This module provides a function to merge two sorted lists into one while maintaining sorted order.

Function:
- merge_two_sorted_lists(list1: list, list2: list) -> list: Combines two sorted lists efficiently.
"""
def merge_two_sorted_lists(list1: list, list2: list) -> list:
    """
    Merges two sorted Python lists and returns a single sorted list.
    
    Parameters:
        list1 (list): The first sorted list.
        list2 (list): The second sorted list.

    Returns:
        list: A single sorted list merged from the two input lists.
        
    Examples:
    >>> merge_two_sorted_lists([1, 3, 6], [4, 8, 9])
    [1, 3, 4, 6, 8, 9]
    
    >>> merge_two_sorted_lists([11, 34, 41], [33, 37, 65])
    [11, 33, 34, 37, 41, 65]
    
    >>> merge_two_sorted_lists([], [4, 77, 90])
    [4, 77, 90]
    
    >>> merge_two_sorted_lists([], [])
    []
    """
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError(
            f"Both inputs must be lists, got {type(list1).__name__} and {type(list2).__name__}."
        )
    
    i, j = 0, 0
    merged = []
    
    # Merge while there are elements in both lists
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
            
    # Append any remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    return merged
