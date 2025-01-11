"""
Module for checking if given words or numbers are palindromes.

This module checks a list of strings and numbers to determine if each one
is a palindrome (reads the same forward and backward). The check is done
for multiple inputs using a for loop.

Author: fevziismailsahin
Created: 01/09/2025
"""

strings_to_check = ["Radar", "12321", "Hello", "1.232.1", "12345", "aA", "Test"]

for value in strings_to_check:
    cleaned_value = "".join([char.lower() for char in value if char.isalnum()])

    if cleaned_value == cleaned_value[::-1]:
        print(f"'{value}' is a palindrome.")
    else:
        print(f"'{value}' is not a palindrome.")
