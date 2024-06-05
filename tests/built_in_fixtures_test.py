import pytest
from src.hex_converter import (  # noqa: F401
    main,
    print_hexadecimal_to_decimal,
    write_hexadecimal_to_decimal,
)

# aplica o marcador de dependency para todos os testes do arquivo
pytestmark = pytest.mark.dependency  # NÃO REMOVA ESSA LINHA


def test_monkeypatch(monkeypatch):

    def mock_input(prompt):
        return "a"

    monkeypatch.setattr("builtins.input", mock_input)
    output = main()

    assert output == 10


def test_capsys(capsys):
    print_hexadecimal_to_decimal("a")

    capture = capsys.readouterr()

    assert capture.err == ""
    assert capture.out == "10\n"


def test_tmp_path(tmp_path):
    output_path = tmp_path / "output.txt"

    write_hexadecimal_to_decimal("a", output_path)

    assert output_path.is_file()
    assert output_path.read_text() == "10"
