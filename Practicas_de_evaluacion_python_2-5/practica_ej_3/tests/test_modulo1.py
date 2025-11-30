import unittest
from app.modulo1.lista import estaEnRango, estaEnLista

class TestListaFunciones(unittest.TestCase):
    def test_esta_en_rango(self):
        self.assertTrue(estaEnRango(10, 1, 20))
        self.assertTrue(estaEnRango(1, 1, 20))
        self.assertTrue(estaEnRango(20, 1, 20))

    def test_esta_en_lista(self):
        lista = [6, 14, 11, 3, 2, 1, 15, 19]
        self.assertTrue(estaEnLista(6, lista))
        self.assertTrue(estaEnLista(19, lista))

if __name__ == "__main__":
    unittest.main()

