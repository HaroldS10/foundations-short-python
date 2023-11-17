from typing import Tuple, Union
 """
    Realiza una búsqueda binaria en la tupla para encontrar el objetivo.
    
    Args:
        tupla (Tuple): La tupla ordenada en la que se realizará la búsqueda.
        objetivo (Any): El elemento que se busca en la tupla.
        
    Returns:
        int: El índice del objetivo si se encuentra, o -1 si no se encuentra.
    """

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
