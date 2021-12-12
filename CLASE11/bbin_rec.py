#10.11 bbin_rec

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            return True
        if e > lista[medio] :
            lista = lista[medio:]
        else:
            lista = lista[:medio]
        res = bbinaria_rec(lista, e)

    return res

lista=[1,5,7,56,102,150,220,225,250,345]
e = 102
print(bbinaria_rec(lista, e))
