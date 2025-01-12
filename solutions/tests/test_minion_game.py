"""
Unit tests for the minion_game function in the minion_game module.

This module contains a group of test cases to verify the correctness of the
minion_game function, which prints the name and score of the winner of the game.

"""

import unittest
import sys

sys.path.append("../")
from solutions.minion_game import minion_game


class TestMinionGame(unittest.TestCase):
    """
    Unit tests for the minion_game function.
    """

    def test_kevin_wins_with_vowels(self):
        """
        Test if Kevin wins when there are more vowels at the start.
        """
        result = minion_game("aeiou")
        self.assertEqual(result, ("Kevin", 15))

    def test_stuart_wins_with_consonants(self):
        """
        Test if Stuart wins when there are more consonants at the start.
        """
        result = minion_game("banana")
        self.assertEqual(result, ("Stuart", 12))

    def test_draw(self):
        """
        Test if the game results in a draw when scores are equal.
        """

        result = minion_game("BANANANAAAS")
        self.assertEqual(result, "Draw")

    def test_single_character_vowel(self):
        """
        Test if Kevin wins with a single vowel character.
        """
        result = minion_game("a")
        self.assertEqual(result, ("Kevin", 1))

    def test_single_character_consonant(self):
        """
        Test if Stuart wins with a single consonant character.
        """
        result = minion_game("b")
        self.assertEqual(result, ("Stuart", 1))

    def test_empty_string(self):
        """
        Test case for empty input (should raise ValueError).
        """
        with self.assertRaises(ValueError):
            minion_game("")

    def test_numeric_input(self):
        """
        Test case for numeric input (should raise ValueError).
        """
        with self.assertRaises(ValueError):
            minion_game("122343")

    def test_all_vowels(self):
        """
        Test boundary case where the input is all vowels.
        """
        result = minion_game("aeiouaeiou")
        self.assertEqual(result, ("Kevin", 55))

    def test_all_consonants(self):
        """
        Test boundary case where the input is all consonants.
        """
        result = minion_game("bcdfg")
        self.assertEqual(result, ("Stuart", 15))


if __name__ == "__main__":
    unittest.main()
