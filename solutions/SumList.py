"""
Author: @arvidon
Created on: jan 7 2025.
"""


def SumList(numbers):
    """
    The SumList function takes a list of numbers as input and returns the sum of all the elements in the list.
    It utilizes Python's built-in sum() function to calculate the sum of the numbers.

    PARAMETERS:
    numbers (List of int or float): A list containing numerical values (either integers or floating-point numbers)
    that need to be summed up.

    RETURN VALUES:
    int or float: The sum of the values in the numbers list. The return type will depend on the types of numbers in the list.
    """
    # Return the sum of all numbers in the list
    return sum(numbers)


# Example usage
numbers = [1, 2, 3, 4, 5]
result = SumList(numbers)
print(f"The sum of the list is: {result}")
