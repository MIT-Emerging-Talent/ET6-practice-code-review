import unittest

from solutions.sort_numbers import sort_numbers


class TestSortNumbers(unittest.TestCase):
    def test_sorted_numbers(self):
        self.assertEqual(sort_numbers([4, 1, 3, 2]), [1, 2, 3, 4])

    def test_floats(self):
        self.assertEqual(sort_numbers([4.5, 2.3, 1.7, 3.9]), [1.7, 2.3, 3.9, 4.5])

    def test_mixed_numbers(self):
        self.assertEqual(sort_numbers([4, 2.5, 3, 1.2]), [1.2, 2.5, 3, 4])

    def test_invalid_input(self):
        self.assertEqual(sort_numbers(["a", None, 3]), "Isn't possible to sort")

    def test_empty_list(self):
        self.assertEqual(sort_numbers([]), "Isn't possible to sort")


if __name__ == "__main__":
    unittest.main()
