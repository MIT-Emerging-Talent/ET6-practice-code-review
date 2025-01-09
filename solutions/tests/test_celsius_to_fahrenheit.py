import unittest
from ..celsius_to_fahrenheit import celsius_to_fahrenheit


class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    Unit tests for the `celsius_to_fahrenheit` function.
    """

    def test_celsius_to_fahrenheit1(self):
        """tests for 50 degree celsius"""
        result = celsius_to_fahrenheit(celsius=50)
        expected_result = 122
        self.assertEqual(result, expected_result)

    def test_celsius_to_fahrenheit2(self):
        """tests for 25 degree celsius"""
        result = celsius_to_fahrenheit(celsius=25)
        expected_result = 77
        self.assertEqual(result, expected_result)

    def test_celsius_to_fahrenheit3(self):
        """tests for 100 degree celsius"""
        result = celsius_to_fahrenheit(celsius=100)
        expected_result = 212
        self.assertEqual(result, expected_result)
