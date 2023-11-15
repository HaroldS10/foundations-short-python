mi_tupla = (1, 2, 3, 'a', 'b')

i = 0
j = -1

for index in mi_tupla:
    print(mi_tupla[i])
    p = (len(mi_tupla) + j)  
    if p == i:
        break
    
    print(mi_tupla[j])

    i += 1
    j -= 1
