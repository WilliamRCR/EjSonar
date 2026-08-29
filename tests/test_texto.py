from src.texto import contar_palabras, es_palindromo, normalizar, palabra_mas_comun


def test_normalizar():
    assert normalizar("  Hola   MUNDO  ") == "hola mundo"


def test_contar_palabras():
    assert contar_palabras("uno dos tres") == 3
    assert contar_palabras("   ") == 0


def test_es_palindromo():
    assert es_palindromo("Anita lava la tina")
    assert not es_palindromo("hola mundo")


def test_palabra_mas_comun_ignora_vacias():
    assert palabra_mas_comun("el gato y el perro y el gato") == "gato"


def test_palabra_mas_comun_incluir_vacias():
    assert palabra_mas_comun("el el el gato", incluir_vacias=True) == "el"


def test_palabra_mas_comun_sin_tokens():
    assert palabra_mas_comun("") is None
