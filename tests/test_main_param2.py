import pytest

from src.main import main


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("8350", "0009", "9350"),
        ("1234", "99", "9934"),
        ("1234", "", "1234"),
        ("999", "0", "999"),
        ("0", "987", "9"),
        ("111", "9", "911"),
        ("111", "999", "999"),
        ("-8350", "0009", "0000"),
        ("-99", "0", "-09"),
        ("-10", "0", "00"),
        ("-1", "", "-1"),
    ],
)
def test_main_examples(a, b, expected):
    assert main(a, b) == expected
