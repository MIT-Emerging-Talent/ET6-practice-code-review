def fuel_gauge(x, y):
    """ """
    if y == 0 or x > y:
        raise ValueError(
            "Invalid input: y must be greater than 0 (tank size can't be zero) and x must be less than or equal to y(fuel can't be more than the tank capacity)."
        )

    percentage = (x / y) * 100
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    return int(percentage)
