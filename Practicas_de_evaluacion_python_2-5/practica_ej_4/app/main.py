import unittest

from practica_ej_2.app.modulo1.funciones import esBinario
from practica_ej_3.app.modulo1.lista import estaEnRango, estaEnLista

class TestPractica4(unittest.TestCase):
    def test_esBinario(self):
        self.assertTrue(esBinario("1010"))
        self.assertFalse(esBinario("Hola"))

    def test_estaEnRango(self):
        self.assertTrue(estaEnRango(10, 1, 20))
        self.assertFalse(estaEnRango(25, 1, 20))

    def test_estaEnLista(self):
        lista = [6, 14, 11, 3, 2, 1, 15, 19]
        self.assertTrue(estaEnLista(6, lista))
        self.assertFalse(estaEnLista(10, lista))

if __name__ == "__main__":
    unittest.main()
