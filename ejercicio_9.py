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
      
      
    
    
        

       



