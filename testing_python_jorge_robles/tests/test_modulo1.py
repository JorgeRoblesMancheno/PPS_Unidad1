import unittest
from app.modulo1.funciones import esPalindromo

class TestPalindromo(unittest.TestCase):
    def test_palindromos_validos(self):
        self.assertTrue(esPalindromo("Anita lava la tina"))
        self.assertTrue(esPalindromo("A man a plan a canal Panama"))

    def test_palindromos_con_tildes(self):
        self.assertFalse(esPalindromo("Á mamá Roma le avivó la mía Moro máma Á"))

    def test_no_palindromos(self):
        self.assertFalse(esPalindromo("Hola mundo"))
        self.assertFalse(esPalindromo("Esto no es palíndromo"))

    def test_cadenas_vacias_y_espacios(self):
        self.assertTrue(esPalindromo(""))
        self.assertTrue(esPalindromo("     "))

    def test_caracteres_especiales_y_numeros(self):
        self.assertTrue(esPalindromo("12321"))
        self.assertFalse(esPalindromo("12345"))
        self.assertTrue(esPalindromo("No 'x' in Nixon"))

    def test_entrada_invalida(self):
        with self.assertRaises(TypeError):
            esPalindromo(None)
        with self.assertRaises(TypeError):
            esPalindromo(12345)

if __name__ == "__main__":
    unittest.main()

