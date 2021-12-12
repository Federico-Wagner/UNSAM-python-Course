# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:45:16 2021

@author: 29-04-21
"""
import random
import matplotlib.pyplot as plt
import numpy as np
import timeit as tt

def generar_lista(N):
	random_list = []
	for _ in range(N):
		element = random.randint(1, 1000)
		random_list.append(element)

	return random_list

listas = []
for N in range(1, 256):
	listas.append(generar_lista(N))

# ////////////////////////////////////////// Ordenamiento por selección //////////////////////////////////////////
def experimento_timeit_seleccion(listas, num):
	"""
	Realiza un experimento usando timeit para evaluar el método
	de selección para ordenamiento de listas
	con las listas pasadas como entrada
	y devuelve los tiempos de ejecución para cada lista
	en un vector.
	El parámetro 'listas' debe ser una lista de listas.
	El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
	"""
	tiempos_seleccion = []

	global lista

	for lista in listas:
		# evalúo el método de selección
		# en una copia nueva para cada iteración
		tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number=num, globals=globals())

		# guardo el resultado
		tiempos_seleccion.append(tiempo_seleccion)

	# paso los tiempos a arrays
	tiempos_seleccion = np.array(tiempos_seleccion)

	return tiempos_seleccion


def ord_seleccion(lista):
	"""Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

	# posición final del segmento a tratar
	n = len(lista) - 1
	comparaciones = 0
	# mientras haya al menos 2 elementos para ordenar
	while n > 0:
		# posición del mayor valor del segmento
		p = buscar_max(lista, 0, n)
		comparaciones += n - 0
		# print(comparaciones)
		# intercambiar el valor que está en p con el valor que
		# está en la última posición del segmento
		lista[p], lista[n] = lista[n], lista[p]
		# print("DEBUG: ", p, n, lista)
		# reducir el segmento en 1
		n = n - 1

	return comparaciones


def buscar_max(lista, a, b):
	"""Devuelve la posición del máximo elemento en un segmento de
	   lista de elementos comparables.
	   La lista no debe ser vacía.
	   a y b son las posiciones inicial y final del segmento"""

	pos_max = a
	for i in range(a + 1, b + 1):
		if lista[i] > lista[pos_max]:
			pos_max = i
	return pos_max
# ////////////////////////////////////////// Ordenamiento por selección //////////////////////////////////////////


# ////////////////////////////////////////// Ordenamiento por inserción //////////////////////////////////////////
def experimento_timeit_insercion(listas, num):
	"""
	Realiza un experimento usando timeit para evaluar el método
	de selección para ordenamiento de listas
	con las listas pasadas como entrada
	y devuelve los tiempos de ejecución para cada lista
	en un vector.
	El parámetro 'listas' debe ser una lista de listas.
	El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
	"""
	tiempos_insercion = []

	global lista

	for lista in listas:
		# evalúo el método de selección
		# en una copia nueva para cada iteración
		tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number=num, globals=globals())

		# guardo el resultado
		tiempos_insercion.append(tiempo_insercion)

	# paso los tiempos a arrays
	tiempos_insercion = np.array(tiempos_insercion)

	return tiempos_insercion


def ord_insercion(lista):
	"""Ordena una lista de elementos según el método de inserción.
	   Pre: los elementos de la lista deben ser comparables.
	   Post: la lista está ordenada."""
	for i in range(len(lista) - 1):
		# Si el elemento de la posición i+1 está desordenado respecto
		# al de la posición i, reubicarlo dentro del segmento [0:i]
		# print(comparaciones)
		if lista[i + 1] < lista[i]:
			reubicar(lista, i + 1)
		# print("DEBUG: ", lista)


def reubicar(lista, p):
	"""Reubica al elemento que está en la posición p de la lista
	   dentro del segmento [0:p-1].
	   Pre: p tiene que ser una posicion válida de lista."""
	v = lista[p]

	# Recorrer el segmento [0:p-1] de derecha a izquierda hasta
	# encontrar la posición j tal que lista[j-1] <= v < lista[j].
	j = p
	while j > 0 and v < lista[j - 1]:
		# Desplazar los elementos hacia la derecha, dejando lugar
		# para insertar el elemento v donde corresponda.
		lista[j] = lista[j - 1]
		j -= 1
	lista[j] = v
# ////////////////////////////////////////// Ordenamiento por inserción //////////////////////////////////////////

