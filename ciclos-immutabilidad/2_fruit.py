#!/usr/bin/python3
from typing import Tuple
frutas: Tuple[str] = ('manzana', 'banana', 'cereza')
for fruta in frutas:
  if fruta != 'manzana' :
    print(fruta)
  