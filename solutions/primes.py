"""
A module to filter prime numbers from a list

Module contents:
    - find_primes_in_list function takes a list of integers as input
    - is_prime determines if a number is prime

Created on 12/25/2024
@author: Anik Kumar Adhikary
"""
def find_primes_in_list(input_list):
    """
    Filters out and returns the prime numbers from the provided input list.
    
    Args:
        input_list (list): A list of integers to be checked for primality.

    Returns:
        list: A list of integers from the input list that are prime numbers.

    Example:
        >>> find_primes_in_list([2, 3, 4, 5, 6, 7])
        [2, 3, 5, 7]
    """
    def is_prime(num):
        """
        Checks if a number is prime.

        Args:
            num (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.

        Example:
            >>> is_prime(5)
            True
            >>> is_prime(4)
            False
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in input_list if is_prime(num)]
