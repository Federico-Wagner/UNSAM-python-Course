# 11.14 precio_alquiler ~ superficie

import matplotlib.pyplot as plt
import numpy as np

def ajuste_lineal_simple(x, y):
	"""
	Determina los coeficiente de aproximacion lineal
	"""
	a = sum(((x - x.mean()) * (y - y.mean()))) / sum(((x - x.mean()) ** 2))
	b = y.mean() - a * x.mean()
	return a, b

def calculos():
	"""
	Genera matrices de datos graficar y calcula errores
	"""
	superficie = np.array([150.0, 120.0, 170.0, 80.0])
	alquiler = np.array([35.0, 29.6, 37.4, 21.0])

	a, b = ajuste_lineal_simple(alquiler, superficie)
	grilla_x = np.linspace(start=20, stop=40, num=5)
	grilla_y = grilla_x * a + b

	errores = alquiler - (a * superficie + b)
	print(errores)
	print("ECM:", (errores ** 2).mean())
	return grilla_x,grilla_y,alquiler,superficie

def graficos(grilla_x,grilla_y,alquiler,superficie):
	"""
	Esta funcion grafica los datos y la recta de aproximacion lineal
	"""
	plt.scatter(x=alquiler, y=superficie)  	#grafico datos
	plt.plot(grilla_x, grilla_y, c='green') #grafico recta aproximacion lineal
	plt.title('precio_alquiler ~ superficie')
	plt.xlabel('precio_alquiler')
	plt.ylabel('superficie')
	plt.show()

if __name__ == '__main__':
	(A,B,C,D) = calculos()
	graficos(A,B,C,D)
