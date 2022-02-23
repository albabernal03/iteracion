nombre = str(input('Introduzca su nombre y apellido:'))
edad = int(input('Introduzca su edad:'))
padres = int(input('Selecione (1) si tiene padres, (2) si solo madre o padre y (3) si no tiene:'))

class información:
    def __init__(self,nombre,edad,padres):
        self.nombre= nombre
        self.edad = edad 
        self.padres = padres 
    
