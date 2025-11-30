def esBinario(strbinario):

    """
    Devuelve True o False si la cadena de caracteres (strbinario)
    contiene únicamente caracteres '0' y '1'.
    """
    
    if not isinstance(strbinario, str):
        return False
    if strbinario == "":
        return False
    return all(ch in "01" for ch in strbinario)
