def euclides(a: int, b: int) -> int:
   
    if b == 0:
        return a
    else:
        return euclides(b, a % b)
