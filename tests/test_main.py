from src.main import main


def test_2positive() -> None:
    numA = "90817"
    numB = "765"
    result = main(numA, numB)
    expected = "97867"
    assert result == expected


def test_negative_and_positive() -> None:
    numA = "-8350"
    numB = "0129"
    result = main(numA, numB)
    expected = "-0120"
    assert result == expected


def test_2positive_many_zeros() -> None:
    numA = "90817"
    numB = "0009"
    result = main(numA, numB)
    expected = "99817"
    assert result == expected


def test_negative_and_positive_many_zeros() -> None:
    numA = "-8350"
    numB = "0009"
    result = main(numA, numB)
    expected = "0000"
    assert result == expected
