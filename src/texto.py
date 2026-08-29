"""Utilidades de texto para el ejemplo de SonarCloud."""

from __future__ import annotations

from collections import Counter

PALABRAS_VACIAS = {"el", "la", "los", "las", "de", "y", "a", "en", "un", "una"}


def normalizar(frase: str) -> str:
    """Pasa a minúsculas y colapsa espacios repetidos."""
    return " ".join(frase.lower().split())


def contar_palabras(frase: str) -> int:
    frase = normalizar(frase)
    if not frase:
        return 0
    return len(frase.split())


def es_palindromo(frase: str) -> bool:
    limpio = "".join(c for c in frase.lower() if c.isalnum())
    return limpio == limpio[::-1]


def palabra_mas_comun(frase: str, incluir_vacias: bool = False) -> str | None:
    tokens = normalizar(frase).split()
    if not incluir_vacias:
        tokens = [t for t in tokens if t not in PALABRAS_VACIAS]
    if not tokens:
        return None
    return Counter(tokens).most_common(1)[0][0]
