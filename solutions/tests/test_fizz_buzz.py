import unittest
from solutions.fizz_buzz import fizz_buzz  

""""
Write a program that prints numbers from 1 to 100. However:
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
For numbers that are multiples of both 3 and 5, print "FizzBuzz"

"""



class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizz_buzz(3), "Fizz")  # Multiple of 3
        self.assertEqual(fizz_buzz(6), "Fizz")  # Another multiple of 3
    
    def test_buzz(self):
        self.assertEqual(fizz_buzz(5), "Buzz")  # Multiple of 5
        self.assertEqual(fizz_buzz(10), "Buzz")  # Another multiple of 5
    
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")  # Multiple of both 3 and 5
        self.assertEqual(fizz_buzz(30), "FizzBuzz")  # Another multiple of 3 and 5
    
    def test_number(self):
        self.assertEqual(fizz_buzz(1), "1")  # Neither multiple of 3 nor 5
        self.assertEqual(fizz_buzz(2), "2")  # Another non-multiple of 3 or 5
    
    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            fizz_buzz(None)    

if __name__ == "__main__":
    unittest.main()   
