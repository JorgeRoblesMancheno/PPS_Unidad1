import pytest

from practica_ej_2.app.modulo1.funciones import esBinario
from practica_ej_3.app.modulo1.lista import estaEnRango, estaEnLista

def test_esBinario_valido():
    assert esBinario("1010") is True
    assert esBinario("000111") is True

def test_esBinario_invalido():
    assert esBinario("Hola") is False
    assert esBinario("102") is False
    assert esBinario("") is False

def test_estaEnRango_valido():
    assert estaEnRango(10, 1, 20) is True
    assert estaEnRango(1, 1, 20) is True
    assert estaEnRango(20, 1, 20) is True

def test_estaEnRango_fuera():
    assert estaEnRango(0, 1, 20) is False
    assert estaEnRango(25, 1, 20) is False

def test_estaEnLista_valido():
    lista = [6, 14, 11, 3, 2, 1, 15, 19]
    assert estaEnLista(6, lista) is True
    assert estaEnLista(19, lista) is True

def test_estaEnLista_fuera():
    lista = [6, 14, 11, 3, 2, 1, 15, 19]
    assert estaEnLista(10, lista) is False
    assert estaEnLista(20, lista) is False
