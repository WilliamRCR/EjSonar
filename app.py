"""Punto de entrada de la mini aplicación de ejemplo para SonarCloud.

Uso:
    python app.py "2 + 3"
    python app.py --texto "Anita lava la tina"
"""

from __future__ import annotations

import argparse

from src.calculadora import dividir, multiplicar, restar, sumar
from src.texto import contar_palabras, es_palindromo, palabra_mas_comun

_OPERACIONES = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir,
}


def evaluar_expresion(expresion: str) -> float:
    """Evalúa expresiones simples del tipo 'a op b' sin usar eval()."""
    partes = expresion.split()
    if len(partes) != 3:
        raise ValueError("Formato esperado: '<numero> <operador> <numero>'")
    izquierda, operador, derecha = partes
    if operador not in _OPERACIONES:
        raise ValueError(f"Operador no soportado: {operador}")
    return _OPERACIONES[operador](float(izquierda), float(derecha))


def analizar_texto(frase: str) -> dict[str, object]:
    return {
        "palabras": contar_palabras(frase),
        "es_palindromo": es_palindromo(frase),
        "palabra_mas_comun": palabra_mas_comun(frase),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ejemplo SonarCloud")
    parser.add_argument("expresion", nargs="?", help="Expresión aritmética 'a op b'")
    parser.add_argument("--texto", help="Analiza una frase en lugar de calcular")
    args = parser.parse_args(argv)

    if args.texto:
        print(analizar_texto(args.texto))
        return 0
    if args.expresion:
        print(evaluar_expresion(args.expresion))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
