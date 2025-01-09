from solutions.SumList import SumList


def test_SumList() -> None:
    """
    Tests the many CornerCases of the SumList function including negative integers,
    empty list, floats, zero at the beginning, single two digit number.
    """
    assert SumList([1, 2, 3, 4, 5]) == 15
    assert SumList([10]) == 10
    assert SumList([-1, -2, -3, -4, -5]) == -15
    assert SumList([1.5, 2.5, 3.0]) == 7.0
    assert SumList([1, 2.5, -3, 4.5]) == 5.0
    assert SumList([0, 1, 2, 3]) == 6
    assert SumList([]) == 0
