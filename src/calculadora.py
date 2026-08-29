"""Operaciones aritméticas básicas usadas como ejemplo para el análisis con SonarCloud."""

from __future__ import annotations


class DivisionPorCeroError(ZeroDivisionError):
    """Error de dominio para dejar clara la causa al llamador."""


def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise DivisionPorCeroError("No se puede dividir entre cero")
    return a / b


def potencia(base: float, exponente: int) -> float:
    if not isinstance(exponente, int):
        raise TypeError("El exponente debe ser un entero")
    return base ** exponente
