from typing import Tuple, Union

def quick_sort(tupla: Tuple[Union[int, str]]) -> Tuple[Union[int, str]]:
    """
    Implementa el algoritmo Quick Sort en una tupla.
    
    Args:
        tupla (Tuple): La tupla que se desea ordenar.
        
    Returns:
        Tuple: La tupla ordenada.
    """
    if len(tupla) <= 1:
        return tupla

    pivot = tupla[len(tupla) // 2]
    menores = tuple(elemento for elemento in tupla if elemento < pivot)
    iguales = tuple(elemento for elemento in tupla if elemento == pivot)
    mayores = tuple(elemento for elemento in tupla if elemento > pivot)

    return quick_sort(menores) + iguales + quick_sort(mayores)
