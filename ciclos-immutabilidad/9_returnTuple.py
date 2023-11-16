#!/usr/bin/python3
from typing import Tuple

def function_rtn(pares, impares):
    return *pares, *impares
    
pares: Tuple[int] = (2, 4, 6)
impares: Tuple[int] = (3, 6, 9)
    
numeros = function_rtn(pares, impares)
print (numeros)
