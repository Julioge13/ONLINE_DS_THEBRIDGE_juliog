import numpy as np

TAM_DEFECTO = 10

def crea_tablero(dimensiones):
    return np.full(dimensiones, " ")

def coloca_barco(tablero, barco):
    for pieza in barco:
        tablero[pieza] = "O"


## codigo para que lo que venga despues, se lance si se ejecuta desde funciones, no si lo han importado de otro
 if __name__ == "__main__":
    print(crea_tablero((15,10)))
