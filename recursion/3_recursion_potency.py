def potencia(x: float, n: int) -> float:
    if n == 0:
        return 1
    elif n < 0:
        return 1 / (x * potencia(x, n + 1))
    else:
        return x * potencia(x, n - 1)
