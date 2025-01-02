#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX
@author: Saadet Kalender
"""
def find_smallest_number(numbers):
    """
    Finds and returns the smallest number in a list.
    
    :param numbers: List of numbers
    :return: The smallest number in the list
    """
    if not numbers:
        raise ValueError("The list is empty.")
    
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

# Example usage
numbers = [34, 2, 56, -3, 99, 0]
print("The smallest number is:", find_smallest_number(numbers))
