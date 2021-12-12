#5.2 Generala no necesariamente servida
import random
from collections import Counter

def tres_tiradas():
    lista = []
    [lista.append(random.randint(1, 6)) for a in range(5)]
    #lista = [1,1,1,1,1]
    j = Counter(lista)
    cantidad_iguales = (list(j.most_common(1)[0])[1])
    el_numero = (list(j.most_common(1)[0])[0])
    if cantidad_iguales == 1:
        cantidad_iguales = 0
    if cantidad_iguales == 5: #Es generala servida
        return (True,'1')
    else:
        lista = []
        [lista.append(random.randint(1, 6)) for a in range(5-cantidad_iguales)]
        l = Counter(lista)
        cantidad_iguales = cantidad_iguales + l[el_numero]

        if cantidad_iguales == 1:
            cantidad_iguales = 0
        if cantidad_iguales == 5:  # Es generala al segundo tiro
            return (True,'2')
        else:
            lista = []
            [lista.append(random.randint(1, 6)) for a in range(5 - cantidad_iguales)]
            m = Counter(lista)
            cantidad_iguales = cantidad_iguales + m[el_numero]

            if cantidad_iguales == 5:  # Es generala al tercer tiro
                return (True,'3')
    return (False,'4')

N = 100000
G = Counter([tres_tiradas() for i in range(N)])
print(G)
print(f'Tiré {N} veces, de las cuales:')
print(G[(True,'1')],' saqué generala servida.')
print(G[(True,'2')],' saqué generala con dos tiros.')
print(G[(True,'3')],' saqué generala con tres tiros.')
Total =G[(True,'1')] + G[(True,'2')] + G[(True,'3')]
print('la probabilidad de obtener generala es:',Total/N)