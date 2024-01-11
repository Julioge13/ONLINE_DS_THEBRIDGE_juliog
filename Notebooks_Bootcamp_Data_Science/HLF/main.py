from tablero import Tablero
import random

def main():
    jugador = Tablero(jugador_id='Jugador', dimensiones=(10, 10))
    maquina = Tablero(jugador_id='Máquina', dimensiones=(10, 10))
    jugador.inicializar_barcos()
    maquina.inicializar_barcos()

    while True:
        print("Tablero del Jugador:")
        jugador.mostrar_tablero()

        # Turno del jugador
        print("Tu turno:")
        while True:
            try:
                x = int(input("Introduce la coordenada X (0-9): "))
                y = int(input("Introduce la coordenada Y (0-9): "))
                if 0 <= x <= 9 and 0 <= y <= 9:
                    break
                else:
                    print("Coordenadas fuera de rango. Introduce coordenadas entre 0 y 9.")
            except ValueError:
                print("Entrada inválida. Introduce un número válido.")

        jugador.disparo_coordenada(x, y)
        if jugador.verificar_victoria():
            print("¡Felicidades! ¡Has hundido todos los barcos enemigos! ¡Ganas!")
            break

        print("\nTablero de la Máquina:")
        maquina.mostrar_tablero()

        # Turno de la máquina (simulado como disparo aleatorio)
        print("\nTurno de la Máquina:")
        x_maquina = random.randint(0, 9)
        y_maquina = random.randint(0, 9)
        maquina.disparo_coordenada(x_maquina, y_maquina)

        if maquina.verificar_victoria():
            print("¡La máquina ha hundido todos tus barcos! ¡Has perdido!")
            break

if __name__ == "__main__":
    main()
