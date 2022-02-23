resultado []
print("Escoge el número que desees editar")
numero=int(input())
print("Escoge la base en la que quieras converit el número elegido")
base=int(input())

def entero_cambiar_base(numero,base):
  if base > 36:
    print(numero)