import unittest

from solutions.max_profit import max_profit


class MaxProfit(unittest.TestCase):
    """Tests for max_profit function"""
    
    def test_basic_case(self):
        """Buy at 1 and sell at 5, then buy at 3 and sell at 6, for a total profit of 7."""
        self.assertEqual(max_profit([7,1,5,3,6,4]), 7)