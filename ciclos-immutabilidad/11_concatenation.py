#!/usr/bin/python3
from typing import Tuple

def tuplas(tupla1, tupla2, escalar):
    resultado = tuple(tupla1 * escalar) + tuple(tupla2 * escalar)
    return resultado

resultado: Tuple[int] = tuplas((1, 2), (3, 4), 3)

print(resultado)
