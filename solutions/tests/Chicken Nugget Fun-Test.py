import unittest
from io import StringIO
import sys

# Assuming the function is in a file named 'chicken_nugget.py'
from chicken_nugget import chicken_nugget_fun

class TestChickenNuggetFun(unittest.TestCase):

    def test_output(self):
        # Backup original stdout
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run the function
        chicken_nugget_fun()

        # Get the output
        output = sys.stdout.getvalue()

        # Check if the output contains a nugget fact
        self.assertTrue(any(fact in output for fact in [
            "Chicken nuggets were invented",
            "The world record for eating chicken nuggets",
            "McDonald's nuggets come in four shapes",
            "Try making homemade nuggets",
            "Some people dip chicken nuggets in honey",
            "Chicken nuggets are eaten by millions",
            "Sweet chili sauce makes chicken nuggets extra tasty",
            "You can even make plant-based chicken nuggets"
        ]))

        # Restore original stdout
        sys.stdout = original_stdout

if _name_ == '_main_':
    unittest.main()
