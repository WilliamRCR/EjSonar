import pytest

from src.calculadora import (
    DivisionPorCeroError,
    dividir,
    multiplicar,
    potencia,
    restar,
    sumar,
)


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0


def test_restar():
    assert restar(10, 4) == 6


def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(5, 0) == 0


def test_dividir_ok():
    assert dividir(9, 3) == 3


def test_dividir_entre_cero():
    with pytest.raises(DivisionPorCeroError):
        dividir(1, 0)


def test_potencia():
    assert potencia(2, 10) == 1024
    assert potencia(5, 0) == 1


def test_potencia_exponente_invalido():
    with pytest.raises(TypeError):
        potencia(2, 1.5)
