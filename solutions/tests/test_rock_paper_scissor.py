"""
Test module for play_round function in the Rock-Paper-Scissors game.
Contains tests for standard cases, edge cases, and defensive assertions.

Created on 31-12-24
Author: Abdulrahman Alsir + Cody
"""

import unittest
import random
from ..rock_paper_scissor import play_round


class TestPlayRound(unittest.TestCase):
    """Test suite for the play_round function in the Rock-Paper-Scissors game."""

    def test_rock(self):
        """Test user input 'rock' against various computer picks."""
        random.choice = lambda options: "scissors"
        self.assertEqual(play_round("rock"), "win")

    def test_paper(self):
        """Test user input 'paper' against various computer picks."""
        random.choice = lambda options: "rock"
        self.assertEqual(play_round("paper"), "win")

    def test_scissors(self):
        """Test user input 'scissors' against various computer picks."""
        random.choice = lambda options: "paper"
        self.assertEqual(play_round("scissors"), "win")

    def test_draw(self):
        """Test that the game results in a draw when both play the same."""
        random.choice = lambda options: "rock"
        self.assertEqual(play_round("rock"), "draw")

    def test_case_insensitivity(self):
        """Test that the function handles case insensitivity."""
        random.choice = lambda options: "rock"
        self.assertEqual(play_round("RoCk"), "draw")

    def test_whitespace_handling(self):
        """Test that the function handles leading/trailing whitespace."""
        random.choice = lambda options: "rock"
        self.assertEqual(play_round(" rock "), "draw")

    def test_empty_input(self):
        """Test that an empty input raises an AssertionError."""
        with self.assertRaises(AssertionError):
            play_round("")

    def test_invalid_input(self):
        """Test that invalid input raises a ValueError."""
        with self.assertRaises(ValueError):
            play_round("invalid_choice")


if __name__ == "__main__":
    unittest.main()
