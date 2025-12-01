import unicodedata

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.
    """

    # Normalizar para eliminar tildes 
    cadena = ''.join(char for char in cadena if unicodedata.category(char) != 'Mn')

    # Convertir a minúsculas y eliminar caracteres no alfanuméricos
    cadena_limpia = ''.join(char.lower() for char in cadena if char.isalnum())

    return cadena_limpia == cadena_limpia[::-1]
