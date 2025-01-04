def get_weather_forecast(city):
    """
    Simulates fetching weather forecast for a city.
    """
    forecast_data = {
        "Pathein": {"temperature": 7, "condition": "Cloudy"},
        "Yangon": {"temperature": 20, "condition": "Sunny"},
        "Mandalay": {"temperature": -1, "condition": "Snowy"},
        "Bagan": {"temperature": 15, "condition": "Rainy"},
    }

    return forecast_data.get(city, None)


def display_forecast(city):
    """
    Displays the weather forecast for the given city.
    """
    forecast = get_weather_forecast(city)
    if forecast:
        print(f"Weather forecast for {city}:")
        print(f"Temperature: {forecast['temperature']}°C")
        print(f"Condition: {forecast['condition']}")
    else:
        print(f"Sorry, we don't have weather data for {city}.")


def main():
    print("Welcome to the Weather Forecast System!")
    city = input("Enter the city name: ").strip()
    display_forecast(city)


if __name__ == "__main__":
    main()
