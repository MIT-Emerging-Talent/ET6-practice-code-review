def convert_temperature(celsius):
    """
    Convert temperature from Celsius to Fahrenheit and Kelvin.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        dict: A dictionary containing the temperature in Fahrenheit and Kelvin.

    Raises:
        ValueError: If the input is not a valid number or is below absolute zero.

    Examples:
        >>> convert_temperature(0)
        {'Fahrenheit': 32.0, 'Kelvin': 273.15}
        >>> convert_temperature(-273.15)
        {'Fahrenheit': -459.67, 'Kelvin': 0.0}
        >>> convert_temperature(100)
        {'Fahrenheit': 212.0, 'Kelvin': 373.15}
        >>> convert_temperature(-300)  # Below absolute zero
        Traceback (most recent call last):
        ValueError: Temperature cannot be below absolute zero (-273.15°C).
    """
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")

    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15

    return {"Fahrenheit": round(fahrenheit, 2), "Kelvin": round(kelvin, 2)}


def main():
    print("Welcome to the Temperature Converter!")
    try:
        user_input = input("Enter a temperature in Celsius: ")
        celsius = float(user_input)
        result = convert_temperature(celsius)
        print(f"The temperature in Fahrenheit is {result['Fahrenheit']}°F.")
        print(f"The temperature in Kelvin is {result['Kelvin']}K.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()  # Run doctests
    main()  # Run the main function for user interaction
