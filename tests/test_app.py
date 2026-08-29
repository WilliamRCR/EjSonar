import pytest

from app import analizar_texto, evaluar_expresion, main


def test_evaluar_expresion_ok():
    assert evaluar_expresion("2 + 3") == 5
    assert evaluar_expresion("10 / 4") == 2.5


def test_evaluar_expresion_formato_invalido():
    with pytest.raises(ValueError):
        evaluar_expresion("2 +")


def test_evaluar_expresion_operador_invalido():
    with pytest.raises(ValueError):
        evaluar_expresion("2 % 3")


def test_analizar_texto():
    resultado = analizar_texto("Anita lava la tina")
    assert resultado["palabras"] == 4
    assert resultado["es_palindromo"] is True


def test_main_con_expresion(capsys):
    assert main(["6 * 7"]) == 0
    assert "42" in capsys.readouterr().out


def test_main_con_texto(capsys):
    assert main(["--texto", "hola hola mundo"]) == 0
    assert "palabra_mas_comun" in capsys.readouterr().out


def test_main_sin_argumentos():
    assert main([]) == 1
