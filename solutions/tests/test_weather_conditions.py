"""Test module for input temperature
This unittest contains test
and edge cases for the weather condition

Created on Sat Jan 10 2025

@author: Yool Malaak
"""

import unittest

from ..weather_conditions import get_weather_condition


class TestGetWeatherCondition(unittest.TestCase):
    """
    Unit tests for the `get_weather_condition` function, which determines
    weather conditions based on temperature in Celsius.
    """

    def test_extremely_hot(self):
        """
        Test for temperatures in the 'Extremely Hot' range (45-50°C).
        """
        self.assertEqual(get_weather_condition(45), "Extremely Hot")
        self.assertEqual(get_weather_condition(50), "Extremely Hot")

    def test_hot(self):
        """
        Test for temperatures in the 'Hot' range (31-44°C).
        """
        self.assertEqual(get_weather_condition(40), "Hot")
        self.assertEqual(get_weather_condition(31), "Hot")

    def test_sunny(self):
        """
        Test for temperatures in the 'Sunny' range (20-30°C).
        """
        self.assertEqual(get_weather_condition(25), "Sunny")
        self.assertEqual(get_weather_condition(20), "Sunny")

    def test_cloudy(self):
        """
        Test for temperatures in the 'Cloudy' range (10-19°C).
        """
        self.assertEqual(get_weather_condition(15), "Cloudy")
        self.assertEqual(get_weather_condition(10), "Cloudy")

    def test_rainy(self):
        """
        Test for temperatures in the 'Rainy' range (0-9°C).
        """
        self.assertEqual(get_weather_condition(5), "Rainy")
        self.assertEqual(get_weather_condition(0), "Rainy")

    def test_freezing(self):
        """
        Test for temperatures in the 'Freezing' range (below 0°C).
        """
        self.assertEqual(get_weather_condition(-5), "Freezing")
        self.assertEqual(get_weather_condition(-10), "Freezing")
