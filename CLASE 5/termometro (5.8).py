# TERMOMETRO 5.8
import random
import numpy as np

mediciones = 999
lista_temp = []
for i in range(mediciones):
    lista_temp.append(round(random.normalvariate(37.5,0.2),3))

print (lista_temp)
print('maximo: ',max(lista_temp))
print('minimo: ',min(lista_temp))
print('promedio: ',round(sum(lista_temp)/len(lista_temp),3))
print('mediana: ',sorted(lista_temp)[int(round(mediciones/2,0))])

print('Q1:',sorted(lista_temp)[int(round(mediciones/4,0))])
print('Q1:',sorted(lista_temp)[int(round(mediciones/2,0))])
print('Q1:',sorted(lista_temp)[int(round(mediciones*3/4,0))])

a = np.array(lista_temp)
#print(a)
np.save('DATA/temperatura', a)

#b = np.load('DATA/temperatura.npy')
#print(b)

