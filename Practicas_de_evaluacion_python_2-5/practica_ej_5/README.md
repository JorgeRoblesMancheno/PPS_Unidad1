# Ejercicio 5

Esta práctica contiene una suite de tests que comprueba las mismas funciones que el ejercicio anterior pero usando un framework distinto. En este caso voy a usar pytest:

- `esBinario(strbinario)` del ejercicio 2
- `estaEnRango(valor, minimo, maximo)` del ejercicio 3
- `estaEnLista(valor, lista)` del ejercicio 3

## Instalación pytest
```bash
python -m pip install pytest
```

## Ejecutar los tests

Desde el directorio raíz, ejecutamos:

```bash
python -m pytest practica_ej_5/app/main.py -v
