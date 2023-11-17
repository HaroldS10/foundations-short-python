from typing import Tuple, Union


def busqueda_binaria(tupla: Tuple[Union[int, str]], objetivo: Union[int, str]) -> int:
    
    izquierda, derecha = 0, len(tupla) - 1
 
    while izquierda <= derecha:
    
     medio = (izquierda + derecha) // 2
         
     if tupla[medio] == objetivo: 
            return medio
     elif tupla[medio] < objetivo:
             izquierda = medio + 1
     else:
             derecha = medio -1 
    return -1
