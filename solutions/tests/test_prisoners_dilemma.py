#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit test for prisoners_dilemma function.
Module contents:
    - TestPrisonersDilemma: Unit test class for the solve prisoners_dilemma function.
Test categories:
    - Standard cases: both players cooperate, both players defect
    - Defensive tests: invalid choices (not 'Cooperate' or 'Defect')
Created on 8 1 2025
@author: omer dafaalla
"""

import unittest
from ..prisoners_dilemma import prisoners_dilemma


class TestPrisonersDilemma(unittest.TestCase):
    """Unit test class for the solve_prisoners_dilemma function."""

    def test_cooperate_cooperate(self):
        """Test when both players cooperate."""
        self.assertEqual(prisoners_dilemma("Cooperate", "Cooperate"), (3, 3))

    def test_defect_cooperate(self):
        """Test when player 1 defects and player 2 cooperates."""
        self.assertEqual(prisoners_dilemma("Defect", "Cooperate"), (5, 0))

    def test_cooperate_defect(self):
        """Test when player 1 cooperates and player 2 defects."""
        self.assertEqual(prisoners_dilemma("Cooperate", "Defect"), (0, 5))

    def test_defect_defect(self):
        """Test when both players defect."""
        self.assertEqual(prisoners_dilemma("Defect", "Defect"), (1, 1))

    def test_invalid_choice(self):
        """Test invalid choices that raise AssertionError."""
        with self.assertRaises(AssertionError):
            prisoners_dilemma("Collaborate", "Cooperate")

        with self.assertRaises(AssertionError):
            prisoners_dilemma("Defect", "Collaborate")
