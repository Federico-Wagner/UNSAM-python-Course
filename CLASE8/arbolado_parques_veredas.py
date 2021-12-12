#8.9 Comparando especies en parques y en veredas
import matplotlib.pyplot as plt
import pandas as pd
import os

#(1)BASE DE DATOS 1: ARBOLADO EN PARQUES
directorio = r'C:\Users\29-04-21\PycharmProjects\CursoUNSAM\CLASE8\Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df_parques = pd.read_csv(fname,low_memory=False)

#(1)BASE DE DATOS 1: ARBOLADO EN VEREDAS
directorio = r'C:\Users\29-04-21\PycharmProjects\CursoUNSAM\CLASE8\Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df_veredas = pd.read_csv(fname,low_memory=False)

#(2)Adecuacion de loabels del archivo de parques
df_parques = df_parques.rename(columns={"nombre_cie" : "nombre_cientifico"})
df_parques = df_parques.rename(columns={"altura_tot" : "altura_arbol"})
df_parques = df_parques.rename(columns={"diametro" : "diametro_altura_pecho"})

#(2)Seleccion de especie. Base de datos de la especie seleccionada
df_tipas_parques = df_parques[df_parques['nombre_cientifico'] =='Tipuana Tipu']  #si uso copy se rompe
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'].copy()

#(3)agregado de columna "ambiente"   (diferentes metos para que no se rompa todo)
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas.loc[:,'ambiente'] = 'vereda'

#(4)union de data frames
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#Seleccion de columnas de trabajo
columnas_trabajo = ['nombre_cientifico','diametro_altura_pecho','altura_arbol','ambiente']

#DATA-FRAME de trabajo (solo columnas de interes)
df_tipas = df_tipas[columnas_trabajo]
print(df_tipas)

#(5,6) Boxplots
df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
plt.ylabel("Diametro del arbol")

df_tipas.boxplot('altura_arbol',by = 'ambiente')
plt.ylabel("Altura  del arbol")
plt.show()
