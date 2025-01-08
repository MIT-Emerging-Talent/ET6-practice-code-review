import os
import unittest

import pandas as pd

from solutions.get_unique_values import get_unique_values


class TestGetUniqueValues(unittest.TestCase):
    def setUp(self):
        """Create a sample CSV file for testing."""
        data = {"col1": [1, 2, 2, 3], "col2": ["a", "b", "a", "c"]}
        self.df = pd.DataFrame(data)
        self.df.to_csv("test_data.csv", index=False)

    def tearDown(self):
        """Remove the sample CSV file after testing."""
        os.remove("test_data.csv")

    def test_empty_file(self):
        """Test with an empty file."""
        # Create an empty file with header
        with open("empty_file.csv", "w") as f:
            f.write("col1,col2\n")  # Add header row

        self.assertEqual(get_unique_values("empty_file.csv", "col1"), [])
        os.remove("empty_file.csv")  # Clean up the empty file

    def test_unique_values(self):
        """Test with valid data and column."""
        self.assertEqual(get_unique_values("test_data.csv", "col1"), [1, 2, 3])
        self.assertEqual(get_unique_values("test_data.csv", "col2"), ["a", "b", "c"])

    def test_file_not_found(self):
        """Test with a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            get_unique_values("nonexistent_file.csv", "col1")

    def test_column_not_in_csv(self):
        """Test with a column not in the CSV."""
        with self.assertRaises(KeyError):
            get_unique_values("test_data.csv", "non_existent_column")
