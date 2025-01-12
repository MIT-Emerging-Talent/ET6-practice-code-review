def calculate_bmi(weight, height):
    """
    This function calculates the Body Mass Index (BMI) based on weight (in kilograms)
    and height (in meters).
    :param weight: float
    :param height: float
    :return: str
    """
    if height <= 0 or weight <= 0:
        return "Invalid input. Height and weight must be greater than zero."

    bmi = weight / (height**2)

    if bmi < 18.5:
        return f"Underweight (BMI: {bmi:.2f})"
    elif 18.5 <= bmi < 24.9:
        return f"Normal weight (BMI: {bmi:.2f})"
    elif 25 <= bmi < 29.9:
        return f"Overweight (BMI: {bmi:.2f})"
    else:
        return f"Obesity (BMI: {bmi:.2f})"
