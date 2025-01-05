"""
A module for playing a game of Rock-Paper-Scissors.

Module contents:
    - play_round: plays a round of Rock-Paper-Scissors, the user either wins,
    loses, or draws based on the user's choice and the computer's choice.

Created on 31-12-24
@author: Abdulrahman Ali (Reviewed by Cody)
"""

import random

options = ["rock", "paper", "scissors"]


def play_round(user_input: str) -> str:
    """
    Allows the user to play a round of Rock-Paper-Scissors with the computer.

    Parameters:
        user_input (str): The user's move ('rock', 'paper', or 'scissors').

    Returns:
        str: The result of the round ('win', 'lose', or 'draw').

    Raises:
        AssertionError: If user_input is not a string or is empty.
        ValueError: If user_input is not one of the valid options.

    Examples:
        >>> play_round('rock')  # doctest: +SKIP
        'win'  # User plays rock, and the computer picks scissors.

        >>> play_round('paper')  # doctest: +SKIP
        'lose'  # User plays paper, and the computer picks scissors.

        >>> play_round('scissors')  # doctest: +SKIP
        'draw'  # User plays scissors, and the computer picks scissors.

        >>> play_round('invalid')
        Traceback (most recent call last):
        ...
        ValueError: Invalid input. Choose one of: rock, paper, scissors.

    Strategy:
        1. Validate the user input to ensure it is a non-empty string and one of the valid options.
        2. Randomly select a move for the computer from the available options.
        3. Compare the user's move with the computer's move to determine the result:
            - If both moves are the same, return "draw".
            - If the user wins, return "win".
            - If the user loses, return "lose".
    """
    assert (
        isinstance(user_input, str) and user_input.strip()
    ), "Input must be a non-empty string."

    user_input = user_input.strip().lower()
    if user_input not in options:
        raise ValueError(f"Invalid input. Choose one of: {', '.join(options)}.")

    computer_pick = random.choice(options)
    if user_input == computer_pick:
        return "draw"
    elif (
        (user_input == "rock" and computer_pick == "scissors")
        or (user_input == "paper" and computer_pick == "rock")
        or (user_input == "scissors" and computer_pick == "paper")
    ):
        return "win"
    else:
        return "lose"
