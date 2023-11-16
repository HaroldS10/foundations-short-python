#!/usr/bin/python3

mi_tupla = (1, 2, 3)
sub_tupla = mi_tupla[1:4]

partes = ((), mi_tupla)
for index, value in enumerate(mi_tupla):
  partes += ((value, ), )
  for j in range(index + 1, len(mi_tupla)):
    partes += ((value, mi_tupla[j], ), )
  
print(partes)
