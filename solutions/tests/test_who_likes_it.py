"""
Tests for the `who_likes_it` module.

This tests the correctness of the function `who_likes_it`:
    - Different numbers of names in the input list.
    - Defensive assertions for invalid inputs
    - Boundary cases like empty and large lists.

Author: Madiha Malikzada
Date: 2025-01-06
"""

import unittest
from solutions.who_likes_it import who_likes_it


class TestWhoLikesIt(unittest.TestCase):
    """
    Unit tests for the `who_likes_it` function
    """

    def test_boundary_empty_list(self):
        """
        Test boundary case for an empty list.
        """
        self.assertEqual(who_likes_it([]), "no one likes this")

    def test_one_like(self):
        """
        Test the case when one person likes the post
        """
        self.assertEqual(who_likes_it(["Evan"]), "Evan likes this")

    def test_two_likes(self):
        """
        Test the case when two people like the post
        """
        self.assertEqual(who_likes_it(["Evan", "Madiha"]), "Evan and Madiha like this")

    def test_three_likes(self):
        """
        Test the case when three people like the post
        """
        self.assertEqual(
            who_likes_it(["Evan", "Madiha", "Megan"]),
            "Evan, Madiha and Megan like this",
        )

    def test_more_than_three_likes(self):
        """
        Test the case when more than three people like the post
        """
        self.assertEqual(
            who_likes_it(["Evan", "Madiha", "Megan", "Camila"]),
            "Evan, Madiha and 2 others like this",
        )

    def test_invalid_input(self):
        """
        Test the case when input is not a list type
        """
        with self.assertRaises(AssertionError):
            who_likes_it("not a list")

    def test_defensive_non_string_elements(self):
        """
        Test the case when input list contains non-string elements
        """
        with self.assertRaises(AssertionError):
            who_likes_it(["Evan", 1, "Megan"])

    def test_boundary_large_list(self):
        """
        Test boundary case for a large list.
        """
        names = ["Name" + str(i) for i in range(100)]
        self.assertEqual(
            who_likes_it(names), f"Name0, Name1 and {len(names) - 2} others like this"
        )


if __name__ == "__main__":
    unittest.main()
