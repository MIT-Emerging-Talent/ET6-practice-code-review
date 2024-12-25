"""
Module for checking if a set of coordinates lie on a straight line.
"""

from typing import List

class Solution:
    """
    A solution to determine if given points lie on a straight line.
    """

    def check_line(self, coordinates: List[List[int]]) -> bool:
        """
        Determines if the given coordinates form a straight line.

        Arguments:
        coordinates: List[List[int]]
            - List of 2D coordinates where each coordinate is represented as [x, y].
            - At least two points are required.

        Returns:
        bool
            - True if all the points lie on a straight line, otherwise False.

        Raises:
        ValueError: If less than two points are provided.
        """

        # Defensive assertion
        if len(coordinates) < 2:
            raise ValueError("At least two points are required to determine a line.")

        # Calculate the slope using differences to avoid floating-point issues
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]

        # Iterate through the points
        for i in range(2, len(coordinates)):
            x_diff = coordinates[i][0] - coordinates[i - 1][0]
            y_diff = coordinates[i][1] - coordinates[i - 1][1]

            # Use cross multiplication to compare slopes
            if dy * x_diff != dx * y_diff:
                return False

        return True
