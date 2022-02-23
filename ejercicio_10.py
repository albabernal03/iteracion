nombres = []
edades = []
padress = []
nombre = str(input('Introduzca su nombre y apellido:'))
nombres.append(nombre)
edad = int(input('Introduzca su edad:'))
edades.append(edad)
padres = int(input('Selecione (1) si tiene padres, (2) si solo madre o padre y (3) si no tiene:'))
padress.append(padres)

class información:
    def __init__(self,nombre,edad,padres):
        self.nombre= nombre
        self.edad = edad 
        self.padres = padres 
    def rango_edad (self):
      if 20 < self.edad < 30:
        print('...................')
        print('NOMBRE         EDAD')
        print(nombre, 'ee 


