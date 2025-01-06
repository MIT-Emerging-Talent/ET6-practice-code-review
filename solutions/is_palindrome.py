"""
Created on 04/01/2025

@author: Tibyan Khalid
"""


def is_palindrome(string):
    """is_palindrome will return whether the entry given is a palindrome or not.
    Palindrome: a word whose reverse is the same as the original word.

     Parameters:
      string(str): the word to be checked

     Returns: string(str) "whether the word is palindrome or not"

     >>> is_palindrome("radar")
     Palindrome

     >>> is_palindrome("hey")
     Not Palindrome
    """
    # argument must be a string
    assert isinstance(string, (str))

    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
