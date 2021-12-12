#9.1 Objetos como estructura de datos
#9.2 Agregá algunos métodos
# 9.9 Mejor salida para objetos
class Lote:
    def __init__(self,nombre,cajones,precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    def __repr__(self):
          return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
    def costo(self):
        return self.cajones * self.precio
    def vender(self,cant):
        self.cajones -= cant
        return self.cajones



a = Lote('Pera', 100, 490.10)
b = Lote('Manzana', 50, 122.34)
c = Lote('Naranja', 75, 91.75)

#print(a)
"""
print(a.nombre)
print(a.cajones)
print(a.precio)
print(a.costo())
print(a.vender(25))
print(a.costo())
"""
#9.3
import fileparse
with open('Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

camion = [ Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]

#print(sum([c.costo() for c in camion]))