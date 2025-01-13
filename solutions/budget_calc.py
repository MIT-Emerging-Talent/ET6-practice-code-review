#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for calculating
 the budget distribution.

Module contents:
    calculate_budget: Calculates budget
      distribution based on a total budget.

Created on 5 1 2025
@author: omer dafaalla
"""


def calculate_budget(total_budget: float) -> list:
    """
    Calculates the budget distribution
      for categories based on a given total budget.

    Parameters:
        total_budget (float): The total
          available budget, which must
            be greater than 0 and less than or equal to 3000.

    Returns:
        list: A list of strings containing
          category names and the
            allocated budget amounts.

    Raises:
        ValueError: If the total_budget
          is not within the allowed range
            (greater than 0 and less than or equal to 3000).
    """

    # Defensive check to ensure the budget is within the valid range
    if not (0 < total_budget <= 3000):
        raise ValueError(
            "Total budget must be greater than 0 and less than or equal to 3000."
        )

    # Define the categories and their corresponding percentages
    categories = ["Rent", "Groceries", "Savings", "Others"]
    percentages = [0.4, 0.3, 0.2, 0.1]

    # List to store the results
    budget_distribution = []

    # Calculate the budget allocation for each category
    for i in range(len(categories)):
        allocated_budget = total_budget * percentages[i]
        budget_distribution.append(f"{categories[i]}: {allocated_budget:.2f}")

    return budget_distribution
