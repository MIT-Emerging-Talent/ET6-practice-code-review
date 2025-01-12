"""
The function takes in temperature in degree celsius and
return weather condition based on temperature

Created on Fri Jan 10 2025

@author: Yool Malaak
"""


def get_weather_condition(temperature):
    """
    A module for getting the weather condition
    Module: takes temperature as input and returns weather condition

    parameters:
        temperature (float): The temperature in degrees Celsius.

    Returns:
        str: The weather condition:
            - 'Extremely Hot': 45 <= Temperature <= 50
            - 'Hot': 31 <= Temperature <= 44
            - 'Sunny': 20 <= Temperature <= 30
            - 'Cloudy': 10 <= Temperature <= 19
            - 'Rainy': 0 <= Temperature <= 9
            - 'Freezing': Temperature < 0

    Examples:
        >>> get_weather_condition(47)
        'Extremely Hot'
        >>> get_weather_condition(40)
        'Hot'
        >>> get_weather_condition(25)
        'Sunny'
        >>> get_weather_condition(15)
        'Cloudy'
        >>> get_weather_condition(5)
        'Rainy'
        >>> get_weather_condition(-5)
        'Freezing'
    """
    if 45 <= temperature <= 50:
        return "Extremely Hot"
    elif 31 <= temperature <= 44:
        return "Hot"
    elif 20 <= temperature <= 30:
        return "Sunny"
    elif 10 <= temperature <= 19:
        return "Cloudy"
    elif 0 <= temperature <= 9:
        return "Rainy"
    else:
        return "Freezing"
