from solutions.bank import value


def test_hello() -> None:
    """
    Test the 'value' function with the input 'hello' and 'HELLO'.

    This test verifies that both lowercase and uppercase 'hello' return the expected
    value of 0.
    """
    assert value("hello") == 0  # 'hello' should return 0
    assert value("HELLO") == 0  # 'HELLO' should return 0, case-insensitive


def test_h() -> None:
    """
    Test the 'value' function with the input 'hippy'.

    This test checks that the word 'hippy' returns the correct value of 20.
    """
    assert value("hippy") == 20  # 'hippy' should return 20


def test_something() -> None:
    """
    Test the 'value' function with the input 'bank' and 'jungkook'.

    This test verifies that the words 'bank' and 'jungkook' both return the expected
    value of 100.
    """
    assert value("bank") == 100  # 'bank' should return 100
    assert value("jungkook") == 100  # 'jungkook' should return 100
