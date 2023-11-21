from typing import Tuple, Union

def suma_tupla(tupla: Tuple[Union[int, float]]) -> Union[int, float]:
    """
    Calcula la suma de los elementos de una tupla que contiene números enteros o de punto flotante.
    
    Args:
        tupla (Tuple[Union[int, float]]): La tupla de números enteros o de punto flotante.
        
    Returns:
        Union[int, float]: La suma de los elementos de la tupla.
    """
    if not tupla:
        return 0
    return tupla[0] + suma_tupla(tupla[1:])
