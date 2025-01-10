# prime_filter_challenge

import math


def filter_primes(numbers: list[int]) -> list[int]:
    """
    Filters out all non-prime numbers from a given list of integers.

    Args:
        numbers (list of int): A list of integers to be processed.

    Returns:
        list of int: A new list containing only the prime numbers, maintaining the original order.

    Example:
        >>> filter_primes([2, 3, 4, 5, 6, 7])
        [2, 3, 5, 7]

        >>> filter_primes([10, 15, 17, 19, 20])
        [17, 19]

    Raises:
        TypeError: If the input is not a list of integers.
        ValueError: If the list contains a non-integer element.
    """

    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    if not all(isinstance(i, int) for i in numbers):
        raise ValueError("All elements in the list must be integers.")

    def is_prime(n):
        """Helper function to check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]
