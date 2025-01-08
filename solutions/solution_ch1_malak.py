"""
This module implements a number guessing game where players select a difficulty
level and attempt to guess a randomly generated number within a limited number of attempts.
The difficulty levels determine the number of attempts allowed.
"""

import random


def choose_difficulty() -> tuple[int, int, str]:
    """
    Prompts the user to select a difficulty level for the game.

    Returns:
        tuple[int, int, str]: A tuple containing the randomly generated number,
                the maximum number of attempts allowed, and a message indicating
                the difficulty level selected.
    """
    try:
        choice = int(input("Enter your choice (1-Easy/2-Medium/3-Hard): "))
    except ValueError:
        return (
            random.randint(1, 50),
            10,
            "Invalid input! Defaulting to Medium (1 to 50) with 10 attempts.",
        )

    if choice == 1:
        return random.randint(1, 50), 15, "Easy (1 to 50) - 15 attempts"
    elif choice == 2:
        return random.randint(1, 50), 10, "Medium (1 to 50) - 10 attempts"
    elif choice == 3:
        return random.randint(1, 50), 5, "Hard (1 to 50) - 5 attempts"
    else:
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

    while not guessed_correctly and attempts < max_attempts:
        messages.append(f"\nYou have {max_attempts - attempts} attempts left.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            messages.append("Invalid input! Please enter a valid number.")
            continue

        attempts += 1

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
            guessed_correctly = True
            messages.append(
                f"🎉 Congratulations! You guessed the number in {attempts} attempts. 🎉"
            )

    if not guessed_correctly:
        messages.append(
            f"You've run out of attempts. The number was {number_to_guess}. Better luck next time!"
        )

    return messages


if __name__ == "__main__":
    game_messages = number_guessing_game()
    for message in game_messages:
        print(message)
