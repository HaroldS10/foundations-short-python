#!/usr/bin/python3
from typing import Tuple

#tupla 1
numbers: Tuple[int] = (2, 4, 6, 8, 10)

#tupla 2
names = 'harold', 'luis', 'julian'
names: Tuple[str]

#tupla_vacia
tuple_cr: Tuple[int ]= ()

#tupla de instacnia 
my_tuple: Tuple[str] = tuple()


#tupla un elemento
tuple_one: Tuple[str] = ('holberton',)

#tupla creada por un for 
tupla_nueva: Tuple[int] = tuple()
for i in range(5):
    tupla_nueva += (i,)
