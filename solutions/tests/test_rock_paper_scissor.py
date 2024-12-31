"""
Test module for play_round function in the Rock-Paper-Scissors game.
Contains tests for standard cases, edge cases, and defensive assertions.

Test categories:
    - Standard cases: typical user inputs and expected game results
    - Edge cases: empty input, invalid input, and quitting the game
    - Defensive tests: wrong input types, assertions

Created on 31-12-24
Author: Abdulrahman Alsir + Codi
"""

import unittest
import random
from rock_paper_scissor import play_round

class TestRockPaperScissors(unittest.TestCase):
    """Test suite for the play_round function in the Rock-Paper-Scissors game."""

    # Standard test cases
    def test_valid_choices(self):
        """It should return a valid game result for rock, paper, and scissors."""
        valid_choices = ['rock', 'paper', 'scissors']
        for choice in valid_choices:
            with self.subTest(choice=choice):
                result = play_round(choice)
                self.assertIn(result, ['win', 'lose', 'draw'])

    def test_user_wins(self):
        """It should return 'win' when the user plays 'rock' and the computer plays 'scissors'."""
        random.choice = lambda options: 'scissors'  # Mocking computer choice
        result = play_round('rock')
        self.assertEqual(result, 'win')

    def test_user_loses(self):
        """It should return 'lose' when the user plays 'rock' and the computer plays 'paper'."""
        random.choice = lambda options: 'paper'  # Mocking computer choice
        result = play_round('rock')
        self.assertEqual(result, 'lose')

    def test_draw(self):
        """It should return 'draw' when both user and computer play 'scissors'."""
        random.choice = lambda options: 'scissors'  # Mocking computer choice
        result = play_round('scissors')
        self.assertEqual(result, 'draw')

    # Edge cases
    def test_empty_input(self):
        """It should return a valid result for an empty input."""
        result = play_round('')
        self.assertIn(result, ['win', 'lose', 'draw'])

    def test_edge_case_user_quits(self):
        """It should allow the user to quit the game by inputting 'q'."""
        result = play_round('q')
        self.assertEqual(result, 'quit')  # Assuming the quit behavior is implemented

    # Defensive tests
    def test_invalid_input(self):
        """It should handle invalid input and return a valid game result."""
        invalid_input = "invalid_choice"
        result = play_round(invalid_input)
        self.assertIn(result, ['win', 'lose', 'draw'])  # Still returns a valid outcome

    def test_defensive_assertions(self):
        """It should raise an AssertionError for non-string input."""
        with self.assertRaises(AssertionError):
            play_round(123)  # Passing an integer instead of a string

if __name__ == '__main__':
    unittest.main()
