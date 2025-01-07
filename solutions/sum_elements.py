#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating sum of integers in a given list.

Module contents:
    - sum_elements: A function to calculate the sum of integers in a list. 

Created on 2025-01-06
@author: Rumiya Ismatova
"""

def sum_elements(numbers:list)->int:
    """
    Calculate the sum of all elements in a list.

    Args:
        numbers[int]: A list of integers
        
    Returns: 
        int: the sum of the numbers in the list
        
    >>> sum_elements([1,2,3])
    6

    >>> sum_elements([2,3,3])
    8

    >>> sum_elements([])
    0
    """
    if len(numbers)==0:
        return 0
    

    
    return sum(numbers)



