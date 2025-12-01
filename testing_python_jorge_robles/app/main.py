"""
charfun.py
Programa que determina si una cadena proporcionada por el
usuario es palíndroma. Para ello se preguntará por teclado al
usuario tantas veces como quiera hasta que escriba la palabra
salir.
"""

from modulo1.funciones import esPalindromo

def main():
    frase = ""
    while frase.lower() != "salir":      
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")

        if frase.lower() != "salir":      
            if esPalindromo(frase):
                print("La frase es palíndroma.")
            else:
                print("La frase no es palíndroma.")

    print("Programa finalizado.")

if __name__ == "__main__":
    main()