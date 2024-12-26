# Tests

This directory contains the unit tests for the project.
The tests are written using the `unittest` framework.

## Running Tests

To run the tests, use the following command:

```sh
python -m unittest
```

This command will automatically discover and run all the test cases in this directory.

## Directory Structure

The tests are organized as follows:

```md
solutions/
    tests/
        __init__.py
        test_example.py
```

- `__init__.py`: This file makes the directory a Python package.
- `test_example.py`: This file contains example test cases.

## Writing Tests

To add new tests, create a new file in the `tests` directory
and define your test cases using the `unittest` framework.

Here is an example of a simple test case:

```python
import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

```

## Test Coverage

Ensure that your tests cover all the critical parts of your codebase.
Aim for high test coverage to catch potential issues early.

## Contributing

If you would like to contribute to the tests, please follow these guidelines:

1. Write clear and concise test cases.
2. Ensure that your tests pass before submitting a pull request.
3. Follow the existing code style and conventions.

Let's maintain a high-quality codebase! 👩‍💻✨🚀
