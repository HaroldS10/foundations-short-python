from typing import Tuple, Union

def ordenamiento_burbuja(tupla: Tuple[Union[str, int]]) -> Tuple[Union[str, int]]:
    """
    Implementa el algoritmo de ordenamiento de burbuja en una tupla.
    
    Args:
        tupla (Tuple): La tupla que se desea ordenar.
        
    Returns:
        Tuple: La tupla ordenada.
    """
    n = len(tupla)
    tupla_ordenada = tuple(tupla)  # Creamos una copia de la tupla para evitar cambios en la original

    # Iteramos a través de todos los elementos de la tupla
    for i in range(n):
        # Últimos i elementos ya están ordenados, no necesitamos volver a verificarlos.
        for j in range(0, n-i-1):
            # Intercambiamos si el elemento encontrado es mayor que el siguiente elemento
            if tupla_ordenada[j] > tupla_ordenada[j+1]:
                # Creamos una tupla temporal con los elementos intercambiados
                tupla_temporal = (
                    *tupla_ordenada[:j],
                    tupla_ordenada[j+1],
                    tupla_ordenada[j],
                    *tupla_ordenada[j+2:]
                )
                # Actualizamos la tupla ordenada con la tupla temporal
                tupla_ordenada = tupla_temporal

    return tupla_ordenada
