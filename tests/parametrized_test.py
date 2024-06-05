import pytest

from src.hex_converter import hexadecimal_to_decimal  # noqa: F401

# aplica o marcador de dependency para todos os testes do arquivo
pytestmark = pytest.mark.dependency  # NÃO REMOVA ESSA LINHA


@pytest.mark.parametrize(
    "hex_to_convert, expected",
    [
        ("8", 8),
        ("9", 9),
        ("a", AssertionError),
        ("b", AssertionError),
        ("c", AssertionError),
        ("e", AssertionError),
        ("f", AssertionError),
    ],
)
def test_convert(hex_to_convert, expected):
    hexadecimal_to_decimal(hex_to_convert) == expected
