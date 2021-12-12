# -*- coding: utf-8 -*-
"""
mundo.py
Created on Wed Oct  7 14:00:00 2020
@author: mlopez
"""

from animal import Leon, Antilope
from tablero import Tablero

def print_debug(msg, print_flag=False):
    if print_flag:
        print(msg)

class Mundo(object):
    """docstring for Mundo"""

    def __init__(self, columnas, filas, n_leones, n_antilopes, debug=False):
        super(Mundo, self).__init__()
        self.debug = debug
        self.ciclo = 0
        self.tablero = Tablero(filas, columnas)
        self.llenar_mundo(n_leones, n_antilopes)

    def llenar_mundo(self, n_leones, n_antilopes):
        for _ in range(n_leones):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un leon", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Leon())

        for _ in range(n_antilopes):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un Antilope", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Antilope())

    def cant_leones(self):
        return sum([1 for x in self.tablero.elementos() if x.es_leon()])

    def cant_antilopes(self):
        return sum([1 for x in self.tablero.elementos() if x.es_antilope()])

    def etapa_movimiento(self):
        print_debug(f"Iniciando Movimiento en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)

            posiciones_libres = self.tablero.posiciones_vecinas_libre(p)
            nueva_posicion = animal.moverse(posiciones_libres)
            if nueva_posicion:
                self.tablero.mover(p, nueva_posicion)

    def etapa_alimentacion(self):
        print_debug(f"Iniciando Alimentación en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
            desplazo = animal.alimentarse(animales_cercanos)
            if desplazo:
                self.tablero.ubicar(desplazo, self.tablero.retirar(p))

    def etapa_reproduccion(self):
        print_debug(f"Iniciando Reproducción en ciclo {self.ciclo}", self.debug)
        for i in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(i)
            if animal.es_reproductore:
                lista_pos_de_vecinos = self.tablero.posiciones_vecinas_con_ocupantes(i)
                lista_vecinos = [objetos[1] for objetos in lista_pos_de_vecinos]
                for vecino in lista_vecinos:
                    if vecino.es_reproductore:
                        if type(vecino) == type(animal): #son animales de la misma especie
                            if type(animal) == Leon and animal.edad>2:
                                pos1 = Leon.reproducirse(self,lista_vecinos, self.tablero.posiciones_vecinas_libre(i))
                                self.tablero.posiciones[pos1] = Leon()
                                break  # solo se reproducira con un vecino
                            if type(animal) == Antilope and animal.edad>2:
                                pos2 = Antilope.reproducirse(self,lista_vecinos, self.tablero.posiciones_vecinas_libre(i))
                                self.tablero.posiciones[pos2] = Antilope()
                                break  # solo se reproducira con un vecino

    def cerrar_un_ciclo(self):
        print_debug(f"Concluyendo ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animal.pasar_un_ciclo() #envejecer, consumir alimento
            if not animal.en_vida():
                self.tablero.retirar(p)
        self.ciclo += 1

    def pasar_un_ciclo(self):
        self.etapa_movimiento()
        self.etapa_alimentacion()
        self.etapa_reproduccion()
        self.cerrar_un_ciclo()

    def __repr__(self):
        res = str(self.tablero)
        res += f"\nEstamos en la ciclo {self.ciclo}"
        res += f"\nCon {self.cant_leones()} Leones, y {self.cant_antilopes()} Antilopes."
        if False:
            res += '\nEspecie   Posicion   años  energia   puede_reproduc\n'
            for p in self.tablero.posiciones_ocupadas():
                animal = self.tablero.posicion(p)
                res += f'{"Leon    " if animal.es_leon() else "Antilope"} {str(p):^10s} {animal.fila_str()}\n'

        return res

    def __str__(self):
        return self.__repr__()

#(columnas, filas, n_leones, n_antilopes)
m = Mundo(12, 6, 4, 10, debug=True)

import time
for i in range(20):
    m.pasar_un_ciclo()
    time.sleep(1.5)
    print(i +1)
    print(m)