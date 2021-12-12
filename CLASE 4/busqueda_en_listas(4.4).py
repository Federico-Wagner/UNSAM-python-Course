#busqueda_en_listas.py 4.4
def buscar_u_elemento(lista,elemento):
    resultado = -1
    cantidad = 0
    for i,x in enumerate(lista):
        if elemento == lista[i]:
            resultado = i
            cantidad +=1
    return resultado,cantidad

print(buscar_u_elemento([1, 2, 3, 2, 3, 4], 1))
buscar_u_elemento([1, 2, 3, 2, 3, 4], 2)
buscar_u_elemento([1, 2, 3, 2, 3, 4], 3)
buscar_u_elemento([1, 2, 3, 2, 3, 4], 5)

def buscar_u_elemento2(lista,elemento):
    cantidad = 0
    for i,x in enumerate(lista):
        if elemento == lista[i]:
            cantidad +=1
    return cantidad

print(buscar_u_elemento2([1, 2, 3, 2, 3, 4], 2))

def maximo (lista):
    m = lista[0]
    for x in lista:
        if x > m:
            m=x
    return m

print('max :',maximo([1, 2, 7, 2, 3, 4]))
print('max :',maximo([1, 2, 3, 4]))
print('max :',maximo([-5, 4]))
print('max :',maximo([-5, -4]))

def minimo (lista):
    m = lista[0]
    for x in lista:
        if x < m:
            m=x
    return m

print('min :',minimo([1, 2, 7, 2, 3, 4]))
print('min :',minimo([1, 2, 3, 4]))
print('min :',minimo([-5, 4]))
print('min :',minimo([-5, -4]))