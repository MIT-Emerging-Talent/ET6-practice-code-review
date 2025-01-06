# FizzBuzz Challenge
"""
Module resolving FizzBuzz problem with function tha takes an integer n as input
and prints the numbers from 1 to n with the rules:
- if a number is divisible by 3, print 'Fizz' instead of the number;
- if a number is divisible by 5, print 'Buzz' instead of the number;
- if a number is divisible by both 3 and 5, print 'FizzBuzz';
- otherwise, print the number itself.

Parameters: integer number

Result: print numbers from 1 to n with above rules.

Example:
>>> fizzbuzz(15)
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz

Created: 01/04/2025
Author: Svitlana Musiienko

"""


def fizzbuzz(n):
    # loop through numbers from 1 to n
    for num in range(1, n + 1):
        # check if the number is divisible by both 3 and 5
        if num % 3 == 0 and num % 5 == 0:
            # print "FizzBuzz" for multiples of both 3 and 5
            print("FizzBuzz")
        # check if the number is divisible by 3 only
        elif num % 3 == 0:
            # print "Fizz" for multiples of 3
            print("Fizz")
        # check if the number is divisible by 5 only
        elif num % 5 == 0:
            # print "Buzz" for multiples of 5
            print("Buzz")
        # print the number if none of the above conditions are met
        else:
            print(num)


# run function with example n=15
fizzbuzz(15)
