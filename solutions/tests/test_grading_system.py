#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for grading_system function

Test categories:
    -Standard test: Tests for typical inputs and expected outputs.
    - Edge test: Tests for boundary conditions and extreme inputs.
    - Defensive test: Tests for invalid input types and assertions.

Created on: 6/1/2025
@author: Razan Ibrahim
Group: Matrix (ET foundations group 16 )
"""

import unittest

from solutions.grading_system import grading_system


class TestGradingSystem(unittest.TestCase):
    """Test the grading_system function"""

    # Standard Test Cases
    def test_score_between_100_and_90(self):
        """it should get "A" grade"""
        actual = grading_system(98)  # call function with test arguments
        expected = "A"  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_score_between_89_and_80(self):
        """it should get "B" grade"""
        actual = grading_system(84)
        expected = "B"
        self.assertEqual(actual, expected)

    def test_score_between_79_and_70(self):
        """it should get "C" grade"""
        actual = grading_system(76)
        expected = "C"
        self.assertEqual(actual, expected)

    def test_score_between_79_and_60(self):
        """it should get "D" grade"""
        actual = grading_system(62)
        expected = "D"
        self.assertEqual(actual, expected)

    def test_score_between_59_and_0(self):
        """it should get "F" grade"""
        actual = grading_system(34)
        expected = "F"
        self.assertEqual(actual, expected)

    # Edge Test Cases
    def test_score_of_0(self):
        """it should get "F" grade"""
        actual = grading_system(0)
        expected = "F"
        self.assertEqual(actual, expected)

    def test_score_of_100(self):
        """it should get "A" grade"""
        actual = grading_system(100)
        expected = "A"
        self.assertEqual(actual, expected)

    def test_score_is_float_value(self):
        """should return "B" grade"""
        actual = grading_system(85.9)
        expected = "B"
        self.assertEqual(actual, expected)

    # Defensive Test Cases
    def test_negative_score(self):
        """It would raise an error if the input score is less than zero"""
        with self.assertRaises(AssertionError):
            grading_system(-4)

    def test_score_grater_than_100(self):
        """It would raise an error if the input score is greater than 100"""
        with self.assertRaises(AssertionError):
            grading_system(115)

    def test_non_numeric_score(self):
        """It would raise an error if the input score is not numerical value"""
        with self.assertRaises(AssertionError):
            grading_system("hundred ")


if __name__ == "__main__":
    unittest.main()
