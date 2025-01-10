"""
BMI Calculator

This program helps you calculate your Body Mass Index (BMI). You can enter your
weight, height, and choose either metric (kg/m²) or imperial (lbs/in²) units.
The program will then calculate your BMI and tell you which category you fall into
(Underweight, Normal weight, Overweight, or Obesity).

Functions:
- calculate_bmi: Calculates your BMI based on your input.
- get_user_input: Asks for your weight, height, and unit preference.
- display_bmi_result: Shows your BMI and the category you fall into.
- main: Runs the program and puts everything together.
"""


def calculate_bmi(weight, height, unit="metric"):
    """
    Calculate your Body Mass Index (BMI) and categorize it based on the value.

    Args:
    - weight (float): The weight of the individual in kilograms (for 'metric')
      or pounds (for 'imperial').
    - height (float): The height of the individual in meters (for 'metric')
      or inches (for 'imperial').
    - unit (str): The unit system to use ('metric' for kg/m², 'imperial' for
      lbs/in²). Default is 'metric'.

    Returns:
    - float: The calculated BMI value.
    - str: The category of BMI (e.g., Underweight, Normal weight, Overweight,
      Obesity).
    """
    if unit == "metric":
        bmi = weight / (height**2)
    elif unit == "imperial":
        bmi = (weight * 703) / (height**2)
    else:
        raise ValueError("Oops! The unit must be either 'metric' or 'imperial'.")

    # Categorizing the BMI value
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    return bmi, category


def get_user_input():
    """
    Prompt the user for their weight, height, and unit system.

    This function ensures valid inputs for weight, height, and unit (metric
    or imperial).

    Returns:
    - tuple: A tuple containing:
        - weight (float): The weight entered by the user.
        - height (float): The height entered by the user.
        - unit (str): The unit system chosen ('metric' or 'imperial').
    """
    print("\nLet's calculate your BMI!")

    # Asking the user to select a unit system
    while True:
        unit = (
            input(
                "Please choose your unit system ('metric' for kg/m², "
                "'imperial' for lbs/in²): "
            )
            .strip()
            .lower()
        )

        if unit not in ["metric", "imperial"]:
            print(
                "Oops, it looks like you didn't choose a valid unit. "
                "Please enter either 'metric' or 'imperial'."
            )
            continue
        break

    # Getting valid weight and height from the user
    while True:
        try:
            weight = float(
                input(f"Great! Now, enter your weight in {unit.capitalize()}: ")
            )
            height = float(input(f"Now, enter your height in {unit.capitalize()}: "))

            if weight <= 0 or height <= 0:
                raise ValueError(
                    "Height and weight must be positive numbers. " + "Let's try again!"
                )
            break
        except ValueError as e:
            print(
                f"Oops! Something went wrong. {e} Please enter valid numbers "
                "for both weight and height."
            )
            continue

    return weight, height, unit


def display_bmi_result(bmi, category):
    """
    Display the result in a user-friendly format.

    Args:
    - bmi (float): The calculated BMI.
    - category (str): The BMI category.
    """
    print("\nWell done! You've calculated your BMI.")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Based on your BMI, you fall into the following category: {category}.\n")


def main():
    """
    Main function to calculate and display the BMI result.

    This function integrates all other functions to:
    - Get user input for weight, height, and unit.
    - Calculate the BMI.
    - Display the result.
    """
    print(
        "Welcome to the BMI Calculator! We'll help you determine your Body "
        "Mass Index (BMI)."
    )

    # Get user input for weight, height, and unit system
    weight, height, unit = get_user_input()

    # Calculate BMI and determine the category
    bmi, category = calculate_bmi(weight, height, unit)

    # Display the results to the user
    display_bmi_result(bmi, category)


# Running the main function when the script is executed
if __name__ == "__main__":
    main()
