"""This function check number for prime or not.

Author: Özgür ÖZBEK
Date: 11th January 2025
Group: ET6-foundations-group-16
"""


def is_prime(number):
    """
    Check if a number is prime.

    Parameters:
    - number (int): The number to check.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False  # Numbers 1 and smaller are not prime
    for i in range(2, number):
        if number % i == 0:  # If a divisor is found, it is not prime
            return False
    return True  # If it has no divisors, it is a prime number


num = 14  # pylint: disable=invalid-name
print(f"Is {num} prime? {is_prime(num)}")
