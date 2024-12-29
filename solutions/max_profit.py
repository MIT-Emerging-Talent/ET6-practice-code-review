#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the maximum profit from stock prices.

Module contents:
    - maxProfit: calculates the maximum profit from a list of stock prices
    with one buy and one sell transaction. We can not sell before buying.

Created on 12 28 2024
@author: Muhammet Isik
"""


def max_profit(prices: list[int]) -> int:
    """Calculates the maximum profit from a list of stock prices.

    The function determines the maximum profit that can be achieved by buying
    and selling a stock once. It ensures that the selling day is after the
    buying day.

    Parameters:
        prices: list[int], a list of integers representing stock prices on
        different days.

    Returns -> int:
        The maximum profit that can be achieved. Returns 0 if no profit
        is possible.

    Raises:
        AssertionError: if the input is not a list
        AssertionError: if the list contains non-integer elements

    Examples:
    >>> maxProfit([7, 2, 5, 3, 7, 4, 1, 10])
    9

    >>> maxProfit([10, 9, 8, 7, 6, 5])
    0  # No profit possible as prices decrease every day

    >>> maxProfit([3, 3, 3, 3, 3])
    0  # No profit possible as prices stay the same
    """
    # Check input validity, Input must be a integer list
    assert isinstance(prices, list), "Input must be a list"

    for price in prices:
        assert isinstance(price, int), "Every single List element must be an integer"

    buy = 0  # Buy index
    sell = 1  # Sell index
    max_profit_value = 0  # Initialize maximum profit

    # Loop through the list to calculate profit
    while sell < len(prices):
        current_profit = prices[sell] - prices[buy]  # Current profit calculation
        if prices[buy] < prices[sell]:
            # Update max profit if better profit found
            max_profit_value = max(current_profit, max_profit_value)
        else:
            buy = sell  # Update buy index if current price is lower
        sell += 1  # Move to the next sell day

    return max_profit_value


print(max_profit([4, 5, 6, 7, 8, 3, 34, 5, 7]))
