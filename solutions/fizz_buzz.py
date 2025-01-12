"""
This module contains the fizz_buzz function which generates a list 
of numbers from 1 to n with specific substitutions for multiples 
of 3 and/or 5.

The function follows the FizzBuzz rules:
- For multiples of 3, "Fizz" is added.
- For multiples of 5, "Buzz" is added.
- For multiples of both 3 and 5, "FizzBuzz" is added.

Example usage:
>>> fizz_buzz(15)
[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
"""


def fizz_buzz(n: int) -> list:
    """
    Generates a list of numbers from 1 to n with specific rules.

    Parameters:
    n (int): The upper limit of the range (inclusive) to generate.

    Returns:
    list: A list containing the numbers and/or string representations according to the rules.

    Example:
    >>> fizz_buzz(15)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
    >>> fizz_buzz(3)
    [1, 2, 'Fizz']
    >>> fizz_buzz(5)
    [1, 2, 'Fizz', 4, 'Buzz']
    """
    # Defensive assertion to check that n is a positive integer
    assert isinstance(n, int) and n > 0, "Input must be a positive integer"

    results = []  # Initialize an empty list to store the results
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")  # Append "FizzBuzz" for multiples of both 3 and 5
        elif i % 3 == 0:
            results.append("Fizz")  # Append "Fizz" for multiples of 3
        elif i % 5 == 0:
            results.append("Buzz")  # Append "Buzz" for multiples of 5
        else:
            results.append(i)  # Append the number itself if not a multiple of 3 or 5
    return results  # Return the list of results
