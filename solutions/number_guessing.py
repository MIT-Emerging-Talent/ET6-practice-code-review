#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a guessing random number game where you guess a number between 1 and 100.

Created on: 2025/01/06
@author Fikremichael Mamo
"""

import random


def play_game(target_number=None, simulated_guesses=None):
    """
    Play a number guessing game where the player tries to guess a number between 1 and 100.

    Args:
        target_number (int, optional): The target number to guess. If None, a random number between 1 and 100 is used.
        simulated_guesses (list of int, optional): A list of simulated guesses to replace user input for testing purposes.

    Returns:
        int: The number of attempts it took to guess the target number correctly.

    Game Rules:
    - Players must guess numbers between 1 and 100.
    - The game provides feedback ("Too low", "Too high", "You're getting warmer", "You're getting colder") based on the guesses.
    - The game ends when the correct number is guessed.
    """

    # If no target number is provided, generate a random number between 1 and 100
    if target_number is None:
        target_number = random.randint(1, 100)

    attempts = 0  # Keep track of the number of attempts
    previous_guess_diff = None  # Store the difference from the previous guess for "warmer" and "colder" feedback
    guess_index = 0  # Track the index for simulated guesses (if provided)

    while True:
        # If there are simulated guesses, use them; otherwise, ask for user input
        if simulated_guesses is not None and guess_index < len(simulated_guesses):
            guess = simulated_guesses[guess_index]
            guess_index += 1
        else:
            guess = int(input("Enter your guess: "))

        # Ensure the guess is between 1 and 100
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        attempts += 1  # Increment the attempt counter
        guess_diff = abs(
            guess - target_number
        )  # Calculate the absolute difference from the target number

        # Provide feedback based on whether the guess was too low or too high
        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break  # Exit the loop once the correct number is guessed

        # Compare the current guess with the previous one to give "warmer" or "colder" feedback
        if previous_guess_diff is not None:
            if guess_diff < previous_guess_diff:
                print("You're getting warmer!")
            elif guess_diff > previous_guess_diff:
                print("You're getting colder!")
        else:
            print("Start guessing!")

        previous_guess_diff = guess_diff  # Update the previous guess difference

    return attempts  # Return the number of attempts to facilitate testing


if __name__ == "__main__":
    """
    Entry point for running the game interactively.
    
    Continuously runs the game and prompts the user to play again after each round.
    """
    while True:
        play_game()  # Run the game
        play_again = input(
            "Do you want to play again? (yes/no): "
        ).lower()  # Ask the user if they want to play again
        if play_again != "yes":
            print(
                "Thanks for playing!"
            )  # Exit the loop if the user doesn't want to play again
            break
