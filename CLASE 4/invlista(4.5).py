#invertir lista 4.5

def invertir_lista(lista):
    long = len(lista)
    lista2 = []
    i = 1
    while i <= long:
        lista2.append(lista[long-i])
        i += 1
    return lista2

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))