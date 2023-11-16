#!/usr/bin/python3
from typing import Tuple
conjunto_partes: Tuple[int] = ((), (1,), (2,), (1, 2), (3,), (1, 3), (2, 3), (1, 2, 3))

tupla_partes = tuple(contenido for tupla in conjunto_partes for contenido in tupla if tupla)
print (tupla_partes)
