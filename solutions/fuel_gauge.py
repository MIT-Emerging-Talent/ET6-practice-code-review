def fuel_gauge(x, y):
    """
    This is a function that calculates the percentage of fuel in a tank.

    Parameters:
    X= fuel in the tank (x value must be less than or equal to y)
    Y= tank capacity (y value must be greater than 0)"""
    if y == 0 or x > y:
        """This is a condition that checks if the tank size is zero or if the fuel is more than the tank capacity."""
        return "Invalid input"

    percentage = (x / y) * 100
    """This is a formula that calculates the percentage of fuel in the tank."""
    if percentage >= 90:
        return "F"
    elif percentage > 10:
        return "M"
    elif percentage <= 10:
        return "E"
    return int(percentage)
