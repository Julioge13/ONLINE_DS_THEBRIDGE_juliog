##### ESTRUCTURA DE UN SCRIPT
# IMPORTS
# VARIABLES Y CONSTANTES GLOBALES
# DEFINICION DE FUNCIONES
# DEFINICION DE CLASES
# CODIGO PRINCIPAL

from sys import path
path.append(".\\")
print(path) ## esto es si creo una carpeta con las librerias

import numpy as np
import funciones as fn # aqui pondria el nombre del directorio, por ejemplo liberia.funciones

tam_tablero = input(f"¿Qué tamaño quieres? (ancho,alto) ({fn.TAM_DEFECTO,fn.TAM_DEFECTO})")

if tam_tablero!= "":
    lista_dimensiones = [int(elemento) for elemento in tam_tablero.split(",")]
else:
    lista_dimensiones = (fn.TAM_DEFECTO,fn.TAM_DEFECTO)

tablero = fn.crea_tablero(lista_dimensiones)

fn.coloca_barco(tablero, [(1,1),(1,2),(1,3)])

print(tablero)