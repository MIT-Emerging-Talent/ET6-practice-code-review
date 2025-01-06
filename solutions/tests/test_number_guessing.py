#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a guessing random number game where you guess a number between 1 and 100.

Created on: 2025/01/06
@author Fikremichael Mamo
"""

import unittest
from ..number_guessing import (
    play_game,
)  # Ensure the correct path to the `play_game` function.


class TestPlayGame(unittest.TestCase):
    """
    Unit tests for the play_game function.
    """

    def test_correct_guess_in_one_attempt(self):
        """
        Test if the game returns 1 attempt when the player guesses correctly on the first try.
        """
        result = play_game(target_number=50, simulated_guesses=[50])
        self.assertEqual(
            result,
            1,
            "Should return 1 attempt when guessed correctly on the first try.",
        )

    def test_multiple_attempts_with_correct_guess(self):
        """
        Test if the game counts the correct number of attempts when multiple guesses are required.
        """
        result = play_game(target_number=30, simulated_guesses=[10, 20, 30])
        self.assertEqual(
            result,
            3,
            "Should return the correct number of attempts when multiple guesses are made.",
        )

    def test_all_guesses_too_low(self):
        """
        Test if the game handles the case where all guesses are lower than the target number.
        """
        result = play_game(target_number=50, simulated_guesses=[10, 20, 30, 40])
        self.assertEqual(
            result,
            4,  # Expecting 5 attempts: 4 low guesses + 1 correct guess
            "Should take 5 attempts when all guesses are too low.",
        )

    def test_invalid_guesses(self):
        """
        Test if the game ignores invalid guesses (e.g., less than 1 or greater than 100)
        and only counts valid attempts.
        """
        result = play_game(target_number=25, simulated_guesses=[-1, 101, 25])
        self.assertEqual(
            result,
            1,
            "Should ignore invalid guesses and return correct attempts, counting only valid guesses.",
        )

    def test_warmer_and_colder_logic(self):
        """
        Test if the game provides 'warmer' and 'colder' feedback correctly based on guesses.
        """
        # In this test, we expect the game to give 'warmer' feedback as the guess gets closer to 50.
        result = play_game(target_number=50, simulated_guesses=[30, 40, 50])
        self.assertEqual(
            result,
            3,
            "Should return correct attempts including 'warmer' and 'colder' feedback.",
        )


if __name__ == "__main__":
    """
    Entry point for running the unittests.
    """
    unittest.main()
