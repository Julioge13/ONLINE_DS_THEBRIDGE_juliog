import time

# Turno del jugador
print()
print("             ~~~~~~~~~~~~~~~~")
print("             |              |")
print("             |   TU TURNO   |")
print("             |              |")
print("             ~~~~~~~~~~~~~~~~")
print()



# Turno de la máquina (simulado como disparo aleatorio)
print()
print("             ~~~~~~~~~~~~~~~~")
print("             |     TURNO    |")
print("             |     DE LA    |")
print("             |    MÁQUINA   |")
print("             ~~~~~~~~~~~~~~~~")
print()





def disparo_coordenada(self, x, y):
    if self.tablero_oculto[x, y] == 1:
        print(f'Has escogido disparar en ({x}, {y})')
        time.sleep(1)
        print(f'Habrás acertado', end="", flush=True)
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(1)
        print("?", flush=True)
        time.sleep(2)
        print("\n\t¡¡Bien hecho, tocado!!\n\n")
        time.sleep(1)
        print("¡Sigue lanzando!\n")
    else:
        print(f'Has escogido disparar en ({x}, {y})')
        time.sleep(1)
        print(f'Habrás acertado', end="", flush=True)
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(1)
        print("?", flush=True)
        time.sleep(2)
        print("\n\tNooo.. Agua...\n\tHay que afinar esa puntería...\n\n")
