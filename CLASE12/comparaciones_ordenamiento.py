from ej_12_4 import generar_lista ,ord_seleccion, ord_insercion, ord_burbujeo
from ej_12_6 import merge_sort


seleccion = []
insercion = []
burbujeo = []
merge_s = []
Cant = 256

for N in range(Cant):
	list = generar_lista(N)

	seleccion.append(ord_seleccion(list.copy()))
	insercion.append(ord_insercion(list.copy()))
	burbujeo.append(ord_burbujeo(list.copy()))
	merge_s.append(merge_sort(list)[1])  #retorna tupla: (lista ordenada, comparaciones)

import matplotlib.pyplot as plt

plt.plot(range(Cant),seleccion,'r--')
plt.plot(range(Cant),insercion,'g-')
plt.plot(range(Cant),burbujeo,'y-.')
plt.plot(range(Cant),merge_s,'y-.')
plt.show()

"""
Conclusiones: en los tres metodos la complejidad de busqueda
crece en forma exponencial con el tamaño de la lista

en el caso de el ordenamiento por insercion la complejidad si 
se ve afectada por el ordenamiento inicial de la lista.

Ordenamiento por seleccion y burbujeo solo dependeran del tamaño de la lista

Merge sort en los graficos que obttuve requierio una cantidad de comprobaciones mucho menor respecto a los otros metodos
"""