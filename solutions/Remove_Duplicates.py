"""
A module for removing duplicates from a list of numbers

Module contents: 
  - Remove_Duplicates: Remove any duplicant number in the list

Created on 2025-1-4
@author: Safaa Osman
"""

def Remove_Duplicates(numbers: list) -> list:
  """
  This Function Removes any duplicates elements from the list

  Arguments: list of integeres

  Returns: list of of integers without duplicates

  Raises:
  AssertionError: if the input is not a list
   

  Examples:
  >>> Remove_Duplicates([1,1,2])
  [1, 2]

  >>> Remove_Duplicates([1,2,2,3,3,3])
  [1, 2, 3]

  >>> Remove_Duplicates([1])
  [1]

  >>> Remove_Duplicates([])
  [] 

  >>> Remove_Duplicates([5,5,5,5,5,5,5])
  [5]

  """
  assert isinstance(numbers,list),"input must be a list"

  Final_list = []
  for num in numbers:
    if num not in Final_list:
      Final_list.append(num)
  return Final_list
