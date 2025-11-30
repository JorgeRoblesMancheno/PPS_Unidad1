import unittest
from app.modulo1.funciones import esBinario

class TestEsBinario(unittest.TestCase):
    def test_cadenas_validas(self):
        self.assertTrue(esBinario("1"))
        self.assertTrue(esBinario("1001"))

    def test_cadenas_invalidas(self):
        self.assertFalse(esBinario("2"))
        self.assertFalse(esBinario("Hola"))
        self.assertFalse(esBinario(""))

if __name__ == "__main__":
    unittest.main()
