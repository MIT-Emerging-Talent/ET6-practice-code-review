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
            num (int): The number to check whether it is prime or not.

        Returns:
            bool: True if the number is prime, False otherwise.

        Example:
            >>> is_prime(29)
            True
            >>> is_prime(36)
            False

        Explanation:
            if num = 29
            num**0.5 is approximately 5.39
            int(num**0.5) gives 5, so we check divisibility from 2 up to 5 + 1 = 6
            We check divisibility by 2, 3, 4, and 5. Since none divide 29, therefore prime.

            if num = 36
            num**0.5 is 6.
            int(num**0.5) gives 6, so we check divisibility from 2 up to 6 + 1 = 7.
            Since 36 is divisible by 2, 3, 4, and 6, therefore 36 is not prime.
        """
        if num < 2:
            return False  # the function returns False because numbers less than 2 are not prime
        for i in range(2, int(num**0.5) + 1):  # num**0.5 calculates square root of num
            # +1 ensures we test all possible divisors from 2 up to the integer square root plus 1.
            if num % i == 0:
                return False  # num is divisible by any number, therefore not prime
        return True  # no divisors are found, the function returns True, indicating that num is prime

    return [num for num in input_list if is_prime(num)]
