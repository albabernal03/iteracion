<h1 align="center">	Iteracion </h1>
<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/iteracion)
***

<h2>¿De qué trata esta tarea?</h2>

En esta tarea resolvemos una serie de ejercicios en el que empleamos funciones.

***

## Indice
1. [Ejercicio 6](#id1)
2. [Ejercicio 7](#id2)
3. [Ejercicio 8](#id3)
4. [Ejercicio 9](#id4)
5. [Ejercicio 10](#id5)
6. [Ejercicio 11](#id6)
7. [Ejercicio 12](#id7)


***

## Ejercicio 6:<a name="id1"></a>

```
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
        self.edad = edad + 1
        print('...................')
        print('NOMBRE         EDAD')
        print(self.nombre,   self.edad)
    def estado_padres (self):
      if padres == 1 or 2:
        print ('Tiene los dos o alguno de los padres ')
      if padres == 3:
        print('Es huérfano')
        print('...................')
        print('NOMBRE         ESTADO')
        print(self.nombre, self.padres)
      if padres == 3 and edad <= 15:
        print('...................')
        print('NOMBRE         ESTADO')
        print(self.nombre, self.padres)
        
    def identidad_padre_jaime(self):
      if self.identidad = "Jaime MARTIN"return self.padre

        




```
***

## Ejercicio 7:<a name="id2"></a>

```
resultado []
print("Escoge el número que desees editar")
numero=int(input())
print("Escoge la base en la que quieras converit el número elegido")
base=int(input())

def entero_cambiar_base(numero,base):
  if base > 36:
    print(numero)
  elif base < 2:
    print("Error, esta base no es válida")
  else:
    resultado.append(numero%base)
    if numero//base == 0:
      print(f"La solución es {resultado}")
    else:
      numero=numero//base
      edici(numero,base)
  edici(numero,base)
```
***

## Ejercicio 8:<a name="id3"></a>
```
import tabulate
def descomposicion():
    cadena = caden.split(separador)
    lista = []
    for i in range(0, len(cadena)):
        lista.append(list(cadena[i: i+1]))
    tabla = lista
    print(tabulate.tabulate(tabla, tablafmt, showindex = True))
```
***

## Ejercicio 9:<a name="id4"></a>

```
palabras = []
palabra1 = str(input('Introduzca una palabra que contenga a:'))
palabras.append(palabra1)
palabra2 = str(input('Introduzca ota palabra que contenga a:'))
palabras.append(palabra2)
palabra3 = str(input('Introduzca la última palabra que contenga a:'))
palabras.append(palabra3)


class palabra:
    def __init__(self,palabra1, palabra2, palabra3):
        self.palabra1 = palabra1
        self.palabra2 = palabra2
        self.palabra3 = palabra3

    def palabras_con_a(self):
        if palabra1.startswith('a') or palabra1.startswith('A') and palabra2.startswith('a') or palabra2.startswith('A') and palabra3.startswith('a')or palabra3.startswith('A'):
            print(palabra1, palabra2,palabra3)
        else:
            pass
    
    def ordenar_alfabéticamente ():
      palabras.sort()
      print(palabras)
      
    def eliminar_palabra():
      eliminar = str(input('Introduce la palabra que desea eliminar:'))
      palabras.remove(eliminar)
      print(palabras)

      
    def añadir_palabra():
      añadir = str(input('Introduzca la palabra que desea añadir'))
      palabras.append(añadir)
      print(palabras)
      
      



```
***

## Ejercicio 10:<a name="id5"></a>


***

## Ejercicio 11:<a name="id6"></a>

```
def euclides_mcd(n, m)
#El Máximo Común Divisor de 'n' y 'm'.
#Enteros naturales n ≥ 0 ; m ≥ 0 y n ≠ 0 y m ≠ 0
#Si n es inferior a m, se invierten
#Obtenemos el resto de la división
    while True:
        resto = n % m
        if resto == 0:
            return m
        # Si n es inferior a m, se invierten
        else:
            n = m
            m = resto
print euclides_mcd(n,m)

# Algoritmo euclídeo solo con sumas o restas
def euclides_mcd(n, m)
    if m == 0:
       return 0,1,0
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    while m != 0:
      q = n//m
      r = n - m * q
      u = u0 - q * u1
      v = v0 - q * v1
      # Actualizamos n,m
      a = b
      b = r
      # Actualizamos para la siguiente operación
      u0 = u1 
      u1 = u
      v0 = v1
      v1 = v
    return a, u0, v0
```
***

## Ejercicio 12:<a name="id7"></a>

```
from math import sqrt

def calcular_cuadrados_perf(n):

  r = []
  s = []
 
  for i in range (n+1):
    s.append(i)

  for t in s:
      if sqrt(t) in s:
        r.append(t)

  print("Los cuadrados perfectos hasta {} son:".format(n))
  
  for x in r:
    print (x)

if __name__ == "__main__":

  n = int(input("Introduzca un numero entero: "))
  calcular_cuadrados_perf(n)
  
  ```
