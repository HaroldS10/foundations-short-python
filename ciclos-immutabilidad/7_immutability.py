#!/usr/bin/python3
from typing import Tuple
mi_tupla: Tuple[int] = (1, 2, 3)
mi_lista = list(mi_tupla)
mi_lista[1] = 42
mi_tupla = tuple(mi_lista)

print (mi_tupla)
