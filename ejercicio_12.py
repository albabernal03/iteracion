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