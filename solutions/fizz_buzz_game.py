"""
A module for a game called FizzBuzz.
Module contents:
    - fizz_buzz: generates a list of strings (Fizz, Buzz, or FizzBuzz)
    "Fizz" when a number is divisible by 3,
     "Buzz" if the number is divisible by 5,
     and FizzBuzz if the number is divisible by both
Created on 31-12-24
@author: Abdulrahman Ali + Cody
"""


def fizz_buzz(start: int, end: int) -> list:
    """
    Generate a list for the FizzBuzz Game.

    Strategy:
        The function iterates through each number in the range [start, end).
        For each number:
            - If divisible by 15 (both 3 and 5), append "FizzBuzz".
            - Else, if divisible by 3, append "Fizz".
            - Else, if divisible by 5, append "Buzz".
            - Otherwise, skip the number.

    Parameters:
        start (int): Start of the range of numbers (included).
        end (int): End of the range of numbers (excluded).

    Returns:
        list: A list containing "Fizz", "Buzz", or "FizzBuzz" based on divisibility
        conditions. Numbers divisible by neither 3 nor 5 are excluded.

    Raises:
        AssertionError: If start or end is not an integer or if start > end.

    Examples:
        >>> fizz_buzz(2, 10)
        ['Fizz', 'Buzz', 'Fizz', 'Fizz']
        >>> fizz_buzz(10, 16)
        ['Buzz', 'Fizz', 'FizzBuzz']
        >>> fizz_buzz(7, 9)
        []
    """
    # Checking for invalid input
    if not isinstance(start, int) or not isinstance(end, int):
        raise AssertionError("start and end must be integers")
    if start > end:
        raise AssertionError("start must be less than or equal to end")

    # Generating the FizzBuzz list
    result = []
    for number in range(start, end):
        if number % 15 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
    return result
