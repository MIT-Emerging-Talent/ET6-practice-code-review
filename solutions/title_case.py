def title_case(s: str) -> str:
    """
    Converts a string to title case (capitalize the first letter of each word).

    Args:
        s (str): The input string.

    Returns:
        str: The string converted to title case.

    Examples:
        >>> string_to_title_case("hello world")
        'Hello World'
        >>> string_to_title_case("PYTHON is awesome")
        'Python Is Awesome'
        >>> string_to_title_case("")
        ''
        >>> string_to_title_case("123abc")
        '123abc'
    """
    return s.title()