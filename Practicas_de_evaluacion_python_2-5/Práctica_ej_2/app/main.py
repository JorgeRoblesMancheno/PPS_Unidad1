from modulo1.funciones import esBinario

if __name__ == "__main__":
    cadena = input("Introduce un número binario: ").strip()
    if esBinario(cadena):
        numero_decimal = int(cadena, 2)
        print(f"El número decimal es: {numero_decimal}")
    else:
        print("La cadena introducida no es un número binario válido.")
