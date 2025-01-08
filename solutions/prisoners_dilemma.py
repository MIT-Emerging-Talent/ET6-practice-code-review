#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for solving the Prisoner's Dilemma.
Module contents:
    - prisoners_dilemma: Solves the game
      theory problem of the Prisoner's Dilemma.
Created on 8 1 2025
@author: omer dafaalla
"""


def prisoners_dilemma(choice1: str, choice2: str) -> tuple:
    """Solves the Prisoner's Dilemma
      and returns the outcomes for both players.

    Parameters:
        choice1: str, the first
          player's choice ('Cooperate' or 'Defect').
        choice2: str, the second
          player's choice ('Cooperate' or 'Defect').

    Returns -> tuple:
        A tuple containing two integers: the
          payoff for player 1 and player 2, respectively.

    Raises:
        AssertionError: if any choice is
          not 'Cooperate' or 'Defect'.

    >>> prisoners_dilemma
    ('Cooperate', 'Cooperate')
    (3, 3)

    >>> prisoners_dilemma('Defect', 'Cooperate')
    (5, 0)

    >>> prisoners_dilemma('Cooperate', 'Defect')
    (0, 5)

    >>> prisoners_dilemma('Defect', 'Defect')
    (1, 1)
    """

    assert choice1 in ["Cooperate", "Defect"], "Choice must be 'Cooperate' or 'Defect'."
    assert choice2 in ["Cooperate", "Defect"], "Choice must be 'Cooperate' or 'Defect'."

    # Payoff matrix based on the choices
    if choice1 == "Cooperate" and choice2 == "Cooperate":
        return (3, 3)
    elif choice1 == "Defect" and choice2 == "Cooperate":
        return (5, 0)
    elif choice1 == "Cooperate" and choice2 == "Defect":
        return (0, 5)
    elif choice1 == "Defect" and choice2 == "Defect":
        return (1, 1)
