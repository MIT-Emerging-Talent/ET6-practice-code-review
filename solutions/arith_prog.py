"""
A module that that generates an arithmetic progression (AP). 

Module contents:
  - generate_arithmetic_progression generates an arithmetic progression

Created on 11/25/2024
@author: Anik Kumar Adhikary
"""
def generate_arithmetic_progression(start, difference, terms):
    """
    It generates an arithmetic progression given a start value,
    a difference, and the number of terms. 

    Parameters:
    - start (int/float): The first term of the AP.
    - difference (int/float): The common difference between terms.
    - terms (int): The number of terms to generate.
    
    Returns:
    - list: A list containing the arithmetic progression

    Example:
    >>> generate_arithmetic_progression(2, 3, 5)
    [2,5,8,11,14]

    Explanation:
    start = 2

    difference = 3

    terms = 5

    The range generates the sequence 0, 1, 2, 3, 4.

    For each value of i, we calculate start + i * difference:

    For i = 0: 2 + 0 * 3 = 2
    For i = 1: 2 + 1 * 3 = 5
    For i = 2: 2 + 2 * 3 = 8
    For i = 3: 2 + 3 * 3 = 11
    For i = 4: 2 + 4 * 3 = 14

    The result is [2, 5, 8, 11, 14], and this is returned by the function
    """
    # A concise way to create a list in Python
    return [start + i * difference for i in range(terms)]
# Expression: start + i * difference; gives the value of the nth term, starting from the first term
# Iteration: for i in range(terms); generates a sequence of numbers from 0 to terms-1
