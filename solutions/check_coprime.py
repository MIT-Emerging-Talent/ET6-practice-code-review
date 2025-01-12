"""Module to check if two numbers are relatively prime.

This module defines a function to determine whether two numbers (Integer) are relatively
prime, meaning they have no common factors than 1.

@author: Vahab
@Created: 11/01/2025
"""


def check_coprime(first_integer: int, second_integer: int) -> bool:
    """Check if two numbers are relatively prime.

        Two numbers are relatively prime when there
        are no common factors other than 1

        Parameters:
            first_integer (int): The first number (must be a positive integer).
            second_integer (int): The second number (must be a positive integer).


        Returns:
            bool: True if the numbers are relatively prime, False otherwise.

        Raises:
            ValueError: If either of the inputs is not a positive integer.
            TypeError: If either of the inputs is not an integer.

    >>> check_coprime(15, 28)
    True
    >>> check_coprime(8, 12)
    False
    >>> check_coprime(7, 9)
    True
    """

    # Check if inputs are integers
    if not isinstance(first_integer, int) or not isinstance(second_integer, int):
        raise TypeError("Both inputs must be integers.")

    # Check if inputs are positive integers
    if first_integer <= 0 or second_integer <= 0:
        raise ValueError("Both numbers must be positive integers.")

    # Find the smaller of the two numbers
    smaller = min(first_integer, second_integer)

    # Check for any common factors greater than 1
    for i in range(2, smaller + 1):
        if first_integer % i == 0 and second_integer % i == 0:
            return False

    return True
