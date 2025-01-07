# Description

Write a program that takes a sentence as input and returns the length of each
 word in the sentence.
 The output should be a list of integers representing word lengths.

## Requirements

* The program should ignore punctuation and count only word lengths.
* Words are separated by spaces.
* Input will always be a single string.

### Example

```python
word_lengths("Hello world!") 
# Output: [5, 5]

word_lengths("Python is awesome.") 
# Output: [6, 2, 7]

word_lengths("I love MIT.") 
# Output: [1, 4, 3]
```

## Testing

Develop tests to validate your function. Consider:

* Sentences with varying lengths of words.
* Edge cases like empty strings or single words.

## Helpful Links

* [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
* [Python List Comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
