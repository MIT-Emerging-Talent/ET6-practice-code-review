from solutions.plates import is_valid


def test_normal():
    """
    Test case for valid license plates
    """
    assert (
        is_valid("CS50") is True
    )  # Starts with two letters, followed by numbers, valid format
    assert is_valid("JK") is True  # Only two letters, valid format


def test_len():
    """
    Test case for invalid license plates that exceed the length limit.
    """
    assert is_valid("whatisthis") is False  # Plate exceeds 6 characters, invalid


def test_zero_between():
    """
    Test cases where numbers (particularly '0') appear inappropriately between letters.
    """
    assert is_valid("hi0012") is False  # '0' appears in between letters, invalid
    assert is_valid("xz4yz0") is False  # '0' appears after letters, invalid


def test_capital():
    """
    Test cases for valid license plates with uppercase letters and numbers.
    """
    assert is_valid("AB1900") is True  # Starts with letters, then numbers, valid format
    assert is_valid("COOKIE") is True  # Only letters, valid format


def test_firstnum_zero():
    """
    Test case where the first number is '0', which is invalid.
    """
    assert is_valid("0CS90") is False  # Starts with '0', invalid


def test_no_punctuation():
    """
    Test cases where the plate includes invalid punctuation characters.
    """
    assert is_valid("xx,.&!") is False  # Contains punctuation, invalid
    assert is_valid(".kook12!") is False  # Contains punctuation, invalid


def test_first_two_alpha():
    """
    Test cases where the first two characters are not letters or are invalid.
    """
    assert is_valid("s1hag") is False  # First character is a number, invalid
    assert is_valid("00nod") is False  # Starts with '0', invalid
    assert is_valid("8805") is False  # Does not start with letters, invalid
