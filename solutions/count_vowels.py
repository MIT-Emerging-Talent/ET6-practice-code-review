'''
Write a function count_vowels(s) that returns the number of vowels in a given string.

Examples
count_vowels("hello") should return 2.
count_vowels("sky") should return 0.
count_vowels("AEIOU") should return 5.
Behavior
The function should:

Take a single string s as input.
Identify and count the vowels (both uppercase and lowercase) in the string.
Return the total count of vowels as an integer.
'''

def count_vowels(text: str) -> int:
    """Count the number of vowels (A,E,I,O,U,a,e,i,o,u) in a string.
    
    Parameters:
        text: str, the input string to check
        
    Returns -> int: number of vowels in the text

    Raises:
        AssertionError: if the argument is not a string
    
    >>> count_vowels("FATIMA")
    3
    >>> count_vowels("Helloworld")
    3
    >>> count_vowels("Madiha")
    3
    """
  assert isinstance(text, str), "input must be a string"
  vowels = "aeiouAEIOU"
  count = 0
  for letter in text:
    if letter in vowels:
      count += 1
  return count



# print(count_vowels("hello"))


  # if vowels== "":
  #   return 0
  # if vowels== "aeiouAEIOU":
  #   return 5
  # if vowels== "fly":
  #   return 0
  # if vowels== "hellO World":
  #   return 3
  # return 0
