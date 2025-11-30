from modulo1.lista import estaEnRango, estaEnLista

if __name__ == "__main__":
    lista_valores = [6, 14, 11, 3, 2, 1, 15, 19]
    try:
        numero = int(input("Introduce un número entre 1 y 20: "))
        if estaEnRango(numero, 1, 20):
            if estaEnLista(numero, lista_valores):
                print("El número está en la lista.")
            else:
                print("El número no está en la lista.")
        else:
            print("El número está fuera del rango permitido.")
    except ValueError:
        print("Debes introducir un número entero.")
