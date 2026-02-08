from src.main import main


def test_input() -> None:
    numA = "90817"
    numB = "765"
    result = main(numA, numB)
    expected = "1"
    assert result == expected
