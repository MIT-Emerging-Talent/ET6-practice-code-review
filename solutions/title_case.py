def title_case(sentence: str) -> str:
    """
    Converts a string to title case (capitalize the first letter of each word).

    Args:
        s (str): The input string.

    Returns:
        str: The string converted to title case.

    Raises:
        AssertionError: If the input is not a string.
        
    >>> title_case("hello world")
    'Hello World'
    >>> title_case("PYTHON is awesome")
    'Python Is Awesome'
    >>> title_case("")
    ''
    >>> title_case("123abc")
    '123Abc'
    """
    assert isinstance(sentence , (str)), "Input must be a  (String)."
    return sentence.title()