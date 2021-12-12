#8.6 Series temporales
import matplotlib.pyplot as plt
import pandas as pd
import os

#BASE DE DATOS:
directorio = r'C:\Users\29-04-21\PycharmProjects\CursoUNSAM\CLASE8\Data'
archivo = 'OBS_SHN_SF-BA.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname,low_memory=False,index_col = ['Time'],parse_dates = True)


dh = df['12-25-2014':].copy() #datos analizados

#8.10 Mareas a mano
delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 21.5 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
plt.show()
