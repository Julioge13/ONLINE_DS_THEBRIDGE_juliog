import numpy as np
import random

class Tablero:
    def __init__(self, jugador_id, dimensiones):
        self.jugador_id = jugador_id
        self.dimensiones = dimensiones
        self.barcos = {
            "Barco1": 4,
            "Barco2": 3,
            "Barco3": 3,
            "Barco4": 2,
            "Barco5": 2,
            "Barco6": 2,
            "Barco7": 1,
            "Barco8": 1,
            "Barco9": 1,
            "Barco10": 1
        }
        self.tablero_oculto = np.zeros(self.dimensiones)
        self.tablero_visible = np.zeros(self.dimensiones)

    def agregar_barco(self, nombre, eslora):
        self.barcos[nombre] = eslora

    def genera_barco(self, tam_barco=4):
        num_filas = self.dimensiones[0]
        num_columnas = self.dimensiones[1]
        orientaciones = ["N", "S", "O", "E"]

        while True:
            orientacion = random.choice(orientaciones)
            origen = (random.randint(0, num_filas - 1), random.randint(0, num_columnas - 1))
            fila = origen[0]
            columna = origen[1]
            barco = []
            
            if self.tablero_oculto[origen] != 1 and self.tablero_oculto[origen] != 2:
                barco.append(origen)
                for i in range(tam_barco - 1):
                    if orientacion == "N":
                        fila -= 1
                    elif orientacion == "S":
                        fila += 1
                    elif orientacion == "E":
                        columna += 1
                    else:
                        columna -= 1

                    if fila >= num_filas or fila < 0 or columna >= num_columnas or columna < 0:
                        break
                    elif self.tablero_oculto[fila, columna] == 1 or self.tablero_oculto[fila, columna] == 2:
                        break
                    barco.append((fila, columna))

                if len(barco) != tam_barco:
                    continue
                else:
                    self.coloca_barco(barco)
                    break
            else:
                continue

    def coloca_barco(self, barco):
        for coordenada in barco:
            self.tablero_oculto[coordenada] = 1

    def inicializar_barcos(self):
        for nombre, eslora in self.barcos.items():
            self.genera_barco(eslora)

    def disparo_coordenada(self, x, y):
        if self.tablero_oculto[x, y] == 1:
            print(f'¡Impacto en ({x}, {y})!')
        else:
            print(f'Agua en ({x}, {y})')

        self.tablero_visible[x, y] = 1

    def mostrar_tablero(self):
        for fila in range(self.dimensiones[0]):
            for columna in range(self.dimensiones[1]):
                if self.tablero_visible[fila, columna] == 0:
                    print("  ", end="")
                elif self.tablero_visible[fila, columna] == 1:
                    if self.tablero_oculto[fila, columna] == 1:
                        print(" X ", end="")
                    else:
                        print(" O ", end="")
                print(" | ", end="")
            print("\n" + "-" * (self.dimensiones[0] * 5))

    def verificar_victoria(self):
        for fila in range(self.dimensiones[0]):
            for columna in range(self.dimensiones[1]):
                if self.tablero_oculto[fila, columna] == 1 and self.tablero_visible[fila, columna] != 1:
                    return False
        return True