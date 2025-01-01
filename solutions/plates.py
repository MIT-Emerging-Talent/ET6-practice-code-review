def main():
    """

    Created On: 2025-01-01
    Author: @arvidon


    Main function that takes user input and checks if the input is a valid license plate.
    It calls the `is_valid` function to determine whether the provided text follows the required format.

    The format is:
    - Must start with at least two letters.
    - Length of the plate should be between 2 and 6 characters.
    - No numbers in between the plate, and the first number must not be '0'.
    - The plate must be alphanumeric.
    """
    # Prompt the user to input a license plate string
    text = input("Text: ")

    # Check if the license plate string is valid
    if is_valid(text):
        print("True")
    else:
        print("False")


def is_valid(s):
    """
    Validates a license plate string based on several conditions:
    1. The plate must start with at least two letters.
    2. The length of the plate must be between 2 and 6 characters.
    3. The first number (if any) must not be '0'.
    4. Numbers should not appear between letters.
    5. The plate should only contain alphanumeric characters (letters and numbers).

    Args:
        s (str): The license plate string to be validated.

    Returns:
        bool: True if the plate is valid, False otherwise.
    """
    # Plates should start with at least two letters
    if len(s) < 2 or not s[:2].isalpha():
        return False

    # The length of the plate should be between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # The first number (if any) should not be 0, and there should be no numbers in between
    temp = 0
    for i in range(3):
        if s[(len(s) - 1) - i].isalpha():
            if s[(len(s) - i - 1) - 1].isnumeric():
                temp += 1
    if temp > 0:
        return False
    if temp == 0:
        for j in range(len(s) - 1):
            if s[j].isalpha():
                if s[j + 1] == "0":
                    return False

    # The plate should contain only alphanumeric characters
    if not s.isalnum():
        return False

    return True


if __name__ == "__main__":
    main()
