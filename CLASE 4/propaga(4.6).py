# propaga 4.6     0 (nuevo), un 1 (encendido) o un -1 (carbonizado)

def propagar(lista):
    lista_de_menos_1 = [0]
    for i,x in enumerate(lista):
        if x == -1:
            lista_de_menos_1.append(i)
    lista_de_menos_1.append(len(lista))
    segmentos = len(lista_de_menos_1)-1
    #print(lista_de_menos_1)
    limite_inf = 0
    limite_sup = lista_de_menos_1[1]

    for tramo in range(segmentos):
        fuego = False
        for x in range(limite_sup-limite_inf):
            if lista[limite_inf+x] == 1:
                fuego = True
        if fuego:
            for x in range(limite_sup - limite_inf):
                if lista[limite_inf + x] != -1:
                    lista[limite_inf + x] = 1
        if tramo+2 > segmentos:
            break
        limite_inf = lista_de_menos_1[tramo + 1]
        limite_sup = lista_de_menos_1[tramo+2]
    return lista

print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
print(propagar([ 0, 0, 0, 1, 0, 0]))
