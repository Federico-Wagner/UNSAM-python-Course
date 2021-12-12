#12.2 burbujeo

def ord_burbujeo(lista):
	"""
	Recorre la lista dada comparando valores contiguos
	Pre: La lista debe contener numeros
	pos: Entrega una lista ordenada de numeros
	"""
	n = len(lista)
	for iters in range(len(lista)-1):
		for elem in range(len(lista)-iters-1):
			if lista[elem] > lista[elem+1]:
				lista = invertir(lista,elem)
	#print(lista)
	return(lista)

def invertir(lista,pos):
	"""
	Dada una posicion y una lista invierte la posicion dada con la inmediata superior
	Pre: pos < len(lista)-1
	Pos: Devuelve la lista con el valor de pos y el inmediato superior intercambiados
	"""
	val_pos = lista[pos]
	lista[pos] = lista[pos+1]
	lista[pos + 1] = val_pos
	return lista

if __name__ == "__main__":
	lista_1 = [1, 2, -3, 8, 1, 5]
	lista_2 = [1, 2, 3, 4, 5]
	lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
	lista_4 = [10, 8, 6, 2, -2, -5]
	lista_5 = [2, 5, 1, 0]

	ord_burbujeo(lista_1)
	ord_burbujeo(lista_2)
	ord_burbujeo(lista_3)
	ord_burbujeo(lista_4)
	ord_burbujeo(lista_5)
