#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  A module for a function that performs binary search on a sorted list.

Module contents:
    - binary_search: Performs binary search on a sorted list.

Created on 2024-12-27
Author: Awaab98"""

from typing import List, Union

def binary_search(list_to_be_searched: List[Union[int, float, str]], target_element: Union[int, float, str]) -> int:
  """Performs binary search on a sorted list. 
  
  Parameters:
      list_to_be_searched: int, float, str: A sorted list in ascending order to be searched.
      target_element: int, float, str: The element to be searched for in the list.

  Returns:
      int: The index of the target element in the list if it is found, -1 otherwise.
      
  Raises:
      TypeError: If the first argument is not a list.
      TypeError: If the list is not a list of integers, floats or strings.
      TypeError: If the second argument is not an integer, float or string.
      ValueError: If the list is empty.
      AssertionError: If the list is not sorted in ascending order.
      
  Examples:
      >>> binary_search([1, 2, 3, 4, 5], 3)
      2
      >>> binary_search([1, 2, 3, 4, 5], 6)
      -1
      >>> binary_search([1.0, 2.0, 3.0, 4.0, 5.0], 3.0)
      2
      >>> binary_search(['a', 'b', 'c', 'd', 'e'], 'c')
      2
      >>> binary_search(['a', 'b', 'c', 'd', 'e'], 'f')
      -1
  """
  
  
