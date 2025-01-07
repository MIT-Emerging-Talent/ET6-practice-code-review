"""
This module implements a number guessing game where players select a difficulty
level and attempt to guess a randomly generated number within a limited number of attempts.
The difficulty levels determine the number of attempts allowed.
"""

import random


def choose_difficulty() -> tuple[int, int, str]:
    """
    Prompts the user to select a difficulty level for the game.

    The strategy for this function is to prompt the user for a difficulty level, handle any
    invalid input, and return a randomly generated number within the selected range, the number
    of attempts allowed, and a message indicating the chosen difficulty level.

    Returns:
        tuple[int, int, str]: A tuple containing the randomly generated number,
                the maximum number of attempts allowed, and a message indicating
                the difficulty level selected.
    """
    try:
        # Attempt to read and convert user input to an integer
        choice = int(input("Enter your choice (1-Easy/2-Medium/3-Hard): "))
    except ValueError:
        # Handle invalid input by returning default Medium settings
        return (
            random.randint(1, 50),
            10,
            "Invalid input! Defaulting to Medium (1 to 50) with 10 attempts.",
        )

    # Return settings based on the user's choice
    if choice == 1:
        return random.randint(1, 50), 15, "Easy (1 to 50) - 15 attempts"
    elif choice == 2:
        return random.randint(1, 50), 10, "Medium (1 to 50) - 10 attempts"
    elif choice == 3:
        return random.randint(1, 50), 5, "Hard (1 to 50) - 5 attempts"
    else:
        # Handle invalid choice by returning default Medium settings
        return (
            random.randint(1, 50),
            10,
            "Invalid choice! Defaulting to Medium (1 to 50) with 10 attempts.",
        )


def number_guessing_game() -> list[str]:
    """
    Implements a number guessing game where the player selects a difficulty
    level and attempts to guess the randomly generated number within a
    limited number of attempts.

    The strategy for this function is to:
    1. Display a welcome message and prompt the user to select a difficulty level.
    2. Generate a random number and set the number of attempts based on the chosen difficulty.
    3. Allow the user to make guesses, providing feedback on whether each guess is too high,
    too low, or correct.
    4. Track the number of attempts and end the game either when the user guesses correctly or
    runs out of attempts.

    Returns:
        list[str]: A list of strings representing the game's messages.
    """
    messages = [
        "Welcome to the Number Guessing Game!",
        "Let's choose a difficulty level:",
    ]

    # Choose the difficulty level
    number_to_guess, max_attempts, difficulty_message = choose_difficulty()
    messages.append(difficulty_message)
    attempts = 0
    guessed_correctly = False

    # Loop until the player guesses correctly or runs out of attempts
    while not guessed_correctly and attempts < max_attempts:
        messages.append(f"\nYou have {max_attempts - attempts} attempts left.")
        try:
            # Attempt to read and convert user guess to an integer
            guess = int(input("Make a guess: "))
        except ValueError:
            # Handle invalid input by prompting user again
            messages.append("Invalid input! Please enter a valid number.")
            continue

        attempts += 1

        # Provide feedback based on the user's guess
        if guess < number_to_guess:
            if number_to_guess - guess > 10:
                messages.append("Too low! Try a much higher number.")
            else:
                messages.append("Too low, but you're close!")
        elif guess > number_to_guess:
            if guess - number_to_guess > 10:
                messages.append("Too high! Try a much lower number.")
            else:
                messages.append("Too high, but you're close!")
        else:
            # User guessed correctly
            guessed_correctly = True
            messages.append(
                f"🎉 Congratulations! You guessed the number in {attempts} attempts. 🎉"
            )

    if not guessed_correctly:
        # User ran out of attempts
        messages.append(
            f"You've run out of attempts. The number was {number_to_guess}. Better luck next time!"
        )

    return messages
