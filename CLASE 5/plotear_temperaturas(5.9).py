#Plotear temperaturas 5.9

import numpy as np

datos = np.load('DATA/temperatura.npy')
#print(datos)

import matplotlib.pyplot as plt
plt.hist(datos,bins=25)
plt.show()
