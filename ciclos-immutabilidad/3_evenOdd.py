#!/usr/bin/python3
from typing import Tuple
numero: Tuple[int] = 0
while numero < 5:
    if numero % 2 == 0:
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")
    numero += 1
