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
    Play a number guessing game.

    Args:
        target_number (int, optional): The target number to guess. If None, a random number between 1 and 100 is used.
        simulated_guesses (list of int, optional): A list of simulated guesses to replace user input for testing purposes.

    Returns:
        int: The number of attempts it took to guess the target number correctly.
    """
    if target_number is None:
        target_number = random.randint(1, 100)

    attempts = 0
    previous_guess_diff = None
    guess_index = 0

    # Use simulated guesses if provided, no input from user
    while True:
        if simulated_guesses is not None and guess_index < len(simulated_guesses):
            guess = simulated_guesses[guess_index]
            guess_index += 1
        else:
            # If no simulated guesses are given, the game will not proceed
            print("No more simulated guesses.")
            break

        # Check if the guess is within the allowed range
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        attempts += 1
        guess_diff = abs(guess - target_number)

        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

        if previous_guess_diff is not None:
            if guess_diff < previous_guess_diff:
                print("You're getting warmer!")
            elif guess_diff > previous_guess_diff:
                print("You're getting colder!")
        else:
            print("Start guessing!")

        previous_guess_diff = guess_diff

    return attempts  # Return the number of attempts to facilitate testing
