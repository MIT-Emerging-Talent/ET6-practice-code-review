# Simple Interest Calculator - Coding Challenge

## Overview

This coding challenge implements a **Simple Interest Calculator**. The purpose
of this calculator is to compute the simple interest based on the following
inputs:

- Principal amount
- Annual interest rate (in percentage)
- Time (in years)

The simple interest is calculated using the formula:

**SI** = _`P × R × T / 100`_

Where:

- **P** = Principal amount (the initial money)
- **R** = Annual interest rate (in percentage)
- **T** = Time (in years)

The program prompts the user for these values, computes the simple interest,
and displays the result.

## Features

- **Interactive Input**: Prompts the user to enter the principal, interest rate, and time,
  and calculates the simple interest.
- **Simple Calculation**: Computes the interest using the standard simple interest formula.
- **Unit Testing**: Includes tests to validate the correctness of the calculator’s functionality.

## How to Run the Calculator

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/MIT-Emerging-Talent/ET6-foundations-group-11.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ET6-foundations-group-11
    ```

3. Install any necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the calculator script:

    ```bash
    python simple_interest_calculator.py
    ```

5. When prompted, enter the required inputs (Principal, Interest Rate, and Time in years),
   and the script will calculate and display the simple interest.

## Running Unit Tests

1. To ensure the calculator works correctly, you can run the unit tests with:

    ```bash
    python -m unittest tests/test_simple_interest_calculator.py
    ```

2. If everything is working properly, the output will look like this:

    ```bash
    Ran 4 tests in 0.001s
    OK
    ```

3. **NOTE**: If you haven't already, make sure to include a `requirements.txt` or instructions
   for users to install any dependencies needed to run the tests (if any).

## Code Structure

- `simple_interest_calculator.py`: The main Python script for calculating simple interest.
- `tests/test_simple_interest_calculator.py`: Unit tests to verify the correctness of the calculator.
- `README.md`: This documentation file.

## How to Contribute

1. Fork the repository and clone it to your local machine.

2. Create a new branch for each feature or bug fix:

    ```bash
    git checkout -b feature/your-feature-name
    ```

3. Make your changes in the new branch.

4. Ensure your code is clean, well-documented, and follows Python best practices.

5. Write unit tests to validate the functionality of your code.

6. Once you're done, submit a pull request for review. The pull request should include:

    - A clear description of what was changed.
    - Any relevant testing details.
    - Links to any related issues.

7. To test your code, make sure to run the unit tests to validate your changes:

    ```bash
    python -m unittest tests/test_simple_interest_calculator.py
    ```

8. If your changes affect the documentation, please update the README file accordingly.

## License

This coding challenge is licensed under the MIT License. Please refer to the
[LICENSE](LICENSE) file for details.
