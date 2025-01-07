"""
Unit tests for the choose_difficulty function from the number guessing game module.
"""

import os
import sys
import unittest
from unittest.mock import patch

from ..ch1_malak_solution import choose_difficulty, number_guessing_game

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestChooseDifficulty(unittest.TestCase):
    """Unit tests for the `choose_difficulty` function."""

    def test_easy_difficulty(self):
        """Test Easy difficulty with expected range and attempts."""
        with patch("builtins.input", return_value="1"):
            number, attempts, message = choose_difficulty()
            self.assertTrue(1 <= number <= 50)
            self.assertEqual(attempts, 15)
            self.assertEqual(message, "Easy (1 to 50) - 15 attempts")

    def test_medium_difficulty(self):
        """Test Medium difficulty with expected range and attempts."""
        with patch("builtins.input", return_value="2"):
            number, attempts, message = choose_difficulty()
            self.assertTrue(1 <= number <= 50)
            self.assertEqual(attempts, 10)
            self.assertEqual(message, "Medium (1 to 50) - 10 attempts")

    def test_hard_difficulty(self):
        """Test Hard difficulty with expected range and attempts."""
        with patch("builtins.input", return_value="3"):
            number, attempts, message = choose_difficulty()
            self.assertTrue(1 <= number <= 50)
            self.assertEqual(attempts, 5)
            self.assertEqual(message, "Hard (1 to 50) - 5 attempts")

    def test_invalid_input(self):
        """Test defaulting to Medium on invalid input."""
        with patch("builtins.input", side_effect=ValueError):
            number, attempts, message = choose_difficulty()
            self.assertTrue(1 <= number <= 50)
            self.assertEqual(attempts, 10)
            self.assertEqual(
                message,
                "Invalid input! Defaulting to Medium (1 to 50) with 10 attempts.",
            )


class TestNumberGuessingGame(unittest.TestCase):
    """Unit tests for the `number_guessing_game` function."""

    def test_number_guessing_game(self):
        """Test the number_guessing_game function."""
        with patch(
            "builtins.input",
            side_effect=[  # Select Medium difficulty
                "2",
                "25",
                "30",
                "40",
                "50",
                "45",
                "48",
                "50",
                "35",
                "20",
                "15",
                "10",
            ],
        ):
            messages = number_guessing_game()
            self.assertIn("Welcome to the Number Guessing Game!", messages)
            self.assertIn("Let's choose a difficulty level:", messages)
            self.assertIn("Medium (1 to 50) - 10 attempts", messages)
            self.assertIn("\nYou have 10 attempts left.", messages)


if __name__ == "__main__":
    unittest.main()
