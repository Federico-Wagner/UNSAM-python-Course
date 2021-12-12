# Búsqueda binaria 6.14
def donde_insertar(lista, x,verbose = False):
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    izq = 0
    der = len(lista) - 1
    if len(lista) == 0:
        #print('0')
        return 0
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    print(medio)
    return medio

donde_insertar([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],18, verbose = True)
donde_insertar([1, 3, 6], 5, verbose = False)
donde_insertar([1, 3, 5], 5, verbose = False)
donde_insertar([], 5, verbose = False)
print(donde_insertar([0,2,4,6], 4,verbose = False))
print(donde_insertar([0,2,4,6], 3,verbose = False))