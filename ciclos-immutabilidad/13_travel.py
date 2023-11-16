#!/usr/bin/python3
from typing import Tuple

def recorrer(tupla):
    print("Recorrido directo:")
    for elemento in tupla:
        print(elemento)

    print("\nRecorrido inverso:")
    for j in range(len(tupla)):
        print(tupla[len(tupla) - j - 1])

    print("\nRecorrido intercalado:")
    for i in range(len(tupla)):
        if i % 2 == 0:
            print(tupla[i])

mi_tupla: Tuple[int] = (1, 2, 3)
recorrer(mi_tupla)
