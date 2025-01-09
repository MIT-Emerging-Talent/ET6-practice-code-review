"""
A module for converting temperature from degree celsius to fahrenheit.

@author: Rama Arafeh.
@date: 8/Jan/2025.
"""


def celsius_to_fahrenheit(celsius: int) -> float:
    """
    converts temperature from degree celsius to fahrenheit.

    :param celsius: temperature in degree celsius.
    :return: temperature in fahrenheit.
    :raises ValueError: If the celsius is negative.
    :raises AssertionError: If the argument isn't a number.
    >>> celsius_to_fahrenheit(50)
    122
    >>> celsius_to_fahrenheit(25)
    77
    >>> celsius_to_fahrenheit(100)
    212
    """
    result = (celsius * 9 / 5) + 32
    return result
