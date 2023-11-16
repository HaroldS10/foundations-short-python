#!/usr/bin/python3
from typing import Tuple

original: Tuple[int] = (1, 2, 3, 4, 5)
nuevo: Tuple[int] = tuple(elemento for elemento in original)

print ((original), "El ID de la tupla es:", id(original))
print ((nuevo), "El ID de la tupla es:", id(nuevo))
