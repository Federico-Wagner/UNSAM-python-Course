#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de identado en el return False ya que escapaba de la funcion con la primer letra sea o no 'a' .
#    Lo corregí probando las salidas con multiples prints. modificando el identado de  i += 1 y de  return False el cual sale afuera del while
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era sintactico.
# faltaban los : en las 3 posiciones que ahora si aparecen y decia return falso en vez de return false
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era la falta de comillas en el tercer llamado a la funcion el cual no era ingresado como una cadena
# de caracteres sino como una variable la cual no poseeia ningun valor asignado
#    A continuación va el código corregido

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')


#%%
#Ejercicio 3.4 Alcances
# faltaba asignar el valor que debia devolver lña funcion suma: return c
#    A continuación va el código corregido

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


#%%
#Ejercicio 3.5 Pisando memoria
#Genero el archivo registros como nuevos valores en memorias en vez de generar multiples registros los cuales
#se sobreescriben por estar direccionando a la misma posicion de memoria
#    A continuación va el código corregido

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {encabezado[0]:fila[0],encabezado[1]:fila[1],encabezado[2]:fila[2]}
            camion.append(registro)
    return camion
camion = leer_camion('Data/camion.csv')
pprint(camion)