# ////////////////////////////////////////// Ordenamiento por BURBUJEO //////////////////////////////////////////
def experimento_timeit_burbujeo(listas, num):
	"""
	Realiza un experimento usando timeit para evaluar el método
	de selección para ordenamiento de listas
	con las listas pasadas como entrada
	y devuelve los tiempos de ejecución para cada lista
	en un vector.
	El parámetro 'listas' debe ser una lista de listas.
	El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
	"""
	tiempos_burbujeo = []

	global lista

	for lista in listas:
		# evalúo el método de selección
		# en una copia nueva para cada iteración
		tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number=num, globals=globals())

		# guardo el resultado
		tiempos_burbujeo.append(tiempo_burbujeo)

	# paso los tiempos a arrays
	tiempos_burbujeo = np.array(tiempos_burbujeo)

	return tiempos_burbujeo


def ord_burbujeo(lista):
	"""
	Recorre la lista dada comparando valores contiguos
	Pre: La lista debe contener numeros
	pos: Entrega una lista ordenada de numeros
	"""
	for iters in range(len(lista) - 1):
		for elem in range(len(lista) - iters - 1):
			if lista[elem] > lista[elem + 1]:
				lista = invertir(lista, elem)


def invertir(lista, pos):
	"""
	Dada una posicion y una lista invierte la posicion dada con la inmediata superior
	Pre: pos < len(lista)-1
	Pos: Devuelve la lista con el valor de pos y el inmediato superior intercambiados
	"""
	val_pos = lista[pos]
	lista[pos] = lista[pos + 1]
	lista[pos + 1] = val_pos

	return lista
# ////////////////////////////////////////// Ordenamiento por BURBUJEO //////////////////////////////////////////

# ////////////////////////////////////////// Ordenamiento por MERGE_SORT ////////////////////////////////////////
def experimento_timeit_merge(listas, num):
	"""
	Realiza un experimento usando timeit para evaluar el método
	de selección para ordenamiento de listas
	con las listas pasadas como entrada
	y devuelve los tiempos de ejecución para cada lista
	en un vector.
	El parámetro 'listas' debe ser una lista de listas.
	El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
	"""
	tiempos_merge = []

	global lista

	for lista in listas:
		# print('aaa',lista)
		# evalúo el método de selección
		# en una copia nueva para cada iteración
		tiempo_merge = tt.timeit('merge_sort(lista)', number=num, globals=globals())

		# guardo el resultado
		tiempos_merge.append(tiempo_merge)

	# paso los tiempos a arrays
	tiempos_merge = np.array(tiempos_merge)

	return tiempos_merge


def merge_sort(lista):
	"""Ordena lista mediante el método merge sort.
	   Pre: lista debe contener elementos comparables.
	   Devuelve: una nueva lista ordenada."""
	if len(lista) < 2:
		lista_nueva = lista
	else:
		medio = len(lista) // 2
		izq = merge_sort(lista[:medio])
		der = merge_sort(lista[medio:])
		lista_nueva = merge(izq, der)

	return lista_nueva


def merge(lista1, lista2):
	"""Intercala los elementos de lista1 y lista2 de forma ordenada.
	   Pre: lista1 y lista2 deben estar ordenadas.
	   Devuelve: una lista con los elementos de lista1 y lista2."""
	i, j = 0, 0
	resultado = []
	while (i < len(lista1) and j < len(lista2)):
		if (lista1[i] < lista2[j]):
			resultado.append(lista1[i])
			i += 1
		else:
			resultado.append(lista2[j])
			j += 1
	# Agregar lo que falta de una lista
	resultado += lista1[i:]
	resultado += lista2[j:]

	return resultado
# ////////////////////////////////////////// Ordenamiento por MERGE_SORT ////////////////////////////////////////



tiempos_seleccion = experimento_timeit_seleccion(listas, 100)
tiempos_insercion = experimento_timeit_insercion(listas, 100)
tiempos_burbujeo = experimento_timeit_burbujeo(listas, 100)
tiempos_merge = experimento_timeit_merge(listas, 100)

plt.plot(tiempos_seleccion, label='seleccion')
plt.plot(tiempos_insercion, label='insercion')
plt.plot(tiempos_burbujeo, label='burbujeo')
plt.plot(tiempos_merge, label='merge')

plt.legend()
plt.show()

"""
Los resultados al evaluar los cuatro metodos de ordenamiento difieren
parcialmente con los resultados obtenidos anteriormente, los metodos de 
inserccion y seleccion insumen un tiempo medio entre el metodo merge y 
por burbujeo
"""
